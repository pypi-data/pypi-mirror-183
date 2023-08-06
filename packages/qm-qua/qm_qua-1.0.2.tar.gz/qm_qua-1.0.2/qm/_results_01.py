import logging
import time
import zipfile
from io import BufferedWriter, BytesIO
from typing import Optional, Union, Dict, Tuple, Generator, List
import numpy
import numpy.lib.format as _format
import json as _json
from dataclasses import dataclass

from qm.StreamMetadata import (
    StreamMetadata,
    StreamMetadataError,
    _get_stream_metadata_dict_from_proto_resp,
)
from qm.exceptions import InvalidStreamMetadataError
from qm.pb.job_results_pb2_grpc import JobResultsServiceStub
from qm.pb.job_results_pb2 import (
    GetJobNamedResultHeaderRequest,
    GetJobNamedResultRequest,
    GetJobResultSchemaRequest,
    GetJobResultSchemaResponse,
    GetJobDebugDataRequest,
    GetProgramMetadataRequest,
)
from qm.persistence import BaseStore

TIMESTAMPS_LEGACY_EXT = "_timestamps"


logger = logging.getLogger(__name__)


def _parse_dtype(simple_dtype: str) -> dict:
    def hinted_tuple_hook(obj):
        if "__tuple__" in obj:
            return tuple(obj["items"])
        else:
            return obj

    dtype = _json.loads(simple_dtype, object_hook=hinted_tuple_hook)
    return dtype


@dataclass
class JobResultItemSchema:
    name: str
    dtype: dict
    shape: Tuple[int]
    is_single: bool
    expected_count: int


@dataclass
class JobResultSchema:
    items: Dict[str, JobResultItemSchema]


@dataclass
class NamedJobResultHeader:
    count_so_far: int
    is_single: bool
    output_name: str
    job_id: str
    d_type: dict
    shape: Tuple[int]
    done: bool
    closed: bool
    has_dataloss: bool


