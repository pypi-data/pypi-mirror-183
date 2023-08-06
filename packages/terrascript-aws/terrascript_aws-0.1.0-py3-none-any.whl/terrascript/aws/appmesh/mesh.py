from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EgressFilter(core.Schema):

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EgressFilter.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    egress_filter: Optional[EgressFilter] = core.attr(EgressFilter, default=None)

    def __init__(
        self,
        *,
        egress_filter: Optional[EgressFilter] = None,
    ):
        super().__init__(
            args=Spec.Args(
                egress_filter=egress_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_filter: Optional[EgressFilter] = core.arg(default=None)


@core.resource(type="aws_appmesh_mesh", namespace="aws_appmesh")
class Mesh(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    mesh_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    spec: Optional[Spec] = core.attr(Spec, default=None)

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
        name: Union[str, core.StringOut],
        spec: Optional[Spec] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Mesh.Args(
                name=name,
                spec=spec,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        spec: Optional[Spec] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
