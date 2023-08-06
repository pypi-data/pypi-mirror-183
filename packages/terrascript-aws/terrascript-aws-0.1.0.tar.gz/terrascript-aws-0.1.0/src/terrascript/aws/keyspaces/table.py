from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionSpecification(core.Schema):

    kms_key_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        kms_key_identifier: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EncryptionSpecification.Args(
                kms_key_identifier=kms_key_identifier,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ClusteringKey(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    order_by: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        order_by: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClusteringKey.Args(
                name=name,
                order_by=order_by,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        order_by: Union[str, core.StringOut] = core.arg()


@core.schema
class Column(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Column.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class PartitionKey(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PartitionKey.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class StaticColumn(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StaticColumn.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SchemaDefinition(core.Schema):

    clustering_key: Optional[Union[List[ClusteringKey], core.ArrayOut[ClusteringKey]]] = core.attr(
        ClusteringKey, default=None, kind=core.Kind.array
    )

    column: Union[List[Column], core.ArrayOut[Column]] = core.attr(Column, kind=core.Kind.array)

    partition_key: Union[List[PartitionKey], core.ArrayOut[PartitionKey]] = core.attr(
        PartitionKey, kind=core.Kind.array
    )

    static_column: Optional[Union[List[StaticColumn], core.ArrayOut[StaticColumn]]] = core.attr(
        StaticColumn, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        column: Union[List[Column], core.ArrayOut[Column]],
        partition_key: Union[List[PartitionKey], core.ArrayOut[PartitionKey]],
        clustering_key: Optional[Union[List[ClusteringKey], core.ArrayOut[ClusteringKey]]] = None,
        static_column: Optional[Union[List[StaticColumn], core.ArrayOut[StaticColumn]]] = None,
    ):
        super().__init__(
            args=SchemaDefinition.Args(
                column=column,
                partition_key=partition_key,
                clustering_key=clustering_key,
                static_column=static_column,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        clustering_key: Optional[
            Union[List[ClusteringKey], core.ArrayOut[ClusteringKey]]
        ] = core.arg(default=None)

        column: Union[List[Column], core.ArrayOut[Column]] = core.arg()

        partition_key: Union[List[PartitionKey], core.ArrayOut[PartitionKey]] = core.arg()

        static_column: Optional[Union[List[StaticColumn], core.ArrayOut[StaticColumn]]] = core.arg(
            default=None
        )


@core.schema
class Comment(core.Schema):

    message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        message: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Comment.Args(
                message=message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PointInTimeRecovery(core.Schema):

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PointInTimeRecovery.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CapacitySpecification(core.Schema):

    read_capacity_units: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    throughput_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    write_capacity_units: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        read_capacity_units: Optional[Union[int, core.IntOut]] = None,
        throughput_mode: Optional[Union[str, core.StringOut]] = None,
        write_capacity_units: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CapacitySpecification.Args(
                read_capacity_units=read_capacity_units,
                throughput_mode=throughput_mode,
                write_capacity_units=write_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        read_capacity_units: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        throughput_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        write_capacity_units: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Ttl(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Ttl.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_keyspaces_table", namespace="aws_keyspaces")
class Table(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity_specification: Optional[CapacitySpecification] = core.attr(
        CapacitySpecification, default=None, computed=True
    )

    comment: Optional[Comment] = core.attr(Comment, default=None, computed=True)

    default_time_to_live: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    encryption_specification: Optional[EncryptionSpecification] = core.attr(
        EncryptionSpecification, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    keyspace_name: Union[str, core.StringOut] = core.attr(str)

    point_in_time_recovery: Optional[PointInTimeRecovery] = core.attr(
        PointInTimeRecovery, default=None, computed=True
    )

    schema_definition: SchemaDefinition = core.attr(SchemaDefinition)

    table_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    ttl: Optional[Ttl] = core.attr(Ttl, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        keyspace_name: Union[str, core.StringOut],
        schema_definition: SchemaDefinition,
        table_name: Union[str, core.StringOut],
        capacity_specification: Optional[CapacitySpecification] = None,
        comment: Optional[Comment] = None,
        default_time_to_live: Optional[Union[int, core.IntOut]] = None,
        encryption_specification: Optional[EncryptionSpecification] = None,
        point_in_time_recovery: Optional[PointInTimeRecovery] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        ttl: Optional[Ttl] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Table.Args(
                keyspace_name=keyspace_name,
                schema_definition=schema_definition,
                table_name=table_name,
                capacity_specification=capacity_specification,
                comment=comment,
                default_time_to_live=default_time_to_live,
                encryption_specification=encryption_specification,
                point_in_time_recovery=point_in_time_recovery,
                tags=tags,
                tags_all=tags_all,
                ttl=ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_specification: Optional[CapacitySpecification] = core.arg(default=None)

        comment: Optional[Comment] = core.arg(default=None)

        default_time_to_live: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        encryption_specification: Optional[EncryptionSpecification] = core.arg(default=None)

        keyspace_name: Union[str, core.StringOut] = core.arg()

        point_in_time_recovery: Optional[PointInTimeRecovery] = core.arg(default=None)

        schema_definition: SchemaDefinition = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        ttl: Optional[Ttl] = core.arg(default=None)