class BaseNamedJobResult:
    def __init__(
        self,
        job_id: str,
        schema: JobResultItemSchema,
        service: JobResultsServiceStub,
        store: BaseStore,
        stream_metadata_errors: List[StreamMetadataError],
        stream_metadata: StreamMetadata,
    ) -> None:
        super().__init__()
        self._job_id = job_id
        self._schema = schema
        self._service = service
        self._store = store
        self._stream_metadata_errors = stream_metadata_errors
        self._stream_metadata = stream_metadata

    @property
    def name(self) -> str:
        """The name of result this handle is connected to"""
        return self._schema.name

    @property
    def job_id(self) -> str:
        """The job id this result came from"""
        return self._job_id

    @property
    def expected_count(self) -> int:
        return self._schema.expected_count

    @property
    def numpy_dtype(self):
        return self._schema.dtype

    @property
    def stream_metadata(self) -> StreamMetadata:
        """Provides the StreamMetadata of this stream.

        Metadata currently includes the values and shapes of the automatically identified loops
        in the program.

        """
        if len(self._stream_metadata_errors) > 0:
            logger.error("Error creating stream metadata:")
            for x in self._stream_metadata_errors:
                logger.error(f"{x.error} in {x.location}")
            raise InvalidStreamMetadataError(self._stream_metadata_errors)
        return self._stream_metadata

    def save_to_store(
        self, writer: Optional[Union[BufferedWriter, BytesIO, str]] = None, **kwargs
    ) -> int:
        """Saving to persistent store the NPY data of this result handle

        :param writer: An optional writer to override the store defined in \
            :class:`QuantumMachinesManager<qm.QuantumMachinesManager.QuantumMachinesManager>`

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        :return: The number of items saved

        """
        kwargs.get("flat_struct")  # for hints
        own_writer = False
        if writer is None:
            own_writer = True
            writer = self._store.job_named_result(
                self._job_id, self._schema.name
            ).for_writing()
        try:
            header = self._get_named_header(**kwargs)
            return self._save_to_file(header, writer)
        finally:
            if own_writer:
                writer.close()

    def wait_for_values(self, count: int = 1, timeout: Optional[float] = None):
        """Wait until we know at least `count` values were processed for this named result

        :param count: The number of items to wait for
        :param timeout: Timeout for waiting in seconds
        :return:
        """
        start = time.time()
        end = start + max(0.0, timeout) if timeout is not None else None
        while end is None or time.time() < end:
            if self.count_so_far() >= count:
                return
            time.sleep(0.01)

    def wait_for_all_values(self, timeout: Optional[float] = None) -> bool:
        """Wait until we know all values were processed for this named result

        :param timeout: Timeout for waiting in seconds
        :return: True if job finished successfully and False if job has closed before done
        """
        start = time.time()
        end = start + max(0.0, timeout) if timeout is not None else None
        while end is None or time.time() < end:
            header = self._get_named_header()
            if header.done or header.closed:
                return header.done
            time.sleep(0.01)
        raise TimeoutError(f"result {self.name} was not done in time")

    def is_processing(self) -> bool:
        header = self._get_named_header()
        return not (header.done or header.closed)

    def count_so_far(self) -> int:
        """
        also `len(handle)`

        :return: The number of values this result has so far
        """
        return self._get_named_header().count_so_far

    def __len__(self) -> int:
        return self.count_so_far()

    def has_dataloss(self) -> bool:
        """
        :return: if there was data loss during job execution
        """
        return self._get_named_header().has_dataloss

    def _write_header(
        self,
        writer: Union[BufferedWriter, BytesIO, str],
        shape: Tuple[int],
        d_type: object,
    ):
        _format.write_array_header_2_0(
            writer, {"descr": d_type, "fortran_order": False, "shape": shape}
        )

    def _save_to_file(
        self, header: NamedJobResultHeader, writer: Union[BufferedWriter, BytesIO, str]
    ) -> int:
        count = 0
        request = GetJobNamedResultRequest()
        request.jobId = self._job_id
        request.outputName = self.name
        request.longOffset.value = 0
        request.limit = header.count_so_far

        owning_writer = False
        if type(writer) is str:
            writer = open(writer, "wb+")
            owning_writer = True

        try:
            finalShape = self._get_final_shape(header.count_so_far, header.shape)

            self._write_header(writer, finalShape, header.d_type)
            for result in self._service.GetJobNamedResult(request):
                count += result.countOfItems
                writer.write(result.data)

        finally:
            if owning_writer:
                writer.close()
        return count

    def _get_named_header(self, **kwargs) -> NamedJobResultHeader:
        request = GetJobNamedResultHeaderRequest()
        request.jobId = self._job_id
        request.outputName = self.name
        if kwargs.get("flat_struct", False) is True:
            request.flatFormat = True
        response = self._service.GetJobNamedResultHeader(request)
        dtype = _parse_dtype(response.simpleDType)

        if (
            kwargs.get("check_for_errors", False)
            and response.HasField("hasExecutionErrors")
            and response.hasExecutionErrors.value
        ):
            logger.error(
                "Errors were detected, please fetch the execution report for more "
                "information."
            )

        return NamedJobResultHeader(
            count_so_far=response.countSoFar,
            is_single=response.isSingle,
            output_name=self.name,
            job_id=self.job_id,
            d_type=dtype,
            shape=tuple(response.shape),
            done=response.done,
            closed=response.closed,
            has_dataloss=response.hasDataloss,
        )

    def fetch_all(self, **kwargs):
        """
        Fetch a result from the current result stream saved in server memory.
        The result stream is populated by the save() and save_all() statements.
        Note that if save_all() statements are used, calling this function twice
        may give different results.

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        :return: all result of current result stream

        """
        kwargs.get("flat_struct")  # for hints
        return self.fetch(slice(0, len(self)), **kwargs)

    def fetch(self, item: Union[int, slice], **kwargs) -> numpy.array:
        """
        Fetch a result from the current result stream saved in server memory.
        The result stream is populated by the save() and save_all() statements.
        Note that if save_all() statements are used, calling this function twice
        with the same item index may give different results.

        :param item: The index of the result in the saved results stream.

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        :return: a single result if item is integer or multiple results if item is Python slice object.

        Example::
        >>>res.fetch(0) #return the item in the top position
        >>>res.fetch(1) #return the item in position number 2
        >>>res.fetch(slice(1,6))# return items from position 1 to position 6 inclusive

        """
        kwargs.get("flat_struct")  # for hints
        if type(item) is int:
            start = item
            stop = item + 1
            step = None
        elif type(item) is slice:
            start = item.start
            stop = item.stop
            step = item.step
        else:
            raise Exception("fetch supports only int or slice")

        if step != 1 and step is not None:
            raise Exception("fetch supports step=1 or None in slices")

        if kwargs.get("check_for_errors") is None:
            header = self._get_named_header(**kwargs, check_for_errors=True)
        else:
            header = self._get_named_header(**kwargs)

        if stop is None:
            stop = header.count_so_far
        if start is None:
            start = 0

        writer = BytesIO()
        count = 0
        request = GetJobNamedResultRequest()
        request.jobId = self._job_id
        request.outputName = self._schema.name
        request.longOffset.value = start
        request.limit = stop - start

        data_writer = BytesIO()
        for result in self._service.GetJobNamedResult(request):
            count += result.countOfItems
            data_writer.write(result.data)

        finalShape = self._get_final_shape(count, header.shape)

        self._write_header(writer, finalShape, header.d_type)

        data_writer.seek(0)
        for d in data_writer:
            writer.write(d)

        writer.seek(0)

        if header.has_dataloss:
            logger.warning(
                f"Possible data loss detected in data for job: {self._job_id}"
            )

        return numpy.load(writer)

    @staticmethod
    def _get_final_shape(count, shape):
        if count == 1:
            finalShape = shape
        else:
            if len(shape) == 1 and shape[0] == 1:
                finalShape = (count,)
            else:
                finalShape = (count,) + shape
        return finalShape


