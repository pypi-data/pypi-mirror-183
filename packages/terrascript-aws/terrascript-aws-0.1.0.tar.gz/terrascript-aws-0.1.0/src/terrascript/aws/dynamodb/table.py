from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class GlobalSecondaryIndex(core.Schema):

    hash_key: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    non_key_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    projection_type: Union[str, core.StringOut] = core.attr(str)

    range_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    read_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    write_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        hash_key: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        projection_type: Union[str, core.StringOut],
        non_key_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        range_key: Optional[Union[str, core.StringOut]] = None,
        read_capacity: Optional[Union[int, core.IntOut]] = None,
        write_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=GlobalSecondaryIndex.Args(
                hash_key=hash_key,
                name=name,
                projection_type=projection_type,
                non_key_attributes=non_key_attributes,
                range_key=range_key,
                read_capacity=read_capacity,
                write_capacity=write_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hash_key: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        non_key_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        projection_type: Union[str, core.StringOut] = core.arg()

        range_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        read_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        write_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class LocalSecondaryIndex(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    non_key_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    projection_type: Union[str, core.StringOut] = core.attr(str)

    range_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        projection_type: Union[str, core.StringOut],
        range_key: Union[str, core.StringOut],
        non_key_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=LocalSecondaryIndex.Args(
                name=name,
                projection_type=projection_type,
                range_key=range_key,
                non_key_attributes=non_key_attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        non_key_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        projection_type: Union[str, core.StringOut] = core.arg()

        range_key: Union[str, core.StringOut] = core.arg()


@core.schema
class PointInTimeRecovery(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=PointInTimeRecovery.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Attribute(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attribute.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Ttl(core.Schema):

    attribute_name: Union[str, core.StringOut] = core.attr(str)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        attribute_name: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Ttl.Args(
                attribute_name=attribute_name,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_name: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Replica(core.Schema):

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    point_in_time_recovery: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    propagate_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    region_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        region_name: Union[str, core.StringOut],
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        point_in_time_recovery: Optional[Union[bool, core.BoolOut]] = None,
        propagate_tags: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Replica.Args(
                region_name=region_name,
                kms_key_arn=kms_key_arn,
                point_in_time_recovery=point_in_time_recovery,
                propagate_tags=propagate_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        point_in_time_recovery: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        propagate_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        region_name: Union[str, core.StringOut] = core.arg()


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ServerSideEncryption.Args(
                enabled=enabled,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_dynamodb_table", namespace="aws_dynamodb")
class Table(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = core.attr(
        Attribute, default=None, computed=True, kind=core.Kind.array
    )

    billing_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_secondary_index: Optional[
        Union[List[GlobalSecondaryIndex], core.ArrayOut[GlobalSecondaryIndex]]
    ] = core.attr(GlobalSecondaryIndex, default=None, kind=core.Kind.array)

    hash_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_secondary_index: Optional[
        Union[List[LocalSecondaryIndex], core.ArrayOut[LocalSecondaryIndex]]
    ] = core.attr(LocalSecondaryIndex, default=None, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    point_in_time_recovery: Optional[PointInTimeRecovery] = core.attr(
        PointInTimeRecovery, default=None, computed=True
    )

    range_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    read_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    replica: Optional[Union[List[Replica], core.ArrayOut[Replica]]] = core.attr(
        Replica, default=None, kind=core.Kind.array
    )

    restore_date_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    restore_source_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    restore_to_latest_time: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    server_side_encryption: Optional[ServerSideEncryption] = core.attr(
        ServerSideEncryption, default=None, computed=True
    )

    stream_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    stream_label: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_view_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    table_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    ttl: Optional[Ttl] = core.attr(Ttl, default=None, computed=True)

    write_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = None,
        billing_mode: Optional[Union[str, core.StringOut]] = None,
        global_secondary_index: Optional[
            Union[List[GlobalSecondaryIndex], core.ArrayOut[GlobalSecondaryIndex]]
        ] = None,
        hash_key: Optional[Union[str, core.StringOut]] = None,
        local_secondary_index: Optional[
            Union[List[LocalSecondaryIndex], core.ArrayOut[LocalSecondaryIndex]]
        ] = None,
        point_in_time_recovery: Optional[PointInTimeRecovery] = None,
        range_key: Optional[Union[str, core.StringOut]] = None,
        read_capacity: Optional[Union[int, core.IntOut]] = None,
        replica: Optional[Union[List[Replica], core.ArrayOut[Replica]]] = None,
        restore_date_time: Optional[Union[str, core.StringOut]] = None,
        restore_source_name: Optional[Union[str, core.StringOut]] = None,
        restore_to_latest_time: Optional[Union[bool, core.BoolOut]] = None,
        server_side_encryption: Optional[ServerSideEncryption] = None,
        stream_enabled: Optional[Union[bool, core.BoolOut]] = None,
        stream_view_type: Optional[Union[str, core.StringOut]] = None,
        table_class: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        ttl: Optional[Ttl] = None,
        write_capacity: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Table.Args(
                name=name,
                attribute=attribute,
                billing_mode=billing_mode,
                global_secondary_index=global_secondary_index,
                hash_key=hash_key,
                local_secondary_index=local_secondary_index,
                point_in_time_recovery=point_in_time_recovery,
                range_key=range_key,
                read_capacity=read_capacity,
                replica=replica,
                restore_date_time=restore_date_time,
                restore_source_name=restore_source_name,
                restore_to_latest_time=restore_to_latest_time,
                server_side_encryption=server_side_encryption,
                stream_enabled=stream_enabled,
                stream_view_type=stream_view_type,
                table_class=table_class,
                tags=tags,
                tags_all=tags_all,
                ttl=ttl,
                write_capacity=write_capacity,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = core.arg(
            default=None
        )

        billing_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_secondary_index: Optional[
            Union[List[GlobalSecondaryIndex], core.ArrayOut[GlobalSecondaryIndex]]
        ] = core.arg(default=None)

        hash_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        local_secondary_index: Optional[
            Union[List[LocalSecondaryIndex], core.ArrayOut[LocalSecondaryIndex]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        point_in_time_recovery: Optional[PointInTimeRecovery] = core.arg(default=None)

        range_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        read_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        replica: Optional[Union[List[Replica], core.ArrayOut[Replica]]] = core.arg(default=None)

        restore_date_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        restore_source_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        restore_to_latest_time: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        server_side_encryption: Optional[ServerSideEncryption] = core.arg(default=None)

        stream_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        stream_view_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        table_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        ttl: Optional[Ttl] = core.arg(default=None)

        write_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)
