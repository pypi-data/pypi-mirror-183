from typing import Dict, List, Optional, Union

import terrascript.core as core


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
class AuthenticateCognito(core.Schema):

    authentication_request_extra_params: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    on_unauthenticated_request: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    session_cookie_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    session_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

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

    scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    session_cookie_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    session_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

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
class DefaultAction(core.Schema):

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
            args=DefaultAction.Args(
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


@core.resource(type="aws_lb_listener", namespace="aws_elb")
class LbListener(core.Resource):

    alpn_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_action: Union[List[DefaultAction], core.ArrayOut[DefaultAction]] = core.attr(
        DefaultAction, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_arn: Union[str, core.StringOut] = core.attr(str)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    ssl_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        default_action: Union[List[DefaultAction], core.ArrayOut[DefaultAction]],
        load_balancer_arn: Union[str, core.StringOut],
        alpn_policy: Optional[Union[str, core.StringOut]] = None,
        certificate_arn: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        protocol: Optional[Union[str, core.StringOut]] = None,
        ssl_policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbListener.Args(
                default_action=default_action,
                load_balancer_arn=load_balancer_arn,
                alpn_policy=alpn_policy,
                certificate_arn=certificate_arn,
                port=port,
                protocol=protocol,
                ssl_policy=ssl_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alpn_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_action: Union[List[DefaultAction], core.ArrayOut[DefaultAction]] = core.arg()

        load_balancer_arn: Union[str, core.StringOut] = core.arg()

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
