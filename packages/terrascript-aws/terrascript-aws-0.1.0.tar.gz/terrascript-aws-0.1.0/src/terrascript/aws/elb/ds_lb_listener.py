from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AuthenticateCognito(core.Schema):

    authentication_request_extra_params: Union[
        Dict[str, str], core.MapOut[core.StringOut]
    ] = core.attr(str, computed=True, kind=core.Kind.map)

    on_unauthenticated_request: Union[str, core.StringOut] = core.attr(str, computed=True)

    scope: Union[str, core.StringOut] = core.attr(str, computed=True)

    session_cookie_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    session_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    user_pool_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_pool_client_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_pool_domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        authentication_request_extra_params: Union[Dict[str, str], core.MapOut[core.StringOut]],
        on_unauthenticated_request: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
        session_cookie_name: Union[str, core.StringOut],
        session_timeout: Union[int, core.IntOut],
        user_pool_arn: Union[str, core.StringOut],
        user_pool_client_id: Union[str, core.StringOut],
        user_pool_domain: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AuthenticateCognito.Args(
                authentication_request_extra_params=authentication_request_extra_params,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
                user_pool_arn=user_pool_arn,
                user_pool_client_id=user_pool_client_id,
                user_pool_domain=user_pool_domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: Union[
            Dict[str, str], core.MapOut[core.StringOut]
        ] = core.arg()

        on_unauthenticated_request: Union[str, core.StringOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()

        session_cookie_name: Union[str, core.StringOut] = core.arg()

        session_timeout: Union[int, core.IntOut] = core.arg()

        user_pool_arn: Union[str, core.StringOut] = core.arg()

        user_pool_client_id: Union[str, core.StringOut] = core.arg()

        user_pool_domain: Union[str, core.StringOut] = core.arg()


@core.schema
class AuthenticateOidc(core.Schema):

    authentication_request_extra_params: Union[
        Dict[str, str], core.MapOut[core.StringOut]
    ] = core.attr(str, computed=True, kind=core.Kind.map)

    authorization_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    client_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    client_secret: Union[str, core.StringOut] = core.attr(str, computed=True)

    issuer: Union[str, core.StringOut] = core.attr(str, computed=True)

    on_unauthenticated_request: Union[str, core.StringOut] = core.attr(str, computed=True)

    scope: Union[str, core.StringOut] = core.attr(str, computed=True)

    session_cookie_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    session_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    token_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_info_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        authentication_request_extra_params: Union[Dict[str, str], core.MapOut[core.StringOut]],
        authorization_endpoint: Union[str, core.StringOut],
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        issuer: Union[str, core.StringOut],
        on_unauthenticated_request: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
        session_cookie_name: Union[str, core.StringOut],
        session_timeout: Union[int, core.IntOut],
        token_endpoint: Union[str, core.StringOut],
        user_info_endpoint: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AuthenticateOidc.Args(
                authentication_request_extra_params=authentication_request_extra_params,
                authorization_endpoint=authorization_endpoint,
                client_id=client_id,
                client_secret=client_secret,
                issuer=issuer,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
                token_endpoint=token_endpoint,
                user_info_endpoint=user_info_endpoint,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: Union[
            Dict[str, str], core.MapOut[core.StringOut]
        ] = core.arg()

        authorization_endpoint: Union[str, core.StringOut] = core.arg()

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        issuer: Union[str, core.StringOut] = core.arg()

        on_unauthenticated_request: Union[str, core.StringOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()

        session_cookie_name: Union[str, core.StringOut] = core.arg()

        session_timeout: Union[int, core.IntOut] = core.arg()

        token_endpoint: Union[str, core.StringOut] = core.arg()

        user_info_endpoint: Union[str, core.StringOut] = core.arg()


@core.schema
class FixedResponse(core.Schema):

    content_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    message_body: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        content_type: Union[str, core.StringOut],
        message_body: Union[str, core.StringOut],
        status_code: Union[str, core.StringOut],
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

        message_body: Union[str, core.StringOut] = core.arg()

        status_code: Union[str, core.StringOut] = core.arg()


@core.schema
class TargetGroup(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    weight: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        weight: Union[int, core.IntOut],
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

        weight: Union[int, core.IntOut] = core.arg()


@core.schema
class Stickiness(core.Schema):

    duration: Union[int, core.IntOut] = core.attr(int, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        duration: Union[int, core.IntOut],
        enabled: Union[bool, core.BoolOut],
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

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Forward(core.Schema):

    stickiness: Union[List[Stickiness], core.ArrayOut[Stickiness]] = core.attr(
        Stickiness, computed=True, kind=core.Kind.array
    )

    target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]] = core.attr(
        TargetGroup, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        stickiness: Union[List[Stickiness], core.ArrayOut[Stickiness]],
        target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]],
    ):
        super().__init__(
            args=Forward.Args(
                stickiness=stickiness,
                target_group=target_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stickiness: Union[List[Stickiness], core.ArrayOut[Stickiness]] = core.arg()

        target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]] = core.arg()


@core.schema
class Redirect(core.Schema):

    host: Union[str, core.StringOut] = core.attr(str, computed=True)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    query: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        host: Union[str, core.StringOut],
        path: Union[str, core.StringOut],
        port: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        query: Union[str, core.StringOut],
        status_code: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Redirect.Args(
                host=host,
                path=path,
                port=port,
                protocol=protocol,
                query=query,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: Union[str, core.StringOut] = core.arg()

        path: Union[str, core.StringOut] = core.arg()

        port: Union[str, core.StringOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        query: Union[str, core.StringOut] = core.arg()

        status_code: Union[str, core.StringOut] = core.arg()


@core.schema
class DefaultAction(core.Schema):

    authenticate_cognito: Union[
        List[AuthenticateCognito], core.ArrayOut[AuthenticateCognito]
    ] = core.attr(AuthenticateCognito, computed=True, kind=core.Kind.array)

    authenticate_oidc: Union[List[AuthenticateOidc], core.ArrayOut[AuthenticateOidc]] = core.attr(
        AuthenticateOidc, computed=True, kind=core.Kind.array
    )

    fixed_response: Union[List[FixedResponse], core.ArrayOut[FixedResponse]] = core.attr(
        FixedResponse, computed=True, kind=core.Kind.array
    )

    forward: Union[List[Forward], core.ArrayOut[Forward]] = core.attr(
        Forward, computed=True, kind=core.Kind.array
    )

    order: Union[int, core.IntOut] = core.attr(int, computed=True)

    redirect: Union[List[Redirect], core.ArrayOut[Redirect]] = core.attr(
        Redirect, computed=True, kind=core.Kind.array
    )

    target_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        authenticate_cognito: Union[List[AuthenticateCognito], core.ArrayOut[AuthenticateCognito]],
        authenticate_oidc: Union[List[AuthenticateOidc], core.ArrayOut[AuthenticateOidc]],
        fixed_response: Union[List[FixedResponse], core.ArrayOut[FixedResponse]],
        forward: Union[List[Forward], core.ArrayOut[Forward]],
        order: Union[int, core.IntOut],
        redirect: Union[List[Redirect], core.ArrayOut[Redirect]],
        target_group_arn: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DefaultAction.Args(
                authenticate_cognito=authenticate_cognito,
                authenticate_oidc=authenticate_oidc,
                fixed_response=fixed_response,
                forward=forward,
                order=order,
                redirect=redirect,
                target_group_arn=target_group_arn,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authenticate_cognito: Union[
            List[AuthenticateCognito], core.ArrayOut[AuthenticateCognito]
        ] = core.arg()

        authenticate_oidc: Union[
            List[AuthenticateOidc], core.ArrayOut[AuthenticateOidc]
        ] = core.arg()

        fixed_response: Union[List[FixedResponse], core.ArrayOut[FixedResponse]] = core.arg()

        forward: Union[List[Forward], core.ArrayOut[Forward]] = core.arg()

        order: Union[int, core.IntOut] = core.arg()

        redirect: Union[List[Redirect], core.ArrayOut[Redirect]] = core.arg()

        target_group_arn: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_lb_listener", namespace="aws_elb")
class DsLbListener(core.Data):

    alpn_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    certificate_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_action: Union[List[DefaultAction], core.ArrayOut[DefaultAction]] = core.attr(
        DefaultAction, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    ssl_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        load_balancer_arn: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLbListener.Args(
                arn=arn,
                load_balancer_arn=load_balancer_arn,
                port=port,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        load_balancer_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
