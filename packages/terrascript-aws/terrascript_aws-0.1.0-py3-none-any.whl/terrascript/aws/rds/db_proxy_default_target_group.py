from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ConnectionPoolConfig(core.Schema):

    connection_borrow_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    init_query: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_connections_percent: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_idle_connections_percent: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    session_pinning_filters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        connection_borrow_timeout: Optional[Union[int, core.IntOut]] = None,
        init_query: Optional[Union[str, core.StringOut]] = None,
        max_connections_percent: Optional[Union[int, core.IntOut]] = None,
        max_idle_connections_percent: Optional[Union[int, core.IntOut]] = None,
        session_pinning_filters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=ConnectionPoolConfig.Args(
                connection_borrow_timeout=connection_borrow_timeout,
                init_query=init_query,
                max_connections_percent=max_connections_percent,
                max_idle_connections_percent=max_idle_connections_percent,
                session_pinning_filters=session_pinning_filters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_borrow_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        init_query: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_connections_percent: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_idle_connections_percent: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        session_pinning_filters: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.resource(type="aws_db_proxy_default_target_group", namespace="aws_rds")
class DbProxyDefaultTargetGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_pool_config: Optional[ConnectionPoolConfig] = core.attr(
        ConnectionPoolConfig, default=None, computed=True
    )

    db_proxy_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_proxy_name: Union[str, core.StringOut],
        connection_pool_config: Optional[ConnectionPoolConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxyDefaultTargetGroup.Args(
                db_proxy_name=db_proxy_name,
                connection_pool_config=connection_pool_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_pool_config: Optional[ConnectionPoolConfig] = core.arg(default=None)

        db_proxy_name: Union[str, core.StringOut] = core.arg()
