from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Cors(core.Schema):

    allow_credentials: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    allow_headers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allow_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allow_origins: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    expose_headers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_age: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        allow_credentials: Union[bool, core.BoolOut],
        allow_headers: Union[List[str], core.ArrayOut[core.StringOut]],
        allow_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        allow_origins: Union[List[str], core.ArrayOut[core.StringOut]],
        expose_headers: Union[List[str], core.ArrayOut[core.StringOut]],
        max_age: Union[int, core.IntOut],
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
        allow_credentials: Union[bool, core.BoolOut] = core.arg()

        allow_headers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        allow_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        allow_origins: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        expose_headers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        max_age: Union[int, core.IntOut] = core.arg()


@core.data(type="aws_lambda_function_url", namespace="aws_lambda")
class DsFunctionUrl(core.Data):

    authorization_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    cors: Union[List[Cors], core.ArrayOut[Cors]] = core.attr(
        Cors, computed=True, kind=core.Kind.array
    )

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    function_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    function_name: Union[str, core.StringOut] = core.attr(str)

    function_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    url_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        function_name: Union[str, core.StringOut],
        qualifier: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFunctionUrl.Args(
                function_name=function_name,
                qualifier=qualifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: Union[str, core.StringOut] = core.arg()

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)
