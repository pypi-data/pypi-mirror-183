from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        kms_key_arn: Union[str, core.StringOut],
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

        kms_key_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Attribute(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    attribute_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        attribute_name: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
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

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class GlobalSecondaryIndex(core.Schema):

    hash_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    non_key_attributes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    projection_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    range_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    read_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    write_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        hash_key: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        non_key_attributes: Union[List[str], core.ArrayOut[core.StringOut]],
        projection_type: Union[str, core.StringOut],
        range_key: Union[str, core.StringOut],
        read_capacity: Union[int, core.IntOut],
        write_capacity: Union[int, core.IntOut],
    ):
        super().__init__(
            args=GlobalSecondaryIndex.Args(
                hash_key=hash_key,
                name=name,
                non_key_attributes=non_key_attributes,
                projection_type=projection_type,
                range_key=range_key,
                read_capacity=read_capacity,
                write_capacity=write_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hash_key: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        non_key_attributes: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        projection_type: Union[str, core.StringOut] = core.arg()

        range_key: Union[str, core.StringOut] = core.arg()

        read_capacity: Union[int, core.IntOut] = core.arg()

        write_capacity: Union[int, core.IntOut] = core.arg()


@core.schema
class Replica(core.Schema):

    kms_key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    region_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        kms_key_arn: Union[str, core.StringOut],
        region_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Replica.Args(
                kms_key_arn=kms_key_arn,
                region_name=region_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_arn: Union[str, core.StringOut] = core.arg()

        region_name: Union[str, core.StringOut] = core.arg()


@core.schema
class LocalSecondaryIndex(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    non_key_attributes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    projection_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    range_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        non_key_attributes: Union[List[str], core.ArrayOut[core.StringOut]],
        projection_type: Union[str, core.StringOut],
        range_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LocalSecondaryIndex.Args(
                name=name,
                non_key_attributes=non_key_attributes,
                projection_type=projection_type,
                range_key=range_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        non_key_attributes: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        projection_type: Union[str, core.StringOut] = core.arg()

        range_key: Union[str, core.StringOut] = core.arg()


@core.schema
class PointInTimeRecovery(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

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


@core.data(type="aws_dynamodb_table", namespace="aws_dynamodb")
class DsTable(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attribute: Union[List[Attribute], core.ArrayOut[Attribute]] = core.attr(
        Attribute, computed=True, kind=core.Kind.array
    )

    billing_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_secondary_index: Union[
        List[GlobalSecondaryIndex], core.ArrayOut[GlobalSecondaryIndex]
    ] = core.attr(GlobalSecondaryIndex, computed=True, kind=core.Kind.array)

    hash_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_secondary_index: Union[
        List[LocalSecondaryIndex], core.ArrayOut[LocalSecondaryIndex]
    ] = core.attr(LocalSecondaryIndex, computed=True, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    point_in_time_recovery: Union[
        List[PointInTimeRecovery], core.ArrayOut[PointInTimeRecovery]
    ] = core.attr(PointInTimeRecovery, computed=True, kind=core.Kind.array)

    range_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    read_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    replica: Union[List[Replica], core.ArrayOut[Replica]] = core.attr(
        Replica, computed=True, kind=core.Kind.array
    )

    server_side_encryption: Optional[ServerSideEncryption] = core.attr(
        ServerSideEncryption, default=None, computed=True
    )

    stream_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    stream_label: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_view_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    table_class: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    ttl: Union[List[Ttl], core.ArrayOut[Ttl]] = core.attr(Ttl, computed=True, kind=core.Kind.array)

    write_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        server_side_encryption: Optional[ServerSideEncryption] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTable.Args(
                name=name,
                server_side_encryption=server_side_encryption,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        server_side_encryption: Optional[ServerSideEncryption] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
