from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EgressFilter(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EgressFilter.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Spec(core.Schema):

    egress_filter: Union[List[EgressFilter], core.ArrayOut[EgressFilter]] = core.attr(
        EgressFilter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        egress_filter: Union[List[EgressFilter], core.ArrayOut[EgressFilter]],
    ):
        super().__init__(
            args=Spec.Args(
                egress_filter=egress_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_filter: Union[List[EgressFilter], core.ArrayOut[EgressFilter]] = core.arg()


@core.data(type="aws_appmesh_mesh", namespace="aws_appmesh")
class DsMesh(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    mesh_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    spec: Union[List[Spec], core.ArrayOut[Spec]] = core.attr(
        Spec, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        mesh_owner: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMesh.Args(
                name=name,
                mesh_owner=mesh_owner,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mesh_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
