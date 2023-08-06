from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_acmpca_permission", namespace="aws_acmpca")
class Permission(core.Resource):

    actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    certificate_authority_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal: Union[str, core.StringOut] = core.attr(str)

    source_account: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        actions: Union[List[str], core.ArrayOut[core.StringOut]],
        certificate_authority_arn: Union[str, core.StringOut],
        principal: Union[str, core.StringOut],
        source_account: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                actions=actions,
                certificate_authority_arn=certificate_authority_arn,
                principal=principal,
                source_account=source_account,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        certificate_authority_arn: Union[str, core.StringOut] = core.arg()

        principal: Union[str, core.StringOut] = core.arg()

        source_account: Optional[Union[str, core.StringOut]] = core.arg(default=None)
