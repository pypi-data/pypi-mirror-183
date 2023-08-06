from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_transfer_ssh_key", namespace="aws_transfer")
class SshKey(core.Resource):

    body: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    server_id: Union[str, core.StringOut] = core.attr(str)

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        body: Union[str, core.StringOut],
        server_id: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SshKey.Args(
                body=body,
                server_id=server_id,
                user_name=user_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        body: Union[str, core.StringOut] = core.arg()

        server_id: Union[str, core.StringOut] = core.arg()

        user_name: Union[str, core.StringOut] = core.arg()
