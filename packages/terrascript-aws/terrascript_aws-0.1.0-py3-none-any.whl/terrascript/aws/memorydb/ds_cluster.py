from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClusterEndpoint(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ClusterEndpoint.Args(
                address=address,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Endpoint(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Endpoint.Args(
                address=address,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Nodes(core.Schema):

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint: Union[List[Endpoint], core.ArrayOut[Endpoint]] = core.attr(
        Endpoint, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zone: Union[str, core.StringOut],
        create_time: Union[str, core.StringOut],
        endpoint: Union[List[Endpoint], core.ArrayOut[Endpoint]],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Nodes.Args(
                availability_zone=availability_zone,
                create_time=create_time,
                endpoint=endpoint,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Union[str, core.StringOut] = core.arg()

        create_time: Union[str, core.StringOut] = core.arg()

        endpoint: Union[List[Endpoint], core.ArrayOut[Endpoint]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Shards(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    nodes: Union[List[Nodes], core.ArrayOut[Nodes]] = core.attr(
        Nodes, computed=True, kind=core.Kind.array
    )

    num_nodes: Union[int, core.IntOut] = core.attr(int, computed=True)

    slots: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        nodes: Union[List[Nodes], core.ArrayOut[Nodes]],
        num_nodes: Union[int, core.IntOut],
        slots: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Shards.Args(
                name=name,
                nodes=nodes,
                num_nodes=num_nodes,
                slots=slots,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        nodes: Union[List[Nodes], core.ArrayOut[Nodes]] = core.arg()

        num_nodes: Union[int, core.IntOut] = core.arg()

        slots: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_memorydb_cluster", namespace="aws_memorydb")
class DsCluster(core.Data):

    acl_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    cluster_endpoint: Union[List[ClusterEndpoint], core.ArrayOut[ClusterEndpoint]] = core.attr(
        ClusterEndpoint, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_patch_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    maintenance_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    num_replicas_per_shard: Union[int, core.IntOut] = core.attr(int, computed=True)

    num_shards: Union[int, core.IntOut] = core.attr(int, computed=True)

    parameter_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    shards: Union[List[Shards], core.ArrayOut[Shards]] = core.attr(
        Shards, computed=True, kind=core.Kind.array
    )

    snapshot_retention_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    sns_topic_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tls_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
