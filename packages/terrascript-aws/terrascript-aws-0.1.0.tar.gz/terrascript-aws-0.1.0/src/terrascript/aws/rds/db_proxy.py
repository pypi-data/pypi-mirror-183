from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Auth(core.Schema):

    auth_scheme: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_auth: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secret_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auth_scheme: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        iam_auth: Optional[Union[str, core.StringOut]] = None,
        secret_arn: Optional[Union[str, core.StringOut]] = None,
        username: Optional[Union[str, core.StringOut]] = None,
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
        auth_scheme: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_auth: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        secret_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        username: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_db_proxy", namespace="aws_rds")
class DbProxy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auth: Union[List[Auth], core.ArrayOut[Auth]] = core.attr(Auth, kind=core.Kind.array)

    debug_logging: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_family: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_client_timeout: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    name: Union[str, core.StringOut] = core.attr(str)

    require_tls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        auth: Union[List[Auth], core.ArrayOut[Auth]],
        engine_family: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        debug_logging: Optional[Union[bool, core.BoolOut]] = None,
        idle_client_timeout: Optional[Union[int, core.IntOut]] = None,
        require_tls: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxy.Args(
                auth=auth,
                engine_family=engine_family,
                name=name,
                role_arn=role_arn,
                vpc_subnet_ids=vpc_subnet_ids,
                debug_logging=debug_logging,
                idle_client_timeout=idle_client_timeout,
                require_tls=require_tls,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth: Union[List[Auth], core.ArrayOut[Auth]] = core.arg()

        debug_logging: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        engine_family: Union[str, core.StringOut] = core.arg()

        idle_client_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        require_tls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        vpc_subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()
