from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_elasticache_global_replication_group", namespace="aws_elasticache")
class GlobalReplicationGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    at_rest_encryption_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    auth_token_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    cache_node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version_actual: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_replication_group_description: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    global_replication_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_replication_group_id_suffix: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    primary_replication_group_id: Union[str, core.StringOut] = core.attr(str)

    transit_encryption_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        global_replication_group_id_suffix: Union[str, core.StringOut],
        primary_replication_group_id: Union[str, core.StringOut],
        engine_version: Optional[Union[str, core.StringOut]] = None,
        global_replication_group_description: Optional[Union[str, core.StringOut]] = None,
        parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalReplicationGroup.Args(
                global_replication_group_id_suffix=global_replication_group_id_suffix,
                primary_replication_group_id=primary_replication_group_id,
                engine_version=engine_version,
                global_replication_group_description=global_replication_group_description,
                parameter_group_name=parameter_group_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_replication_group_description: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        global_replication_group_id_suffix: Union[str, core.StringOut] = core.arg()

        parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        primary_replication_group_id: Union[str, core.StringOut] = core.arg()
