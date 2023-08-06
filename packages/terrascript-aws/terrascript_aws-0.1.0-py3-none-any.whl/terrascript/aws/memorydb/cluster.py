from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.resource(type="aws_memorydb_cluster", namespace="aws_memorydb")
class Cluster(core.Resource):

    acl_name: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cluster_endpoint: Union[List[ClusterEndpoint], core.ArrayOut[ClusterEndpoint]] = core.attr(
        ClusterEndpoint, computed=True, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_patch_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    final_snapshot_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    node_type: Union[str, core.StringOut] = core.attr(str)

    num_replicas_per_shard: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    num_shards: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    shards: Union[List[Shards], core.ArrayOut[Shards]] = core.attr(
        Shards, computed=True, kind=core.Kind.array
    )

    snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    snapshot_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_retention_limit: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    snapshot_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    sns_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tls_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        acl_name: Union[str, core.StringOut],
        node_type: Union[str, core.StringOut],
        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        final_snapshot_name: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        maintenance_window: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        num_replicas_per_shard: Optional[Union[int, core.IntOut]] = None,
        num_shards: Optional[Union[int, core.IntOut]] = None,
        parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        snapshot_name: Optional[Union[str, core.StringOut]] = None,
        snapshot_retention_limit: Optional[Union[int, core.IntOut]] = None,
        snapshot_window: Optional[Union[str, core.StringOut]] = None,
        sns_topic_arn: Optional[Union[str, core.StringOut]] = None,
        subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tls_enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                acl_name=acl_name,
                node_type=node_type,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                description=description,
                engine_version=engine_version,
                final_snapshot_name=final_snapshot_name,
                kms_key_arn=kms_key_arn,
                maintenance_window=maintenance_window,
                name=name,
                name_prefix=name_prefix,
                num_replicas_per_shard=num_replicas_per_shard,
                num_shards=num_shards,
                parameter_group_name=parameter_group_name,
                port=port,
                security_group_ids=security_group_ids,
                snapshot_arns=snapshot_arns,
                snapshot_name=snapshot_name,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                sns_topic_arn=sns_topic_arn,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                tls_enabled=tls_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acl_name: Union[str, core.StringOut] = core.arg()

        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_snapshot_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_type: Union[str, core.StringOut] = core.arg()

        num_replicas_per_shard: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        num_shards: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        snapshot_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_retention_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        snapshot_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sns_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tls_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