class MultipleNamedJobResult(BaseNamedJobResult):
    """
    A handle to a result of a pipeline terminating with ``save_all``
    """

    def __init__(
        self,
        job_id: str,
        schema: JobResultItemSchema,
        service: JobResultsServiceStub,
        store: BaseStore,
        stream_metadata_errors: List[StreamMetadataError],
        jobResults,
        stream_metadata: StreamMetadata,
    ) -> None:
        if schema.is_single:
            raise Exception("expecting a multi-result schema")
        self.jobResults = jobResults
        super().__init__(
            job_id, schema, service, store, stream_metadata_errors, stream_metadata
        )

    def _wait_for_any_value(self):
        self.wait_for_values(count=1, timeout=0.5)

    def fetch(self, item: Union[int, slice], **kwargs) -> numpy.array:
        """
        Fetch a result from the current result stream saved in server memory.
        The result stream is populated by the save() and save_all() statements.
        Note that if save_all() statements are used, calling this function twice
        with the same item index may give different results.

        :param item: The index of the result in the saved results stream.

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        :return: a single result if item is integer or multiple results if item is Python slice object.

        Example::
        >>>res.fetch(0) #return the item in the top position
        >>>res.fetch(1) #return the item in position number 2
        >>>res.fetch(slice(1,6))# return items from position 1 to position 6 inclusive

        """
        if kwargs.get("flat_struct"):
            return super().fetch(item, **kwargs)
        else:
            # legacy support - reconstruct the old structure
            name = self._schema.name
            timestampsName = name + TIMESTAMPS_LEGACY_EXT
            timestampsResultHandle = self.jobResults.get(timestampsName)
            if timestampsResultHandle is None:
                return super().fetch(item, **kwargs)
            else:
                valuesResult = super().fetch(item, **kwargs, flat_struct=True)

                fetchedLength = len(valuesResult)
                if isinstance(item, slice):
                    item = slice(item.start, item.start + fetchedLength, item.step)
                else:
                    item = slice(0, fetchedLength, 1)

                timestampsResult = timestampsResultHandle.fetch(
                    item, **kwargs, flat_struct=True, check_for_errors=False
                )

                dtype = [
                    ("value", valuesResult.dtype),
                    ("timestamp", timestampsResult.dtype),
                ]  # timestampsResult.dtype.descr
                combined = numpy.rec.fromarrays(
                    [valuesResult, timestampsResult], dtype=dtype
                )
                return combined.view(numpy.ndarray).astype(dtype)

    def save_to_store(
        self, writer: Optional[Union[BufferedWriter, BytesIO, str]] = None, **kwargs
    ) -> int:
        """Saving to persistent store the NPY data of this result handle

        :param writer: An optional writer to override the store defined in \
                        :class:`QuantumMachinesManager<qm.QuantumMachinesManager.QuantumMachinesManager>`

        :return: The number of items saved

        """
        if kwargs.get("flat_struct"):
            return super().save_to_store(writer, **kwargs)
        else:
            # legacy support - reconstruct the old structure
            name = self._schema.name
            timestampsName = name + TIMESTAMPS_LEGACY_EXT
            timestampsResultHandle = self.jobResults.get(timestampsName)
            if timestampsResultHandle is None:
                return super().save_to_store(writer, **kwargs)
            else:
                final_result = self.fetch_all(**kwargs)
                own_writer = False
                if writer is None:
                    own_writer = True
                    writer = self._store.job_named_result(
                        self._job_id, self._schema.name
                    ).for_writing()
                try:
                    owning_writer = False
                    if type(writer) is str:
                        writer = open(writer, "wb+")
                        owning_writer = True

                    try:
                        self._write_header(
                            writer, (len(final_result),), final_result.dtype.descr
                        )
                        writer.write(final_result.tobytes())

                    finally:
                        if owning_writer:
                            writer.close()
                    return len(final_result)
                finally:
                    if own_writer:
                        writer.close()


