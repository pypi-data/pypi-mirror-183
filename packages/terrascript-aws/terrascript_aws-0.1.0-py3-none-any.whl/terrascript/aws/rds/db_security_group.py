from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Ingress(core.Schema):

    cidr: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_group_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    security_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    security_group_owner_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cidr: Optional[Union[str, core.StringOut]] = None,
        security_group_id: Optional[Union[str, core.StringOut]] = None,
        security_group_name: Optional[Union[str, core.StringOut]] = None,
        security_group_owner_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Ingress.Args(
                cidr=cidr,
                security_group_id=security_group_id,
                security_group_name=security_group_name,
                security_group_owner_id=security_group_owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_db_security_group", namespace="aws_rds")
class DbSecurityGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ingress: Union[List[Ingress], core.ArrayOut[Ingress]] = core.attr(Ingress, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

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
        ingress: Union[List[Ingress], core.ArrayOut[Ingress]],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSecurityGroup.Args(
                ingress=ingress,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ingress: Union[List[Ingress], core.ArrayOut[Ingress]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
