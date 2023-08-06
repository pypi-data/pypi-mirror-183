from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_codeartifact_authorization_token", namespace="aws_codeartifact")
class DsAuthorizationToken(core.Data):

    authorization_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain: Union[str, core.StringOut] = core.attr(str)

    domain_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    duration_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    expiration: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        domain: Union[str, core.StringOut],
        domain_owner: Optional[Union[str, core.StringOut]] = None,
        duration_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAuthorizationToken.Args(
                domain=domain,
                domain_owner=domain_owner,
                duration_seconds=duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: Union[str, core.StringOut] = core.arg()

        domain_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        duration_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)
