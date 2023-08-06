from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Cors(core.Schema):

    allow_credentials: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    allow_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_methods: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_origins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_age: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allow_credentials: Optional[Union[bool, core.BoolOut]] = None,
        allow_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        allow_methods: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        allow_origins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        max_age: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Cors.Args(
                allow_credentials=allow_credentials,
                allow_headers=allow_headers,
                allow_methods=allow_methods,
                allow_origins=allow_origins,
                expose_headers=expose_headers,
                max_age=max_age,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_credentials: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        allow_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allow_methods: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allow_origins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_age: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_lambda_function_url", namespace="aws_lambda")
class FunctionUrl(core.Resource):

    authorization_type: Union[str, core.StringOut] = core.attr(str)

    cors: Optional[Cors] = core.attr(Cors, default=None)

    function_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    function_name: Union[str, core.StringOut] = core.attr(str)

    function_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    url_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        authorization_type: Union[str, core.StringOut],
        function_name: Union[str, core.StringOut],
        cors: Optional[Cors] = None,
        qualifier: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FunctionUrl.Args(
                authorization_type=authorization_type,
                function_name=function_name,
                cors=cors,
                qualifier=qualifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authorization_type: Union[str, core.StringOut] = core.arg()

        cors: Optional[Cors] = core.arg(default=None)

        function_name: Union[str, core.StringOut] = core.arg()

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)
