from typing import List, Union

import terrascript.core as core


@core.data(type="aws_transfer_server", namespace="aws_transfer")
class DsServer(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_provider_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    invocation_role: Union[str, core.StringOut] = core.attr(str, computed=True)

    logging_role: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocols: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_policy_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    server_id: Union[str, core.StringOut] = core.attr(str)

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        server_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsServer.Args(
                server_id=server_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        server_id: Union[str, core.StringOut] = core.arg()
