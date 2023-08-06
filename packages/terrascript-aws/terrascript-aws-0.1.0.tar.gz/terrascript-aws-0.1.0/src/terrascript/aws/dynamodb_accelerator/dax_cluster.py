from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Nodes(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        availability_zone: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Nodes.Args(
                address=address,
                availability_zone=availability_zone,
                id=id,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        availability_zone: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ServerSideEncryption.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_dax_cluster", namespace="aws_dynamodb_accelerator")
class DaxCluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cluster_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_endpoint_encryption_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    configuration_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_role_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    node_type: Union[str, core.StringOut] = core.attr(str)

    nodes: Union[List[Nodes], core.ArrayOut[Nodes]] = core.attr(
        Nodes, computed=True, kind=core.Kind.array
    )

    notification_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    replication_factor: Union[int, core.IntOut] = core.attr(int)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    server_side_encryption: Optional[ServerSideEncryption] = core.attr(
        ServerSideEncryption, default=None
    )

    subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        iam_role_arn: Union[str, core.StringOut],
        node_type: Union[str, core.StringOut],
        replication_factor: Union[int, core.IntOut],
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        cluster_endpoint_encryption_type: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        maintenance_window: Optional[Union[str, core.StringOut]] = None,
        notification_topic_arn: Optional[Union[str, core.StringOut]] = None,
        parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        server_side_encryption: Optional[ServerSideEncryption] = None,
        subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DaxCluster.Args(
                cluster_name=cluster_name,
                iam_role_arn=iam_role_arn,
                node_type=node_type,
                replication_factor=replication_factor,
                availability_zones=availability_zones,
                cluster_endpoint_encryption_type=cluster_endpoint_encryption_type,
                description=description,
                maintenance_window=maintenance_window,
                notification_topic_arn=notification_topic_arn,
                parameter_group_name=parameter_group_name,
                security_group_ids=security_group_ids,
                server_side_encryption=server_side_encryption,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        cluster_endpoint_encryption_type: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        cluster_name: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_role_arn: Union[str, core.StringOut] = core.arg()

        maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_type: Union[str, core.StringOut] = core.arg()

        notification_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replication_factor: Union[int, core.IntOut] = core.arg()

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        server_side_encryption: Optional[ServerSideEncryption] = core.arg(default=None)

        subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
