from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_db_proxy_endpoint", namespace="aws_rds")
class DbProxyEndpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_proxy_endpoint_name: Union[str, core.StringOut] = core.attr(str)

    db_proxy_name: Union[str, core.StringOut] = core.attr(str)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_default: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        db_proxy_endpoint_name: Union[str, core.StringOut],
        db_proxy_name: Union[str, core.StringOut],
        vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_role: Optional[Union[str, core.StringOut]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxyEndpoint.Args(
                db_proxy_endpoint_name=db_proxy_endpoint_name,
                db_proxy_name=db_proxy_name,
                vpc_subnet_ids=vpc_subnet_ids,
                tags=tags,
                tags_all=tags_all,
                target_role=target_role,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_proxy_endpoint_name: Union[str, core.StringOut] = core.arg()

        db_proxy_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()
