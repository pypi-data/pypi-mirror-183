from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AuthenticationMode(core.Schema):

    password_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    passwords: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password_count: Union[int, core.IntOut],
        passwords: Union[List[str], core.ArrayOut[core.StringOut]],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AuthenticationMode.Args(
                password_count=password_count,
                passwords=passwords,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password_count: Union[int, core.IntOut] = core.arg()

        passwords: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_memorydb_user", namespace="aws_memorydb")
class User(core.Resource):

    access_string: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_mode: AuthenticationMode = core.attr(AuthenticationMode)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    minimum_engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_string: Union[str, core.StringOut],
        authentication_mode: AuthenticationMode,
        user_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                access_string=access_string,
                authentication_mode=authentication_mode,
                user_name=user_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_string: Union[str, core.StringOut] = core.arg()

        authentication_mode: AuthenticationMode = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_name: Union[str, core.StringOut] = core.arg()
