from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ApiKey(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ApiKey.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Basic(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Basic.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class Body(core.Schema):

    is_value_secret: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        is_value_secret: Optional[Union[bool, core.BoolOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Body.Args(
                is_value_secret=is_value_secret,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        is_value_secret: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Header(core.Schema):

    is_value_secret: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        is_value_secret: Optional[Union[bool, core.BoolOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Header.Args(
                is_value_secret=is_value_secret,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        is_value_secret: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class QueryString(core.Schema):

    is_value_secret: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        is_value_secret: Optional[Union[bool, core.BoolOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=QueryString.Args(
                is_value_secret=is_value_secret,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        is_value_secret: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OauthHttpParameters(core.Schema):

    body: Optional[Union[List[Body], core.ArrayOut[Body]]] = core.attr(
        Body, default=None, kind=core.Kind.array
    )

    header: Optional[Union[List[Header], core.ArrayOut[Header]]] = core.attr(
        Header, default=None, kind=core.Kind.array
    )

    query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = core.attr(
        QueryString, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        body: Optional[Union[List[Body], core.ArrayOut[Body]]] = None,
        header: Optional[Union[List[Header], core.ArrayOut[Header]]] = None,
        query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = None,
    ):
        super().__init__(
            args=OauthHttpParameters.Args(
                body=body,
                header=header,
                query_string=query_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        body: Optional[Union[List[Body], core.ArrayOut[Body]]] = core.arg(default=None)

        header: Optional[Union[List[Header], core.ArrayOut[Header]]] = core.arg(default=None)

        query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = core.arg(
            default=None
        )


@core.schema
class ClientParameters(core.Schema):

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClientParameters.Args(
                client_id=client_id,
                client_secret=client_secret,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()


@core.schema
class Oauth(core.Schema):

    authorization_endpoint: Union[str, core.StringOut] = core.attr(str)

    client_parameters: Optional[ClientParameters] = core.attr(ClientParameters, default=None)

    http_method: Union[str, core.StringOut] = core.attr(str)

    oauth_http_parameters: OauthHttpParameters = core.attr(OauthHttpParameters)

    def __init__(
        self,
        *,
        authorization_endpoint: Union[str, core.StringOut],
        http_method: Union[str, core.StringOut],
        oauth_http_parameters: OauthHttpParameters,
        client_parameters: Optional[ClientParameters] = None,
    ):
        super().__init__(
            args=Oauth.Args(
                authorization_endpoint=authorization_endpoint,
                http_method=http_method,
                oauth_http_parameters=oauth_http_parameters,
                client_parameters=client_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_endpoint: Union[str, core.StringOut] = core.arg()

        client_parameters: Optional[ClientParameters] = core.arg(default=None)

        http_method: Union[str, core.StringOut] = core.arg()

        oauth_http_parameters: OauthHttpParameters = core.arg()


@core.schema
class InvocationHttpParameters(core.Schema):

    body: Optional[Union[List[Body], core.ArrayOut[Body]]] = core.attr(
        Body, default=None, kind=core.Kind.array
    )

    header: Optional[Union[List[Header], core.ArrayOut[Header]]] = core.attr(
        Header, default=None, kind=core.Kind.array
    )

    query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = core.attr(
        QueryString, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        body: Optional[Union[List[Body], core.ArrayOut[Body]]] = None,
        header: Optional[Union[List[Header], core.ArrayOut[Header]]] = None,
        query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = None,
    ):
        super().__init__(
            args=InvocationHttpParameters.Args(
                body=body,
                header=header,
                query_string=query_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        body: Optional[Union[List[Body], core.ArrayOut[Body]]] = core.arg(default=None)

        header: Optional[Union[List[Header], core.ArrayOut[Header]]] = core.arg(default=None)

        query_string: Optional[Union[List[QueryString], core.ArrayOut[QueryString]]] = core.arg(
            default=None
        )


@core.schema
class AuthParameters(core.Schema):

    api_key: Optional[ApiKey] = core.attr(ApiKey, default=None)

    basic: Optional[Basic] = core.attr(Basic, default=None)

    invocation_http_parameters: Optional[InvocationHttpParameters] = core.attr(
        InvocationHttpParameters, default=None
    )

    oauth: Optional[Oauth] = core.attr(Oauth, default=None)

    def __init__(
        self,
        *,
        api_key: Optional[ApiKey] = None,
        basic: Optional[Basic] = None,
        invocation_http_parameters: Optional[InvocationHttpParameters] = None,
        oauth: Optional[Oauth] = None,
    ):
        super().__init__(
            args=AuthParameters.Args(
                api_key=api_key,
                basic=basic,
                invocation_http_parameters=invocation_http_parameters,
                oauth=oauth,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: Optional[ApiKey] = core.arg(default=None)

        basic: Optional[Basic] = core.arg(default=None)

        invocation_http_parameters: Optional[InvocationHttpParameters] = core.arg(default=None)

        oauth: Optional[Oauth] = core.arg(default=None)


@core.resource(type="aws_cloudwatch_event_connection", namespace="aws_eventbridge")
class CloudwatchEventConnection(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auth_parameters: AuthParameters = core.attr(AuthParameters)

    authorization_type: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    secret_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_parameters: AuthParameters,
        authorization_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventConnection.Args(
                auth_parameters=auth_parameters,
                authorization_type=authorization_type,
                name=name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_parameters: AuthParameters = core.arg()

        authorization_type: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