class SingleNamedJobResult(BaseNamedJobResult):
    """
    A handle to a result of a pipeline terminating with ``save``
    """

    def __init__(
        self,
        job_id: str,
        schema: JobResultItemSchema,
        service: JobResultsServiceStub,
        store: BaseStore,
        stream_metadata_errors: List[StreamMetadataError],
        stream_metadata: StreamMetadata,
    ) -> None:
        if not schema.is_single:
            raise Exception("expecting a single-result schema")
        super().__init__(
            job_id, schema, service, store, stream_metadata_errors, stream_metadata
        )

    def wait_for_values(self, count: int = 1, timeout: Optional[float] = None):
        if count != 1:
            raise RuntimeError("single result can wait only for a single value")
        return super().wait_for_values(1, timeout)

    def fetch_all(self, **kwargs):
        """
        Fetch a result from the current result stream saved in server memory.
        The result stream is populated by the save() and save_all() statements.
        Note that if save_all() statements are used, calling this function twice
        may give different results.

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        :return: all result of current result stream

        """
        kwargs.get("flat_struct")  # for hints
        return self.fetch(0, **kwargs)

    def fetch(self, item: Union[int, slice], **kwargs):

        """
        Fetch a single result from the current result stream saved in server memory.
        The result stream is populated by the save().

        :param item: ignored

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        :return: the current result

        Example::
        >>>res.fetch() #return the item in the top position

        """
        if (isinstance(item, int) and item != 0) or isinstance(item, slice):
            logger.warning("Fetching single result will always return the single value")
        value = super().fetch(0, **kwargs)
        if kwargs.get("flat_struct", False) is True:
            if len(value) == 0:
                return None
            elif len(value) == 1:
                return value[0]
            else:
                return value
        else:
            if len(value) == 0:
                return None
            elif len(value[0]) == 1:
                return value[0][0]
            else:
                return value[0]


