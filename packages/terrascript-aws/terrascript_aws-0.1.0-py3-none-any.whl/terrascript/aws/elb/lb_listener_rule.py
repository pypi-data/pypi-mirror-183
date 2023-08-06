from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Stickiness(core.Schema):

    duration: Union[int, core.IntOut] = core.attr(int)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        duration: Union[int, core.IntOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Stickiness.Args(
                duration=duration,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: Union[int, core.IntOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class TargetGroup(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    weight: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        weight: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TargetGroup.Args(
                arn=arn,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        weight: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Forward(core.Schema):

    stickiness: Optional[Stickiness] = core.attr(Stickiness, default=None)

    target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]] = core.attr(
        TargetGroup, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]],
        stickiness: Optional[Stickiness] = None,
    ):
        super().__init__(
            args=Forward.Args(
                target_group=target_group,
                stickiness=stickiness,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stickiness: Optional[Stickiness] = core.arg(default=None)

        target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]] = core.arg()


@core.schema
class Redirect(core.Schema):

    host: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    query: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status_code: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status_code: Union[str, core.StringOut],
        host: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[str, core.StringOut]] = None,
        protocol: Optional[Union[str, core.StringOut]] = None,
        query: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Redirect.Args(
                status_code=status_code,
                host=host,
                path=path,
                port=port,
                protocol=protocol,
                query=query,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        query: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status_code: Union[str, core.StringOut] = core.arg()


@core.schema
class FixedResponse(core.Schema):

    content_type: Union[str, core.StringOut] = core.attr(str)

    message_body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        content_type: Union[str, core.StringOut],
        message_body: Optional[Union[str, core.StringOut]] = None,
        status_code: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FixedResponse.Args(
                content_type=content_type,
                message_body=message_body,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_type: Union[str, core.StringOut] = core.arg()

        message_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AuthenticateCognito(core.Schema):

    authentication_request_extra_params: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    on_unauthenticated_request: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_cookie_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    user_pool_arn: Union[str, core.StringOut] = core.attr(str)

    user_pool_client_id: Union[str, core.StringOut] = core.attr(str)

    user_pool_domain: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        user_pool_arn: Union[str, core.StringOut],
        user_pool_client_id: Union[str, core.StringOut],
        user_pool_domain: Union[str, core.StringOut],
        authentication_request_extra_params: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        on_unauthenticated_request: Optional[Union[str, core.StringOut]] = None,
        scope: Optional[Union[str, core.StringOut]] = None,
        session_cookie_name: Optional[Union[str, core.StringOut]] = None,
        session_timeout: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AuthenticateCognito.Args(
                user_pool_arn=user_pool_arn,
                user_pool_client_id=user_pool_client_id,
                user_pool_domain=user_pool_domain,
                authentication_request_extra_params=authentication_request_extra_params,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        on_unauthenticated_request: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_cookie_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        user_pool_arn: Union[str, core.StringOut] = core.arg()

        user_pool_client_id: Union[str, core.StringOut] = core.arg()

        user_pool_domain: Union[str, core.StringOut] = core.arg()


@core.schema
class AuthenticateOidc(core.Schema):

    authentication_request_extra_params: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    authorization_endpoint: Union[str, core.StringOut] = core.attr(str)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    issuer: Union[str, core.StringOut] = core.attr(str)

    on_unauthenticated_request: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_cookie_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    token_endpoint: Union[str, core.StringOut] = core.attr(str)

    user_info_endpoint: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        authorization_endpoint: Union[str, core.StringOut],
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        issuer: Union[str, core.StringOut],
        token_endpoint: Union[str, core.StringOut],
        user_info_endpoint: Union[str, core.StringOut],
        authentication_request_extra_params: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        on_unauthenticated_request: Optional[Union[str, core.StringOut]] = None,
        scope: Optional[Union[str, core.StringOut]] = None,
        session_cookie_name: Optional[Union[str, core.StringOut]] = None,
        session_timeout: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AuthenticateOidc.Args(
                authorization_endpoint=authorization_endpoint,
                client_id=client_id,
                client_secret=client_secret,
                issuer=issuer,
                token_endpoint=token_endpoint,
                user_info_endpoint=user_info_endpoint,
                authentication_request_extra_params=authentication_request_extra_params,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        authorization_endpoint: Union[str, core.StringOut] = core.arg()

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        issuer: Union[str, core.StringOut] = core.arg()

        on_unauthenticated_request: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_cookie_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        token_endpoint: Union[str, core.StringOut] = core.arg()

        user_info_endpoint: Union[str, core.StringOut] = core.arg()


@core.schema
class Action(core.Schema):

    authenticate_cognito: Optional[AuthenticateCognito] = core.attr(
        AuthenticateCognito, default=None
    )

    authenticate_oidc: Optional[AuthenticateOidc] = core.attr(AuthenticateOidc, default=None)

    fixed_response: Optional[FixedResponse] = core.attr(FixedResponse, default=None)

    forward: Optional[Forward] = core.attr(Forward, default=None)

    order: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    redirect: Optional[Redirect] = core.attr(Redirect, default=None)

    target_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        authenticate_cognito: Optional[AuthenticateCognito] = None,
        authenticate_oidc: Optional[AuthenticateOidc] = None,
        fixed_response: Optional[FixedResponse] = None,
        forward: Optional[Forward] = None,
        order: Optional[Union[int, core.IntOut]] = None,
        redirect: Optional[Redirect] = None,
        target_group_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Action.Args(
                type=type,
                authenticate_cognito=authenticate_cognito,
                authenticate_oidc=authenticate_oidc,
                fixed_response=fixed_response,
                forward=forward,
                order=order,
                redirect=redirect,
                target_group_arn=target_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authenticate_cognito: Optional[AuthenticateCognito] = core.arg(default=None)

        authenticate_oidc: Optional[AuthenticateOidc] = core.arg(default=None)

        fixed_response: Optional[FixedResponse] = core.arg(default=None)

        forward: Optional[Forward] = core.arg(default=None)

        order: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        redirect: Optional[Redirect] = core.arg(default=None)

        target_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class HostHeader(core.Schema):

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=HostHeader.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class HttpHeader(core.Schema):

    http_header_name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        http_header_name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=HttpHeader.Args(
                http_header_name=http_header_name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_header_name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class HttpRequestMethod(core.Schema):

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=HttpRequestMethod.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class PathPattern(core.Schema):

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=PathPattern.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class QueryString(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        value: Union[str, core.StringOut],
        key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=QueryString.Args(
                value=value,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceIp(core.Schema):

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=SourceIp.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Condition(core.Schema):

    host_header: Optional[HostHeader] = core.attr(HostHeader, default=None)

    http_header: Optional[HttpHeader] = core.attr(HttpHeader, default=None)

    http_request_method: Optional[HttpRequestMethod] = core.attr(HttpRequestMethod, default=None)

    path_pattern: Optional[PathPattern] = core.attr(PathPattern, default=None)

    query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = core.attr(
        QueryString, default=None, kind=core.Kind.array
    )

    source_ip: Optional[SourceIp] = core.attr(SourceIp, default=None)

    def __init__(
        self,
        *,
        host_header: Optional[HostHeader] = None,
        http_header: Optional[HttpHeader] = None,
        http_request_method: Optional[HttpRequestMethod] = None,
        path_pattern: Optional[PathPattern] = None,
        query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = None,
        source_ip: Optional[SourceIp] = None,
    ):
        super().__init__(
            args=Condition.Args(
                host_header=host_header,
                http_header=http_header,
                http_request_method=http_request_method,
                path_pattern=path_pattern,
                query_string=query_string,
                source_ip=source_ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host_header: Optional[HostHeader] = core.arg(default=None)

        http_header: Optional[HttpHeader] = core.arg(default=None)

        http_request_method: Optional[HttpRequestMethod] = core.arg(default=None)

        path_pattern: Optional[PathPattern] = core.arg(default=None)

        query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = core.arg(
            default=None
        )

        source_ip: Optional[SourceIp] = core.arg(default=None)


@core.resource(type="aws_lb_listener_rule", namespace="aws_elb")
class LbListenerRule(core.Resource):

    action: Union[List[Action], core.ArrayOut[Action]] = core.attr(Action, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    condition: Union[List[Condition], core.ArrayOut[Condition]] = core.attr(
        Condition, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    listener_arn: Union[str, core.StringOut] = core.attr(str)

    priority: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

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
        action: Union[List[Action], core.ArrayOut[Action]],
        condition: Union[List[Condition], core.ArrayOut[Condition]],
        listener_arn: Union[str, core.StringOut],
        priority: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbListenerRule.Args(
                action=action,
                condition=condition,
                listener_arn=listener_arn,
                priority=priority,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[List[Action], core.ArrayOut[Action]] = core.arg()

        condition: Union[List[Condition], core.ArrayOut[Condition]] = core.arg()

        listener_arn: Union[str, core.StringOut] = core.arg()

        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
