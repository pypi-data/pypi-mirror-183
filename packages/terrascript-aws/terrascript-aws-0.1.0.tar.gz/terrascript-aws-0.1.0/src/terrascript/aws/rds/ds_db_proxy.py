from typing import List, Union

import terrascript.core as core


@core.schema
class Auth(core.Schema):

    auth_scheme: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_auth: Union[str, core.StringOut] = core.attr(str, computed=True)

    secret_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    username: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        auth_scheme: Union[str, core.StringOut],
        description: Union[str, core.StringOut],
        iam_auth: Union[str, core.StringOut],
        secret_arn: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Auth.Args(
                auth_scheme=auth_scheme,
                description=description,
                iam_auth=iam_auth,
                secret_arn=secret_arn,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_scheme: Union[str, core.StringOut] = core.arg()

        description: Union[str, core.StringOut] = core.arg()

        iam_auth: Union[str, core.StringOut] = core.arg()

        secret_arn: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_db_proxy", namespace="aws_rds")
class DsDbProxy(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auth: Union[List[Auth], core.ArrayOut[Auth]] = core.attr(
        Auth, computed=True, kind=core.Kind.array
    )

    debug_logging: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_family: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_client_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    require_tls: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsDbProxy.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
