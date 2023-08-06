from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VirtualService(core.Schema):

    virtual_service_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        virtual_service_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VirtualService.Args(
                virtual_service_name=virtual_service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_service_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Target(core.Schema):

    virtual_service: VirtualService = core.attr(VirtualService)

    def __init__(
        self,
        *,
        virtual_service: VirtualService,
    ):
        super().__init__(
            args=Target.Args(
                virtual_service=virtual_service,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_service: VirtualService = core.arg()


@core.schema
class GrpcRouteAction(core.Schema):

    target: Target = core.attr(Target)

    def __init__(
        self,
        *,
        target: Target,
    ):
        super().__init__(
            args=GrpcRouteAction.Args(
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target: Target = core.arg()


@core.schema
class GrpcRouteMatch(core.Schema):

    service_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        service_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=GrpcRouteMatch.Args(
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        service_name: Union[str, core.StringOut] = core.arg()


@core.schema
class GrpcRoute(core.Schema):

    action: GrpcRouteAction = core.attr(GrpcRouteAction)

    match: GrpcRouteMatch = core.attr(GrpcRouteMatch)

    def __init__(
        self,
        *,
        action: GrpcRouteAction,
        match: GrpcRouteMatch,
    ):
        super().__init__(
            args=GrpcRoute.Args(
                action=action,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: GrpcRouteAction = core.arg()

        match: GrpcRouteMatch = core.arg()


@core.schema
class RewriteHostname(core.Schema):

    default_target_hostname: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        default_target_hostname: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RewriteHostname.Args(
                default_target_hostname=default_target_hostname,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_target_hostname: Union[str, core.StringOut] = core.arg()


@core.schema
class Prefix(core.Schema):

    default_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_prefix: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Prefix.Args(
                default_prefix=default_prefix,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Rewrite(core.Schema):

    hostname: Optional[RewriteHostname] = core.attr(RewriteHostname, default=None)

    prefix: Optional[Prefix] = core.attr(Prefix, default=None)

    def __init__(
        self,
        *,
        hostname: Optional[RewriteHostname] = None,
        prefix: Optional[Prefix] = None,
    ):
        super().__init__(
            args=Rewrite.Args(
                hostname=hostname,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: Optional[RewriteHostname] = core.arg(default=None)

        prefix: Optional[Prefix] = core.arg(default=None)


@core.schema
class Http2RouteAction(core.Schema):

    rewrite: Optional[Rewrite] = core.attr(Rewrite, default=None)

    target: Target = core.attr(Target)

    def __init__(
        self,
        *,
        target: Target,
        rewrite: Optional[Rewrite] = None,
    ):
        super().__init__(
            args=Http2RouteAction.Args(
                target=target,
                rewrite=rewrite,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rewrite: Optional[Rewrite] = core.arg(default=None)

        target: Target = core.arg()


@core.schema
class Http2RouteMatchHostname(core.Schema):

    exact: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        exact: Optional[Union[str, core.StringOut]] = None,
        suffix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Http2RouteMatchHostname.Args(
                exact=exact,
                suffix=suffix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exact: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Http2RouteMatch(core.Schema):

    hostname: Optional[Http2RouteMatchHostname] = core.attr(Http2RouteMatchHostname, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        hostname: Optional[Http2RouteMatchHostname] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Http2RouteMatch.Args(
                hostname=hostname,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: Optional[Http2RouteMatchHostname] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Http2Route(core.Schema):

    action: Http2RouteAction = core.attr(Http2RouteAction)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    def __init__(
        self,
        *,
        action: Http2RouteAction,
        match: Http2RouteMatch,
    ):
        super().__init__(
            args=Http2Route.Args(
                action=action,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Http2RouteAction = core.arg()

        match: Http2RouteMatch = core.arg()


@core.schema
class HttpRoute(core.Schema):

    action: Http2RouteAction = core.attr(Http2RouteAction)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    def __init__(
        self,
        *,
        action: Http2RouteAction,
        match: Http2RouteMatch,
    ):
        super().__init__(
            args=HttpRoute.Args(
                action=action,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Http2RouteAction = core.arg()

        match: Http2RouteMatch = core.arg()


@core.schema
class Spec(core.Schema):

    grpc_route: Optional[GrpcRoute] = core.attr(GrpcRoute, default=None)

    http2_route: Optional[Http2Route] = core.attr(Http2Route, default=None)

    http_route: Optional[HttpRoute] = core.attr(HttpRoute, default=None)

    def __init__(
        self,
        *,
        grpc_route: Optional[GrpcRoute] = None,
        http2_route: Optional[Http2Route] = None,
        http_route: Optional[HttpRoute] = None,
    ):
        super().__init__(
            args=Spec.Args(
                grpc_route=grpc_route,
                http2_route=http2_route,
                http_route=http_route,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc_route: Optional[GrpcRoute] = core.arg(default=None)

        http2_route: Optional[Http2Route] = core.arg(default=None)

        http_route: Optional[HttpRoute] = core.arg(default=None)


@core.resource(type="aws_appmesh_gateway_route", namespace="aws_appmesh")
class GatewayRoute(core.Resource):

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

    virtual_gateway_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        mesh_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        spec: Spec,
        virtual_gateway_name: Union[str, core.StringOut],
        mesh_owner: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayRoute.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                virtual_gateway_name=virtual_gateway_name,
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

        virtual_gateway_name: Union[str, core.StringOut] = core.arg()
