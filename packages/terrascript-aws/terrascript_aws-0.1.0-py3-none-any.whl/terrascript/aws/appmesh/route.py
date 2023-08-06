from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class WeightedTarget(core.Schema):

    virtual_node: Union[str, core.StringOut] = core.attr(str)

    weight: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        virtual_node: Union[str, core.StringOut],
        weight: Union[int, core.IntOut],
    ):
        super().__init__(
            args=WeightedTarget.Args(
                virtual_node=virtual_node,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node: Union[str, core.StringOut] = core.arg()

        weight: Union[int, core.IntOut] = core.arg()


@core.schema
class Action(core.Schema):

    weighted_target: Union[List[WeightedTarget], core.ArrayOut[WeightedTarget]] = core.attr(
        WeightedTarget, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        weighted_target: Union[List[WeightedTarget], core.ArrayOut[WeightedTarget]],
    ):
        super().__init__(
            args=Action.Args(
                weighted_target=weighted_target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        weighted_target: Union[List[WeightedTarget], core.ArrayOut[WeightedTarget]] = core.arg()


@core.schema
class Range(core.Schema):

    end: Union[int, core.IntOut] = core.attr(int)

    start: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        end: Union[int, core.IntOut],
        start: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Range.Args(
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        end: Union[int, core.IntOut] = core.arg()

        start: Union[int, core.IntOut] = core.arg()


@core.schema
class MetadataMatch(core.Schema):

    exact: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    range: Optional[Range] = core.attr(Range, default=None)

    regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        exact: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        range: Optional[Range] = None,
        regex: Optional[Union[str, core.StringOut]] = None,
        suffix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MetadataMatch.Args(
                exact=exact,
                prefix=prefix,
                range=range,
                regex=regex,
                suffix=suffix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exact: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        range: Optional[Range] = core.arg(default=None)

        regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Metadata(core.Schema):

    invert: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    match: Optional[MetadataMatch] = core.attr(MetadataMatch, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        invert: Optional[Union[bool, core.BoolOut]] = None,
        match: Optional[MetadataMatch] = None,
    ):
        super().__init__(
            args=Metadata.Args(
                name=name,
                invert=invert,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invert: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        match: Optional[MetadataMatch] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class GrpcRouteMatch(core.Schema):

    metadata: Optional[Union[List[Metadata], core.ArrayOut[Metadata]]] = core.attr(
        Metadata, default=None, kind=core.Kind.array
    )

    method_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metadata: Optional[Union[List[Metadata], core.ArrayOut[Metadata]]] = None,
        method_name: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        service_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=GrpcRouteMatch.Args(
                metadata=metadata,
                method_name=method_name,
                prefix=prefix,
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metadata: Optional[Union[List[Metadata], core.ArrayOut[Metadata]]] = core.arg(default=None)

        method_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PerRetryTimeout(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PerRetryTimeout.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class GrpcRouteRetryPolicy(core.Schema):

    grpc_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    http_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_retries: Union[int, core.IntOut] = core.attr(int)

    per_retry_timeout: PerRetryTimeout = core.attr(PerRetryTimeout)

    tcp_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        max_retries: Union[int, core.IntOut],
        per_retry_timeout: PerRetryTimeout,
        grpc_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        http_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tcp_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=GrpcRouteRetryPolicy.Args(
                max_retries=max_retries,
                per_retry_timeout=per_retry_timeout,
                grpc_retry_events=grpc_retry_events,
                http_retry_events=http_retry_events,
                tcp_retry_events=tcp_retry_events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        http_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_retries: Union[int, core.IntOut] = core.arg()

        per_retry_timeout: PerRetryTimeout = core.arg()

        tcp_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class Idle(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Idle.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class PerRequest(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PerRequest.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class GrpcRouteTimeout(core.Schema):

    idle: Optional[Idle] = core.attr(Idle, default=None)

    per_request: Optional[PerRequest] = core.attr(PerRequest, default=None)

    def __init__(
        self,
        *,
        idle: Optional[Idle] = None,
        per_request: Optional[PerRequest] = None,
    ):
        super().__init__(
            args=GrpcRouteTimeout.Args(
                idle=idle,
                per_request=per_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Optional[Idle] = core.arg(default=None)

        per_request: Optional[PerRequest] = core.arg(default=None)


@core.schema
class GrpcRoute(core.Schema):

    action: Action = core.attr(Action)

    match: Optional[GrpcRouteMatch] = core.attr(GrpcRouteMatch, default=None)

    retry_policy: Optional[GrpcRouteRetryPolicy] = core.attr(GrpcRouteRetryPolicy, default=None)

    timeout: Optional[GrpcRouteTimeout] = core.attr(GrpcRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        match: Optional[GrpcRouteMatch] = None,
        retry_policy: Optional[GrpcRouteRetryPolicy] = None,
        timeout: Optional[GrpcRouteTimeout] = None,
    ):
        super().__init__(
            args=GrpcRoute.Args(
                action=action,
                match=match,
                retry_policy=retry_policy,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        match: Optional[GrpcRouteMatch] = core.arg(default=None)

        retry_policy: Optional[GrpcRouteRetryPolicy] = core.arg(default=None)

        timeout: Optional[GrpcRouteTimeout] = core.arg(default=None)


@core.schema
class Header(core.Schema):

    invert: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    match: Optional[MetadataMatch] = core.attr(MetadataMatch, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        invert: Optional[Union[bool, core.BoolOut]] = None,
        match: Optional[MetadataMatch] = None,
    ):
        super().__init__(
            args=Header.Args(
                name=name,
                invert=invert,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invert: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        match: Optional[MetadataMatch] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Http2RouteMatch(core.Schema):

    header: Optional[Union[List[Header], core.ArrayOut[Header]]] = core.attr(
        Header, default=None, kind=core.Kind.array
    )

    method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Union[str, core.StringOut] = core.attr(str)

    scheme: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        prefix: Union[str, core.StringOut],
        header: Optional[Union[List[Header], core.ArrayOut[Header]]] = None,
        method: Optional[Union[str, core.StringOut]] = None,
        scheme: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Http2RouteMatch.Args(
                prefix=prefix,
                header=header,
                method=method,
                scheme=scheme,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header: Optional[Union[List[Header], core.ArrayOut[Header]]] = core.arg(default=None)

        method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Union[str, core.StringOut] = core.arg()

        scheme: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Http2RouteRetryPolicy(core.Schema):

    http_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_retries: Union[int, core.IntOut] = core.attr(int)

    per_retry_timeout: PerRetryTimeout = core.attr(PerRetryTimeout)

    tcp_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        max_retries: Union[int, core.IntOut],
        per_retry_timeout: PerRetryTimeout,
        http_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tcp_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Http2RouteRetryPolicy.Args(
                max_retries=max_retries,
                per_retry_timeout=per_retry_timeout,
                http_retry_events=http_retry_events,
                tcp_retry_events=tcp_retry_events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_retries: Union[int, core.IntOut] = core.arg()

        per_retry_timeout: PerRetryTimeout = core.arg()

        tcp_retry_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class Http2Route(core.Schema):

    action: Action = core.attr(Action)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    retry_policy: Optional[Http2RouteRetryPolicy] = core.attr(Http2RouteRetryPolicy, default=None)

    timeout: Optional[GrpcRouteTimeout] = core.attr(GrpcRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        match: Http2RouteMatch,
        retry_policy: Optional[Http2RouteRetryPolicy] = None,
        timeout: Optional[GrpcRouteTimeout] = None,
    ):
        super().__init__(
            args=Http2Route.Args(
                action=action,
                match=match,
                retry_policy=retry_policy,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        match: Http2RouteMatch = core.arg()

        retry_policy: Optional[Http2RouteRetryPolicy] = core.arg(default=None)

        timeout: Optional[GrpcRouteTimeout] = core.arg(default=None)


@core.schema
class HttpRoute(core.Schema):

    action: Action = core.attr(Action)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    retry_policy: Optional[Http2RouteRetryPolicy] = core.attr(Http2RouteRetryPolicy, default=None)

    timeout: Optional[GrpcRouteTimeout] = core.attr(GrpcRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        match: Http2RouteMatch,
        retry_policy: Optional[Http2RouteRetryPolicy] = None,
        timeout: Optional[GrpcRouteTimeout] = None,
    ):
        super().__init__(
            args=HttpRoute.Args(
                action=action,
                match=match,
                retry_policy=retry_policy,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        match: Http2RouteMatch = core.arg()

        retry_policy: Optional[Http2RouteRetryPolicy] = core.arg(default=None)

        timeout: Optional[GrpcRouteTimeout] = core.arg(default=None)


@core.schema
class TcpRouteTimeout(core.Schema):

    idle: Optional[Idle] = core.attr(Idle, default=None)

    def __init__(
        self,
        *,
        idle: Optional[Idle] = None,
    ):
        super().__init__(
            args=TcpRouteTimeout.Args(
                idle=idle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Optional[Idle] = core.arg(default=None)


@core.schema
class TcpRoute(core.Schema):

    action: Action = core.attr(Action)

    timeout: Optional[TcpRouteTimeout] = core.attr(TcpRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        timeout: Optional[TcpRouteTimeout] = None,
    ):
        super().__init__(
            args=TcpRoute.Args(
                action=action,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        timeout: Optional[TcpRouteTimeout] = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    grpc_route: Optional[GrpcRoute] = core.attr(GrpcRoute, default=None)

    http2_route: Optional[Http2Route] = core.attr(Http2Route, default=None)

    http_route: Optional[HttpRoute] = core.attr(HttpRoute, default=None)

    priority: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tcp_route: Optional[TcpRoute] = core.attr(TcpRoute, default=None)

    def __init__(
        self,
        *,
        grpc_route: Optional[GrpcRoute] = None,
        http2_route: Optional[Http2Route] = None,
        http_route: Optional[HttpRoute] = None,
        priority: Optional[Union[int, core.IntOut]] = None,
        tcp_route: Optional[TcpRoute] = None,
    ):
        super().__init__(
            args=Spec.Args(
                grpc_route=grpc_route,
                http2_route=http2_route,
                http_route=http_route,
                priority=priority,
                tcp_route=tcp_route,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc_route: Optional[GrpcRoute] = core.arg(default=None)

        http2_route: Optional[Http2Route] = core.arg(default=None)

        http_route: Optional[HttpRoute] = core.arg(default=None)

        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tcp_route: Optional[TcpRoute] = core.arg(default=None)


@core.resource(type="aws_appmesh_route", namespace="aws_appmesh")
class Route(core.Resource):

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

    virtual_router_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        mesh_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        spec: Spec,
        virtual_router_name: Union[str, core.StringOut],
        mesh_owner: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Route.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                virtual_router_name=virtual_router_name,
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

        virtual_router_name: Union[str, core.StringOut] = core.arg()
