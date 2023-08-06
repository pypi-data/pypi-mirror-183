import dataclasses
from typing import Optional

from qm.info_service.info import QuaMachineInfo


@dataclasses.dataclass
class ServerCapabilities:
    has_job_streaming_state: bool
    supports_multiple_inputs_for_element: bool
    supports_analog_delay: bool
    supports_shared_oscillators: bool
    supports_crosstalk: bool
    supports_shared_ports: bool
    supports_input_stream: bool

    @staticmethod
    def build(qua_implementation: Optional[QuaMachineInfo]):
        caps = (
            qua_implementation.capabilities
            if qua_implementation is not None
            else list()
        )
        return ServerCapabilities(
            has_job_streaming_state=_has_job_streaming_state(qua_implementation),
            supports_multiple_inputs_for_element="qm.multiple_inputs_for_element"
            in caps,
            supports_analog_delay="qm.analog_delay" in caps,
            supports_shared_oscillators="qm.shared_oscillators" in caps,
            supports_crosstalk="qm.crosstalk" in caps,
            supports_shared_ports="qm.shared_ports" in caps,
            supports_input_stream="qm.input_stream" in caps,
        )


def _has_job_streaming_state(qua_implementation: Optional[QuaMachineInfo]):
    if qua_implementation is not None:
        return "qm.job_streaming_state" in qua_implementation.capabilities
    return False
