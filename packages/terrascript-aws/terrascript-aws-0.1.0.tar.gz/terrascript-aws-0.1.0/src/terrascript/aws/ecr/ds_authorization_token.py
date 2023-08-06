from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_ecr_authorization_token", namespace="aws_ecr")
class DsAuthorizationToken(core.Data):

    authorization_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    expires_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    password: Union[str, core.StringOut] = core.attr(str, computed=True)

    proxy_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    registry_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        registry_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAuthorizationToken.Args(
                registry_id=registry_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        registry_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
