from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VirtualNode(core.Schema):

    virtual_node_name: Union[str, core.StringOut] = core.attr(str)

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

    virtual_router_name: Union[str, core.StringOut] = core.attr(str)

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

    virtual_node: Optional[VirtualNode] = core.attr(VirtualNode, default=None)

    virtual_router: Optional[VirtualRouter] = core.attr(VirtualRouter, default=None)

    def __init__(
        self,
        *,
        virtual_node: Optional[VirtualNode] = None,
        virtual_router: Optional[VirtualRouter] = None,
    ):
        super().__init__(
            args=Provider.Args(
                virtual_node=virtual_node,
                virtual_router=virtual_router,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node: Optional[VirtualNode] = core.arg(default=None)

        virtual_router: Optional[VirtualRouter] = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    provider: Optional[Provider] = core.attr(Provider, default=None)

    def __init__(
        self,
        *,
        provider: Optional[Provider] = None,
    ):
        super().__init__(
            args=Spec.Args(
                provider=provider,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provider: Optional[Provider] = core.arg(default=None)


@core.resource(type="aws_appmesh_virtual_service", namespace="aws_appmesh")
class VirtualService(core.Resource):

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
            args=VirtualService.Args(
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
