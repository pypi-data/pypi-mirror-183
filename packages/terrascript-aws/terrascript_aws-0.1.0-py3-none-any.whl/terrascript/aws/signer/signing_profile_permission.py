from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_signer_signing_profile_permission", namespace="aws_signer")
class SigningProfilePermission(core.Resource):

    action: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal: Union[str, core.StringOut] = core.attr(str)

    profile_name: Union[str, core.StringOut] = core.attr(str)

    profile_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    statement_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    statement_id_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        action: Union[str, core.StringOut],
        principal: Union[str, core.StringOut],
        profile_name: Union[str, core.StringOut],
        profile_version: Optional[Union[str, core.StringOut]] = None,
        statement_id: Optional[Union[str, core.StringOut]] = None,
        statement_id_prefix: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningProfilePermission.Args(
                action=action,
                principal=principal,
                profile_name=profile_name,
                profile_version=profile_version,
                statement_id=statement_id,
                statement_id_prefix=statement_id_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[str, core.StringOut] = core.arg()

        principal: Union[str, core.StringOut] = core.arg()

        profile_name: Union[str, core.StringOut] = core.arg()

        profile_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        statement_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        statement_id_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
