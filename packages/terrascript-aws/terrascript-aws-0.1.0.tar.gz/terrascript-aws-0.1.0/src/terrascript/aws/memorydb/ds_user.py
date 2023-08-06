from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AuthenticationMode(core.Schema):

    password_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        password_count: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AuthenticationMode.Args(
                password_count=password_count,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password_count: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_memorydb_user", namespace="aws_memorydb")
class DsUser(core.Data):

    access_string: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_mode: Union[
        List[AuthenticationMode], core.ArrayOut[AuthenticationMode]
    ] = core.attr(AuthenticationMode, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    minimum_engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        user_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                user_name=user_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        user_name: Union[str, core.StringOut] = core.arg()
