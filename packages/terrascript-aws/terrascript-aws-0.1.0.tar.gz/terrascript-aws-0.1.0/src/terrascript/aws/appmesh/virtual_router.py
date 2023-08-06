from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PortMapping(core.Schema):

    port: Union[int, core.IntOut] = core.attr(int)

    protocol: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PortMapping.Args(
                port=port,
                protocol=protocol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port: Union[int, core.IntOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()


@core.schema
class Listener(core.Schema):

    port_mapping: PortMapping = core.attr(PortMapping)

    def __init__(
        self,
        *,
        port_mapping: PortMapping,
    ):
        super().__init__(
            args=Listener.Args(
                port_mapping=port_mapping,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port_mapping: PortMapping = core.arg()


@core.schema
class Spec(core.Schema):

    listener: Listener = core.attr(Listener)

    def __init__(
        self,
        *,
        listener: Listener,
    ):
        super().__init__(
            args=Spec.Args(
                listener=listener,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        listener: Listener = core.arg()


@core.resource(type="aws_appmesh_virtual_router", namespace="aws_appmesh")
class VirtualRouter(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    mesh_name: Union[str, core.StringOut] = core.attr(str)

    mesh_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    spec: Spec = core.attr(Spec)

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
        mesh_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        spec: Spec,
        mesh_owner: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VirtualRouter.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                mesh_owner=mesh_owner,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        mesh_name: Union[str, core.StringOut] = core.arg()

        mesh_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        spec: Spec = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
