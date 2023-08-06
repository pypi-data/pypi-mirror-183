from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_security_group_association", namespace="aws_vpc")
class EndpointSecurityGroupAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    replace_default_association: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_group_id: Union[str, core.StringOut] = core.attr(str)

    vpc_endpoint_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        security_group_id: Union[str, core.StringOut],
        vpc_endpoint_id: Union[str, core.StringOut],
        replace_default_association: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointSecurityGroupAssociation.Args(
                security_group_id=security_group_id,
                vpc_endpoint_id=vpc_endpoint_id,
                replace_default_association=replace_default_association,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        replace_default_association: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_group_id: Union[str, core.StringOut] = core.arg()

        vpc_endpoint_id: Union[str, core.StringOut] = core.arg()
