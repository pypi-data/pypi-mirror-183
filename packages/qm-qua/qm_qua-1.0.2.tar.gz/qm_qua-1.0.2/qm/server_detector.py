import dataclasses
from typing import Optional, List, Tuple

import grpc
import grpclib.client
from google.protobuf import empty_pb2
import grpclib.events
from qm.info_service.client import QuaClient
from qm.info_service.info import QuaMachineInfo

from qm.grpc_client_interceptor.response_metadata_collect_client_interceptor import (
    DebugData,
)
from qm.run_async import run_async
from qm.capabilities import ServerCapabilities
from qm.grpc_client_interceptor import (
    header_manipulator_client_interceptor,
    response_metadata_collect_client_interceptor,
)
from qm.pb import frontend_pb2_grpc


@dataclasses.dataclass
class DetectedServer:
    port: int
    host: str
    qop_version: Optional[str]
    grpc_channel: Optional[grpc.Channel]
    # does it implement the QUA service
    qua_implementation: Optional[QuaMachineInfo]
    qua_client: QuaClient
    debug_data: DebugData

    def close_channels(self):
        if self.grpc_channel is not None:
            self.grpc_channel.close()

    @property
    def capabilities(self) -> ServerCapabilities:
        return ServerCapabilities.build(qua_implementation=self.qua_implementation)


def default_interceptors(user_token):
    return [
        header_manipulator_client_interceptor.header_adder_interceptor(
            "x-grpc-service", "gateway"
        ),
        header_manipulator_client_interceptor.header_adder_interceptor(
            "authorization", f"Bearer {user_token}"
        ),
    ]


def detect_server(
    user_token,
    credentials,
    host,
    port_from_user_config: int,
    user_provided_port: Optional[int],
    add_debug_data: bool,
) -> Tuple[Optional[DetectedServer], List[int]]:
    max_message_size = 1024 * 1024 * 100  # 100 mb in bytes
    options = [
        ("grpc.max_receive_message_length", max_message_size),
    ]
    detected = None
    if user_provided_port is None:
        possible_ports_to_try = [port_from_user_config, 80, 9510]
        ports_to_try = []
        for port in possible_ports_to_try:
            if port is not None:
                if int(port) not in ports_to_try:
                    ports_to_try.append(int(port))
    else:
        ports_to_try = [user_provided_port]

    for port in ports_to_try:
        detected = try_server(
            user_token, credentials, options, host, port, add_debug_data
        )
        if detected.qop_version is not None:
            break

    if detected.qop_version is None:
        return None, ports_to_try
    else:
        return detected, ports_to_try


def try_server(
    user_token, credentials, options, host, port, add_debug_data
) -> DetectedServer:
    debug_data = DebugData()
    interceptors = default_interceptors(user_token)
    if add_debug_data:
        interceptors.append(
            response_metadata_collect_client_interceptor.response_metadata_collect_client_interceptor(
                debug_data
            )
        )
    intercept_channel = build_channel(interceptors, credentials, options, host, port)
    frontend = frontend_pb2_grpc.FrontendStub(intercept_channel)

    detected = DetectedServer(
        port=port,
        host=host,
        qop_version=None,
        qua_implementation=None,
        grpc_channel=intercept_channel,
        qua_client=QuaClient(
            host=host,
            port=port,
            grpc_channel_factory=lambda: build_grpclib_channel(
                credentials, user_token, host, port
            ),
        ),
        debug_data=debug_data if add_debug_data else None,
    )
    try:
        req = empty_pb2.Empty()
        res = frontend.GetVersion(req)
        detected.qop_version = str(res.value)
    except grpc.RpcError:
        pass
    try:
        info: QuaMachineInfo = run_async(detected.qua_client.get_server_info())
        detected.qua_implementation = info
    except OSError:
        pass
    return detected


def build_channel(interceptors, credentials, options, host, port):
    address = host + ":" + str(port)
    compression = grpc.Compression.Gzip
    channel = (
        grpc.insecure_channel(
            target=address,
            options=options,
            compression=compression,
        )
        if credentials is None
        else grpc.secure_channel(
            target=address,
            credentials=credentials,
            options=options,
            compression=compression,
        )
    )
    return grpc.intercept_channel(channel, *interceptors)


def build_grpclib_channel(credentials, user_token, host, port):
    channel = grpclib.client.Channel(
        host=host,
        port=port,
        ssl=credentials is not None,
        config=grpclib.client.Configuration(),
    )

    async def send_request(event: grpclib.events.SendRequest):
        event.metadata["x-grpc-service"] = "gateway"
        event.metadata["authorization"] = f"Bearer {user_token}"

    grpclib.events.listen(channel, grpclib.events.SendRequest, send_request)
    return channel
