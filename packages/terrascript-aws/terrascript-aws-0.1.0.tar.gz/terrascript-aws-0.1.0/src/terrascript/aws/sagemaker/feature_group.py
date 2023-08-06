from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DataCatalogConfig(core.Schema):

    catalog: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    database: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    table_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        catalog: Optional[Union[str, core.StringOut]] = None,
        database: Optional[Union[str, core.StringOut]] = None,
        table_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DataCatalogConfig.Args(
                catalog=catalog,
                database=database,
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        table_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3StorageConfig(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_uri: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_uri: Union[str, core.StringOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3StorageConfig.Args(
                s3_uri=s3_uri,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_uri: Union[str, core.StringOut] = core.arg()


@core.schema
class OfflineStoreConfig(core.Schema):

    data_catalog_config: Optional[DataCatalogConfig] = core.attr(
        DataCatalogConfig, default=None, computed=True
    )

    disable_glue_table_creation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    s3_storage_config: S3StorageConfig = core.attr(S3StorageConfig)

    def __init__(
        self,
        *,
        s3_storage_config: S3StorageConfig,
        data_catalog_config: Optional[DataCatalogConfig] = None,
        disable_glue_table_creation: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=OfflineStoreConfig.Args(
                s3_storage_config=s3_storage_config,
                data_catalog_config=data_catalog_config,
                disable_glue_table_creation=disable_glue_table_creation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_catalog_config: Optional[DataCatalogConfig] = core.arg(default=None)

        disable_glue_table_creation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        s3_storage_config: S3StorageConfig = core.arg()


@core.schema
class SecurityConfig(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SecurityConfig.Args(
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OnlineStoreConfig(core.Schema):

    enable_online_store: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_config: Optional[SecurityConfig] = core.attr(SecurityConfig, default=None)

    def __init__(
        self,
        *,
        enable_online_store: Optional[Union[bool, core.BoolOut]] = None,
        security_config: Optional[SecurityConfig] = None,
    ):
        super().__init__(
            args=OnlineStoreConfig.Args(
                enable_online_store=enable_online_store,
                security_config=security_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_online_store: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_config: Optional[SecurityConfig] = core.arg(default=None)


@core.schema
class FeatureDefinition(core.Schema):

    feature_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    feature_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        feature_name: Optional[Union[str, core.StringOut]] = None,
        feature_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FeatureDefinition.Args(
                feature_name=feature_name,
                feature_type=feature_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        feature_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        feature_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sagemaker_feature_group", namespace="aws_sagemaker")
class FeatureGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_time_feature_name: Union[str, core.StringOut] = core.attr(str)

    feature_definition: Union[
        List[FeatureDefinition], core.ArrayOut[FeatureDefinition]
    ] = core.attr(FeatureDefinition, kind=core.Kind.array)

    feature_group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    offline_store_config: Optional[OfflineStoreConfig] = core.attr(OfflineStoreConfig, default=None)

    online_store_config: Optional[OnlineStoreConfig] = core.attr(OnlineStoreConfig, default=None)

    record_identifier_feature_name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

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
        event_time_feature_name: Union[str, core.StringOut],
        feature_definition: Union[List[FeatureDefinition], core.ArrayOut[FeatureDefinition]],
        feature_group_name: Union[str, core.StringOut],
        record_identifier_feature_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        offline_store_config: Optional[OfflineStoreConfig] = None,
        online_store_config: Optional[OnlineStoreConfig] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FeatureGroup.Args(
                event_time_feature_name=event_time_feature_name,
                feature_definition=feature_definition,
                feature_group_name=feature_group_name,
                record_identifier_feature_name=record_identifier_feature_name,
                role_arn=role_arn,
                description=description,
                offline_store_config=offline_store_config,
                online_store_config=online_store_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        event_time_feature_name: Union[str, core.StringOut] = core.arg()

        feature_definition: Union[
            List[FeatureDefinition], core.ArrayOut[FeatureDefinition]
        ] = core.arg()

        feature_group_name: Union[str, core.StringOut] = core.arg()

        offline_store_config: Optional[OfflineStoreConfig] = core.arg(default=None)

        online_store_config: Optional[OnlineStoreConfig] = core.arg(default=None)

        record_identifier_feature_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
