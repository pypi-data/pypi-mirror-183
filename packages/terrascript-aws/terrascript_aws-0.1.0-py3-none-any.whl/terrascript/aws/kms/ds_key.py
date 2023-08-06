from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PrimaryKey(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PrimaryKey.Args(
                arn=arn,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        region: Union[str, core.StringOut] = core.arg()


@core.schema
class ReplicaKeys(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ReplicaKeys.Args(
                arn=arn,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        region: Union[str, core.StringOut] = core.arg()


@core.schema
class MultiRegionConfiguration(core.Schema):

    multi_region_key_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    primary_key: Union[List[PrimaryKey], core.ArrayOut[PrimaryKey]] = core.attr(
        PrimaryKey, computed=True, kind=core.Kind.array
    )

    replica_keys: Union[List[ReplicaKeys], core.ArrayOut[ReplicaKeys]] = core.attr(
        ReplicaKeys, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        multi_region_key_type: Union[str, core.StringOut],
        primary_key: Union[List[PrimaryKey], core.ArrayOut[PrimaryKey]],
        replica_keys: Union[List[ReplicaKeys], core.ArrayOut[ReplicaKeys]],
    ):
        super().__init__(
            args=MultiRegionConfiguration.Args(
                multi_region_key_type=multi_region_key_type,
                primary_key=primary_key,
                replica_keys=replica_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        multi_region_key_type: Union[str, core.StringOut] = core.arg()

        primary_key: Union[List[PrimaryKey], core.ArrayOut[PrimaryKey]] = core.arg()

        replica_keys: Union[List[ReplicaKeys], core.ArrayOut[ReplicaKeys]] = core.arg()


@core.data(type="aws_kms_key", namespace="aws_kms")
class DsKey(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_master_key_spec: Union[str, core.StringOut] = core.attr(str, computed=True)

    deletion_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    expiration_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str)

    key_manager: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_usage: Union[str, core.StringOut] = core.attr(str, computed=True)

    multi_region: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    multi_region_configuration: Union[
        List[MultiRegionConfiguration], core.ArrayOut[MultiRegionConfiguration]
    ] = core.attr(MultiRegionConfiguration, computed=True, kind=core.Kind.array)

    origin: Union[str, core.StringOut] = core.attr(str, computed=True)

    valid_to: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        key_id: Union[str, core.StringOut],
        grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsKey.Args(
                key_id=key_id,
                grant_tokens=grant_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        key_id: Union[str, core.StringOut] = core.arg()
