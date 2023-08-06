from dataclasses import dataclass
from typing import List, Dict
import numpy as np


@dataclass
class IterationData:
    iteration_variable_name: str
    iteration_values: np.ndarray


@dataclass
class StreamMetadataError:
    error: str
    location: str


@dataclass
class StreamMetadata:
    stream_name: str
    iteration_values: List[IterationData]


def _get_numpy_array_from_proto_iteration_data(iteration_data) -> np.ndarray:
    if iteration_data.HasField("forEachIntIterationValues"):
        return np.array(iteration_data.forEachIntIterationValues.values)
    elif iteration_data.HasField("forEachDoubleIterationValues"):
        return np.array(iteration_data.forEachDoubleIterationValues.values)
    elif iteration_data.HasField("forDoubleIterationValues"):
        start = iteration_data.forDoubleIterationValues.startValue
        step = iteration_data.forDoubleIterationValues.step
        stop = start + step * iteration_data.forDoubleIterationValues.numberOfIterations
        return np.arange(start=start, step=step, stop=round(stop, 9))
    elif iteration_data.HasField("forIntIterationValues"):
        start = iteration_data.forIntIterationValues.startValue
        step = iteration_data.forIntIterationValues.step
        stop = (
            iteration_data.forIntIterationValues.startValue
            + iteration_data.forIntIterationValues.step
            * iteration_data.forIntIterationValues.numberOfIterations
        )
        return np.arange(start=start, step=step, stop=stop)


def _get_stream_metadata_dict_from_proto_resp(
    program_metadata,
) -> Dict[str, List[StreamMetadata]]:
    stream_metadata_dict = {
        x.streamName: StreamMetadata(
            x.streamName,
            [
                IterationData(
                    y.iterationVariableName,
                    _get_numpy_array_from_proto_iteration_data(y),
                )
                for y in x.iterationData
            ],
        )
        for x in program_metadata.programStreamMetadata.streamMetadata
    }

    return stream_metadata_dict
