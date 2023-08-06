from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClusterConfiguration(core.Schema):

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    maintenance_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    num_shards: Union[int, core.IntOut] = core.attr(int, computed=True)

    parameter_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_retention_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    topic_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        description: Union[str, core.StringOut],
        engine_version: Union[str, core.StringOut],
        maintenance_window: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        node_type: Union[str, core.StringOut],
        num_shards: Union[int, core.IntOut],
        parameter_group_name: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
        snapshot_retention_limit: Union[int, core.IntOut],
        snapshot_window: Union[str, core.StringOut],
        subnet_group_name: Union[str, core.StringOut],
        topic_arn: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClusterConfiguration.Args(
                description=description,
                engine_version=engine_version,
                maintenance_window=maintenance_window,
                name=name,
                node_type=node_type,
                num_shards=num_shards,
                parameter_group_name=parameter_group_name,
                port=port,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                subnet_group_name=subnet_group_name,
                topic_arn=topic_arn,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Union[str, core.StringOut] = core.arg()

        engine_version: Union[str, core.StringOut] = core.arg()

        maintenance_window: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        node_type: Union[str, core.StringOut] = core.arg()

        num_shards: Union[int, core.IntOut] = core.arg()

        parameter_group_name: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()

        snapshot_retention_limit: Union[int, core.IntOut] = core.arg()

        snapshot_window: Union[str, core.StringOut] = core.arg()

        subnet_group_name: Union[str, core.StringOut] = core.arg()

        topic_arn: Union[str, core.StringOut] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_memorydb_snapshot", namespace="aws_memorydb")
class DsSnapshot(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_configuration: Union[
        List[ClusterConfiguration], core.ArrayOut[ClusterConfiguration]
    ] = core.attr(ClusterConfiguration, computed=True, kind=core.Kind.array)

    cluster_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    source: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSnapshot.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
