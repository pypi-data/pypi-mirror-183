import json as _json
from dataclasses import dataclass
from enum import Enum
from io import BytesIO
from typing import Tuple

import numpy
import numpy.lib.format as _format
from google.protobuf.json_format import MessageToDict

from qm._QmJobErrors import (
    _handle_job_manager_error,
    MissingElementError,
    ElementWithoutIntermediateFrequencyError,
    ElementWithSingleInputError,
    InvalidElementCorrectionError,
)
from qm._report import ExecutionReport
from qm._results import JobResults
from qm.pb.frontend_pb2 import (
    IsJobRunningRequest,
    IsJobAcquiringDataRequest,
    IsJobAcquiringDataResponse,
    HaltRequest,
    GetSimulatedQuantumStateRequest,
)
from qm.pb.frontend_pb2 import ResumeRequest, PausedStatusRequest
from qm.pb.job_manager_pb2 import (
    SetElementCorrectionRequest,
    GetElementCorrectionRequest,
)
from qm.pb.job_manager_pb2_grpc import JobManagerServiceStub
from qm.pb.job_results_pb2 import PullSimulatorSamplesRequest
from qm.pb.job_results_pb2_grpc import JobResultsServiceStub
from qm.persistence import BinaryAsset
from qm.results.SimulatorSamples import SimulatorSamples
from qm.utils import insert_input_stream_to_job


class AcquiringStatus(Enum):
    AcquireStopped = 0
    NoDataToAcquire = 1
    HasDataToAcquire = 2


@dataclass
class DensityMatrix:
    timestamp: int
    data: numpy.ndarray


class SimulatorOutput:
    def __init__(self, job_id: str, frontend) -> None:
        super().__init__()
        self._id = job_id
        self._frontend = frontend

    def get_quantum_state(self) -> DensityMatrix:
        request = GetSimulatedQuantumStateRequest()
        request.jobId = self._id

        result = self._frontend.GetSimulatedQuantumState(request)
        if result.ok:
            flatten = numpy.array(
                [complex(item.re, item.im) for item in result.state.data]
            )
            n = int(numpy.sqrt(len(flatten)))
            if len(flatten) != (n * n):
                raise RuntimeError("Quantum state matrix is not correct")
            else:
                pass

            matrix = flatten.reshape(n, n)
            timestamp = result.state.timeStamp
            return DensityMatrix(timestamp, matrix)
        else:
            raise RuntimeError("Error while pulling quantum state")