class JobResults:
    """
    Access to the results of a QmJob

    This object is created by calling :attr:`QmJob.result_handles<qm.QmJob.QmJob.result_handles>`

    Assuming you have an instance of JobResults::

        job_results:JobResults

    This object is iterable::

        for name, handle in job_results:
            print(name)

    Can detect if a name exists::

        if "somename" in job_results:
            print("somename exists!")
            handle = job_results.get("somename")

    """

    def __init__(
        self, job_id: str, service: JobResultsServiceStub, store: BaseStore
    ) -> None:
        super().__init__()
        self._job_id = job_id
        self._service = service
        self._store = store
        schema = JobResults._load_schema(job_id, service)
        self._schema = schema
        (stream_metadata_errors, stream_metadata_dict) = self._get_stream_metadata()

        self._all_results: Dict[str, BaseNamedJobResult] = {}
        for (name, item_schema) in schema.items.items():
            stream_metadata = stream_metadata_dict.get(name)
            if item_schema.is_single:
                result = SingleNamedJobResult(
                    job_id,
                    item_schema,
                    service,
                    store,
                    stream_metadata_errors,
                    stream_metadata,
                )
            else:
                result = MultipleNamedJobResult(
                    job_id,
                    item_schema,
                    service,
                    store,
                    stream_metadata_errors,
                    self,
                    stream_metadata,
                )
            self._all_results[name] = result
            if not hasattr(self, name):
                setattr(self, name, result)

    def _get_stream_metadata(
        self,
    ) -> Optional[Tuple[List[StreamMetadataError], Dict[str, StreamMetadata]]]:
        request = GetProgramMetadataRequest()
        request.jobId = self._job_id
        program_metadata = self._service.GetProgramMetadata(request)

        if program_metadata.success:
            stream_metadata_errors = [
                StreamMetadataError(x.error, x.location)
                for x in program_metadata.programStreamMetadata.streamMetadataExtractionError
            ]

            stream_metadata_dict = {}
            if len(stream_metadata_errors) == 0:
                stream_metadata_dict = _get_stream_metadata_dict_from_proto_resp(
                    program_metadata
                )

            return stream_metadata_errors, stream_metadata_dict

        return None

    def __iter__(self) -> Generator[Tuple[str, BaseNamedJobResult], None, None]:
        for item in self._schema.items.values():
            yield item.name, self.get(item.name)

    def is_processing(self) -> bool:
        """Check if the job is still processing results

        :return: True if results are still being processed, False otherwise
        """
        key = list(self._all_results.keys())[0]
        return self._all_results[key].is_processing()

    def save_to_store(
        self, writer: Optional[Union[BufferedWriter, BytesIO, str]] = None, **kwargs
    ):
        """Save all results to store (file system by default) in a single NPZ file

        :param writer: An optional writer to be used instead of the pre-populated \
            store passed to :class:`qm.QuantumMachinesManager.QuantumMachinesManager`

        :key flat_struct: results will have a flat structure - dimensions will be \
            part of the shape and not of the type

        """
        kwargs.get("flat_struct")  # for hints
        own_writer = False
        if writer is None:
            own_writer = True
            writer = self._store.all_job_results(self._job_id).for_writing()
        zipf = None
        try:
            zipf = zipfile.ZipFile(
                writer, allowZip64=True, mode="w", compression=zipfile.ZIP_DEFLATED
            )
            for (name, result) in self:
                with zipf.open(f"{name}.npy", "w") as entry:
                    result.save_to_store(entry, **kwargs)
                pass
        finally:
            zipf.close()
            if own_writer:
                writer.close()

    @staticmethod
    def _load_schema(job_id: str, service: JobResultsServiceStub) -> JobResultSchema:
        request = GetJobResultSchemaRequest()
        request.jobId = job_id
        response: GetJobResultSchemaResponse = service.GetJobResultSchema(request)
        return JobResultSchema(
            {
                item.name: JobResultItemSchema(
                    item.name,
                    _parse_dtype(item.simpleDType),
                    tuple(item.shape),
                    item.isSingle,
                    item.expectedCount,
                )
                for item in response.items
            }
        )

    def get(
        self, name: str
    ) -> Optional[Union[MultipleNamedJobResult, SingleNamedJobResult]]:
        """Get a handle to a named result from :func:`stream_processing<qm.qua._dsl.stream_processing>`

        :param name: The named result using in :func:`stream_processing<qm.qua._dsl.stream_processing>`
        :return: A handle object to the results :class:`MultipleNamedJobResult` or :class:`SingleNamedJobResult` \
                or None if the named results in unknown

        """
        return self._all_results[name] if name in self._all_results else None

    def __contains__(self, name: str):
        return name in self._all_results

    def wait_for_all_values(self, timeout: Optional[float] = None) -> bool:
        """Wait until we know all values were processed for all named results

        :param timeout: Timeout for waiting in seconds
        :return: True if all finished successfully, False if any result was closed before done
        """
        start = time.time()
        end: Optional[int] = start + max(0.0, timeout) if timeout is not None else None
        keys = list(self._all_results.keys())
        all_done = True
        while len(keys) > 0 and (end is None or time.time() < end):
            result = self._all_results[keys[0]]
            time_remaining = None
            if end is not None:
                time_remaining = max(0.0, end - time.time())
            all_done = all_done and result.wait_for_all_values(time_remaining)
            keys = keys[1:]
        return all_done

    def get_debug_data(
        self, writer: Optional[Union[BufferedWriter, BytesIO, str]] = None
    ):
        """

        :return: debugging data to report to QM
        """
        request = GetJobDebugDataRequest()
        request.jobId = self._job_id

        if writer is None:
            writer = f"./{self._job_id}-DebugData.zip"

        owning_writer = False
        if type(writer) is str:
            writer = open(writer, "wb+")
            owning_writer = True

        try:
            for result in self._service.GetJobDebugData(request):
                writer.write(result.data)

        finally:
            if owning_writer:
                writer.close()
