from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class IpAddress(core.Schema):

    ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    ip_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        ip_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
        ip: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=IpAddress.Args(
                ip_id=ip_id,
                subnet_id=subnet_id,
                ip=ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ip_id: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_route53_resolver_endpoint", namespace="aws_route53_resolver")
class Endpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    direction: Union[str, core.StringOut] = core.attr(str)

    host_vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Union[List[IpAddress], core.ArrayOut[IpAddress]] = core.attr(
        IpAddress, kind=core.Kind.array
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        direction: Union[str, core.StringOut],
        ip_address: Union[List[IpAddress], core.ArrayOut[IpAddress]],
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                direction=direction,
                ip_address=ip_address,
                security_group_ids=security_group_ids,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        direction: Union[str, core.StringOut] = core.arg()

        ip_address: Union[List[IpAddress], core.ArrayOut[IpAddress]] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