class QmJob:
    def __init__(
        self,
        qmm: "qm.QuantumMachinesManager.QuantumMachinesManager",
        job_id: str,
        execute_response=None,
    ):
        super().__init__()
        self._id = job_id

        self._simulated_analog_outputs = {"samples": None, "waveforms": None}
        self._simulated_digital_outputs = {"samples": None, "waveforms": None}
        if execute_response is not None and execute_response.HasField("simulated"):
            if execute_response.simulated.HasField("analogOutputs"):
                self._simulated_analog_outputs = MessageToDict(
                    execute_response.simulated.analogOutputs
                )
            if execute_response.simulated.HasField("digitalOutputs"):
                self._simulated_digital_outputs = MessageToDict(
                    execute_response.simulated.digitalOutputs
                )
            if len(execute_response.simulated.errors) > 0:
                raise RuntimeError("\n".join(execute_response.simulated.errors))

        self._qmm = qmm
        self._frontend = qmm._frontend
        self._job_manager_client = JobManagerServiceStub(self.manager._channel)

    def id(self):
        """
        :return: The id of the job
        """
        return self._id

    @property
    def manager(self) -> "qm.QuantumMachinesManager.QuantumMachinesManager":
        """
        The QM object where this job lives

        :return:

        """
        return self._qmm

    def simulated_analog_waveforms(self):
        """
        Return the results of the simulation of elements and analog outputs.

        The returned dictionary has the following keys and entries:

        ``elements``: a dictionary containing the outputs with timestamps and values arranged by elements.

        ``controllers``: a dictionary containing the outputs with timestamps and values arranged by controllers.

            ``ports``: a dictionary containing the outputs with timestamps and values arranged by output ports.

                for each element or output port, the entry is a list of dictionaries with the following information:

                ``timestamp``:

                    The time, in nsec, from the start of the program to the start of the pulse.

                ``samples``:

                    Output information, with ``duration`` given in nsec and ``value`` given normalized OPX output units.


        :return: A dictionary containing output information for the analog outputs of the controller.

        """
        return self._simulated_analog_outputs["waveforms"]

    def simulated_digital_waveforms(self):
        """
        Return the results of the simulation of digital outputs.

        ``controllers``: a dictionary containing the outputs with timestamps and values arranged by controllers.

            ``ports``: a dictionary containing the outputs with timestamps and values arranged by output ports.

                for each element or output port, the entry is a list of dictionaries with the following information:

                ``timestamp``:

                    The time, in nsec, from the start of the program to the start of the pulse.

                ``samples``:

                    A list containing the sequence of outputted values, with ``duration`` given in nsec
                    and ``value`` given as a boolean value.



        :return: A dictionary containing output information for the analog outputs of the controller.
        """
        return self._simulated_digital_outputs["waveforms"]

    def halt(self) -> bool:
        """
        Halts the job on the opx
        """
        request = HaltRequest()
        request.jobId = self._id

        response = self._frontend.Halt(request)
        return response.ok

    def _get_np_simulated_samples(
        self, path=None, include_analog=True, include_digital=True
    ):
        request = PullSimulatorSamplesRequest()
        request.jobId = self._id
        request.includeAnalog = include_analog
        request.includeDigital = include_digital
        request.includeAllConnections = True

        writer = BytesIO()
        data_writer = BytesIO()

        for result in self._frontend.PullSimulatorSamples(request):
            if result.ok:
                one_of = result.WhichOneof("body")
                if one_of == "header":
                    _format.write_array_header_2_0(
                        writer,
                        {
                            "descr": _json.loads(result.header.simpleDType),
                            "fortran_order": False,
                            "shape": (result.header.countOfItems,),
                        },
                    )
                elif one_of == "data":
                    data_writer.write(result.data.data)

            else:
                raise RuntimeError("Error while pulling samples")

        data_writer.seek(0)
        for d in data_writer:
            writer.write(d)

        writer.seek(0)
        return numpy.load(writer)

    def get_simulated_samples(self, include_analog=True, include_digital=True):
        """
        Obtain the output samples of a QUA program simulation.

        Samples are returned in an object that holds the controllers in the current simulation,
        where each controller's name will be a property of this object.
        The value of each property of the returned value is an object with the following properties:

        ``analog``:

            holds a dictionary with analog port names as keys and numpy array of samples as values.

        ``digital``:

            holds a dictionary with digital port names as keys and numpy array of samples as values.

        It is also possible to directly plot the outputs using a built-in plot command.

        Example::

            >>> samples = job.get_simulated_samples()
            >>> analog1 = samples.con1.analog["1"]  # obtain analog port 1 of controller "con1"
            >>> digital9 = samples.con1.analog["9"]  # obtain digital port 9 of controller "con1"
            >>> samples.con1.plot()  # Plots all active ports
            >>> samples.con1.plot(analog_ports=['1', '2'], digital_ports=['9'])  # Plots the given output ports

        .. note::

            The simulated digital waveforms are delayed by 136ns relative to the real
            output of the OPX.

        :param include_analog: Should we collect simulated analog samples
        :param include_digital: Should we collect simulated digital samples

        :return: The simulated samples of the job.
        """
        return SimulatorSamples.from_np_array(
            self._get_np_simulated_samples(
                include_analog=include_analog, include_digital=include_digital
            )
        )

    def resume(self):
        """
        Resumes a program that was halted using the pause statement
        """
        request = ResumeRequest()
        request.jobId = self._id
        self._frontend.Resume(request)

    @property
    def result_handles(self) -> JobResults:
        """
        :type: qm._results.JobResults
        :return: The handles that this job generated
        """
        has_job_streaming_state = self.manager._caps.has_job_streaming_state
        if not has_job_streaming_state:
            import qm._results_01

            return qm._results_01.JobResults(
                self._id,
                JobResultsServiceStub(self.manager._channel),
                self.manager.store,
            )
        return JobResults(
            self._id, JobResultsServiceStub(self.manager._channel), self.manager.store
        )

    @property
    def simulator(self) -> SimulatorOutput:
        return SimulatorOutput(self._id, self._frontend)

    def set_element_correction(
        self, element, correction
    ) -> Tuple[float, float, float, float]:
        """
        Sets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer associated with a element.

        Changes will only be done to the current job!

        Values will be rounded to an accuracy of 2^-16.
        Valid values for the correction values are between -2 and (2 - 2^-16).

        Warning - the correction matrix can increase the output voltage which might result in an
        overflow.

        :param element: the name of the element to update the correction for
        :type element: str
        :param correction:

            tuple is of the form (v00, v01, v10, v11) where
            the matrix is
            | v00 v01 |
            | v10 v11 |

        :type correction: tuple
        :return: The correction matrix, after rounding to the OPX resolution.
        """
        request = SetElementCorrectionRequest()
        request.jobId = self._id
        request.qeName = element
        request.correction.v00 = correction[0]
        request.correction.v01 = correction[1]
        request.correction.v10 = correction[2]
        request.correction.v11 = correction[3]

        response = self._job_manager_client.SetElementCorrection(request)
        valid_errors = (
            MissingElementError,
            ElementWithSingleInputError,
            InvalidElementCorrectionError,
            ElementWithoutIntermediateFrequencyError,
        )
        _handle_job_manager_error(request, response, valid_errors)
        return (
            response.correction.v00,
            response.correction.v01,
            response.correction.v10,
            response.correction.v11,
        )

    def get_element_correction(self, element) -> Tuple[float, float, float, float]:
        """
        Gets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer associated with a element.

        :param element: the name of the element to update the correction for
        :type element: str
        :return: The current correction matrix
        """
        request = GetElementCorrectionRequest()
        request.jobId = self._id
        request.qeName = element

        response = self._job_manager_client.GetElementCorrection(request)
        valid_errors = (
            MissingElementError,
            ElementWithSingleInputError,
            ElementWithoutIntermediateFrequencyError,
        )
        _handle_job_manager_error(request, response, valid_errors)
        return (
            response.correction.v00,
            response.correction.v01,
            response.correction.v10,
            response.correction.v11,
        )

    def is_paused(self):
        """
        :return: Returns ``True`` if the job is in a paused state.

        see also:

            ``resume()``
        """
        request = PausedStatusRequest()
        request.jobId = self._id

        response = self._frontend.PausedStatus(request)
        return response.isPaused

    def _is_job_running(self):
        """
        :return: Returns ``True`` if the job is running
        """
        request = IsJobRunningRequest()
        request.jobId = self._id

        response = self._frontend.IsJobRunning(request)
        return response.isRunning

    def _is_data_acquiring(self):
        """
        Returns the data acquiring status.
        The possible statuses are: AcquireStopped, NoDataToAcquire,  HasDataToAcquire

        :return: An AcquiringStatus enum object
        """
        request = IsJobAcquiringDataRequest()
        request.jobId = self._id

        response = self._frontend.IsJobAcquiringData(request)
        result = response.acquiringStatus
        if result == IsJobAcquiringDataResponse.ACQUIRE_STOPPED:
            return AcquiringStatus(0)
        elif result == IsJobAcquiringDataResponse.NO_DATA_TO_ACQUIRE:
            return AcquiringStatus(1)
        elif result == IsJobAcquiringDataResponse.HAS_DATA_TO_ACQUIRE:
            return AcquiringStatus(2)

    def execution_report(self) -> ExecutionReport:
        """
        Get runtime errors report for this job. See `Runtime errors <https://qm-docs.qualang.io/guides/error#runtime-errors>`__.

        :type: qm._report.ExecutionReport
        :return: An object holding the errors that this job generated.
        """
        return ExecutionReport(self._id, JobResultsServiceStub(self.manager._channel))

    def insert_input_stream(
        self,
        name: str,
        data,
    ):
        """
        Insert data to the input stream declared in the QUA program.
        The data is then ready to be read by the program using the advance
        input stream QUA statement.

        Multiple data entries can be inserted before the data is read by the program.

        See `Input streams <https://qm-docs.qualang.io/guides/features#input-streams>`__ for more information.

        -- Available from QOP 2.0 --

        :param name: The input stream name the data is to be inserted to.
        :param data: The data to be inserted. The data's size must match the size of the input stream.
        """
        insert_input_stream_to_job(self, data, name)


class _SavedResults:
    def __init__(self, asset: BinaryAsset) -> None:
        self._asset = asset
        super().__init__()

    def get_numpy_results(self, *args, **kwargs):
        input = self._asset.for_reading()
        try:
            return numpy.load(input)
        finally:
            input.close()
