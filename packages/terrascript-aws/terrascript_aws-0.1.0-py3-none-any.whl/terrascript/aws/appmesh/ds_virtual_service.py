from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VirtualNode(core.Schema):

    virtual_node_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        virtual_node_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VirtualNode.Args(
                virtual_node_name=virtual_node_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node_name: Union[str, core.StringOut] = core.arg()


@core.schema
class VirtualRouter(core.Schema):

    virtual_router_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        virtual_router_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VirtualRouter.Args(
                virtual_router_name=virtual_router_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_router_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Provider(core.Schema):

    virtual_node: Union[List[VirtualNode], core.ArrayOut[VirtualNode]] = core.attr(
        VirtualNode, computed=True, kind=core.Kind.array
    )

    virtual_router: Union[List[VirtualRouter], core.ArrayOut[VirtualRouter]] = core.attr(
        VirtualRouter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        virtual_node: Union[List[VirtualNode], core.ArrayOut[VirtualNode]],
        virtual_router: Union[List[VirtualRouter], core.ArrayOut[VirtualRouter]],
    ):
        super().__init__(
            args=Provider.Args(
                virtual_node=virtual_node,
                virtual_router=virtual_router,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node: Union[List[VirtualNode], core.ArrayOut[VirtualNode]] = core.arg()

        virtual_router: Union[List[VirtualRouter], core.ArrayOut[VirtualRouter]] = core.arg()


@core.schema
class Spec(core.Schema):

    provider: Union[List[Provider], core.ArrayOut[Provider]] = core.attr(
        Provider, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        provider: Union[List[Provider], core.ArrayOut[Provider]],
    ):
        super().__init__(
            args=Spec.Args(
                provider=provider,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provider: Union[List[Provider], core.ArrayOut[Provider]] = core.arg()


@core.data(type="aws_appmesh_virtual_service", namespace="aws_appmesh")
class DsVirtualService(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    mesh_name: Union[str, core.StringOut] = core.attr(str)

    mesh_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    spec: Union[List[Spec], core.ArrayOut[Spec]] = core.attr(
        Spec, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        mesh_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        mesh_owner: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsVirtualService.Args(
                mesh_name=mesh_name,
                name=name,
                mesh_owner=mesh_owner,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mesh_name: Union[str, core.StringOut] = core.arg()

        mesh_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
