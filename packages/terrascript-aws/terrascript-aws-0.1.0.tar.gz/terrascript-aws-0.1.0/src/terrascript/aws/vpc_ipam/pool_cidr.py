from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CidrAuthorizationContext(core.Schema):

    message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    signature: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: Optional[Union[str, core.StringOut]] = None,
        signature: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CidrAuthorizationContext.Args(
                message=message,
                signature=signature,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        signature: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_vpc_ipam_pool_cidr", namespace="aws_vpc_ipam")
class PoolCidr(core.Resource):

    cidr: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    cidr_authorization_context: Optional[CidrAuthorizationContext] = core.attr(
        CidrAuthorizationContext, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipam_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ipam_pool_id: Union[str, core.StringOut],
        cidr: Optional[Union[str, core.StringOut]] = None,
        cidr_authorization_context: Optional[CidrAuthorizationContext] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolCidr.Args(
                ipam_pool_id=ipam_pool_id,
                cidr=cidr,
                cidr_authorization_context=cidr_authorization_context,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cidr_authorization_context: Optional[CidrAuthorizationContext] = core.arg(default=None)

        ipam_pool_id: Union[str, core.StringOut] = core.arg()
