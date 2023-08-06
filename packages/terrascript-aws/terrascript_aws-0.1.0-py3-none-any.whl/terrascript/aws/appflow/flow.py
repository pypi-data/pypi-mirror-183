from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class IncrementalPullConfig(core.Schema):

    datetime_type_field_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        datetime_type_field_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=IncrementalPullConfig.Args(
                datetime_type_field_name=datetime_type_field_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        datetime_type_field_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3InputFormatConfig(core.Schema):

    s3_input_file_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_input_file_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3InputFormatConfig.Args(
                s3_input_file_type=s3_input_file_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_input_file_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SourceConnectorPropertiesS3(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_input_format_config: Optional[S3InputFormatConfig] = core.attr(
        S3InputFormatConfig, default=None
    )

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        s3_input_format_config: Optional[S3InputFormatConfig] = None,
    ):
        super().__init__(
            args=SourceConnectorPropertiesS3.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                s3_input_format_config=s3_input_format_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_input_format_config: Optional[S3InputFormatConfig] = core.arg(default=None)


@core.schema
class Veeva(core.Schema):

    document_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    include_all_versions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_renditions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_source_files: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        document_type: Optional[Union[str, core.StringOut]] = None,
        include_all_versions: Optional[Union[bool, core.BoolOut]] = None,
        include_renditions: Optional[Union[bool, core.BoolOut]] = None,
        include_source_files: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Veeva.Args(
                object=object,
                document_type=document_type,
                include_all_versions=include_all_versions,
                include_renditions=include_renditions,
                include_source_files=include_source_files,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        document_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        include_all_versions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_renditions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_source_files: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Amplitude(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Amplitude.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Datadog(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Datadog.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceConnectorPropertiesMarketo(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceConnectorPropertiesMarketo.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class GoogleAnalytics(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=GoogleAnalytics.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceConnectorPropertiesSalesforce(core.Schema):

    enable_dynamic_field_update: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_deleted_records: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        enable_dynamic_field_update: Optional[Union[bool, core.BoolOut]] = None,
        include_deleted_records: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=SourceConnectorPropertiesSalesforce.Args(
                object=object,
                enable_dynamic_field_update=enable_dynamic_field_update,
                include_deleted_records=include_deleted_records,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_dynamic_field_update: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_deleted_records: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Dynatrace(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Dynatrace.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class ServiceNow(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ServiceNow.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Slack(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Slack.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceConnectorPropertiesZendesk(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceConnectorPropertiesZendesk.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class InforNexus(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InforNexus.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceConnectorPropertiesSapoData(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceConnectorPropertiesSapoData.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Singular(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Singular.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Trendmicro(core.Schema):

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Trendmicro.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceConnectorPropertiesCustomConnector(core.Schema):

    custom_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    entity_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        entity_name: Union[str, core.StringOut],
        custom_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=SourceConnectorPropertiesCustomConnector.Args(
                entity_name=entity_name,
                custom_properties=custom_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        entity_name: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceConnectorProperties(core.Schema):

    amplitude: Optional[Amplitude] = core.attr(Amplitude, default=None)

    custom_connector: Optional[SourceConnectorPropertiesCustomConnector] = core.attr(
        SourceConnectorPropertiesCustomConnector, default=None
    )

    datadog: Optional[Datadog] = core.attr(Datadog, default=None)

    dynatrace: Optional[Dynatrace] = core.attr(Dynatrace, default=None)

    google_analytics: Optional[GoogleAnalytics] = core.attr(GoogleAnalytics, default=None)

    infor_nexus: Optional[InforNexus] = core.attr(InforNexus, default=None)

    marketo: Optional[SourceConnectorPropertiesMarketo] = core.attr(
        SourceConnectorPropertiesMarketo, default=None
    )

    s3: Optional[SourceConnectorPropertiesS3] = core.attr(SourceConnectorPropertiesS3, default=None)

    salesforce: Optional[SourceConnectorPropertiesSalesforce] = core.attr(
        SourceConnectorPropertiesSalesforce, default=None
    )

    sapo_data: Optional[SourceConnectorPropertiesSapoData] = core.attr(
        SourceConnectorPropertiesSapoData, default=None
    )

    service_now: Optional[ServiceNow] = core.attr(ServiceNow, default=None)

    singular: Optional[Singular] = core.attr(Singular, default=None)

    slack: Optional[Slack] = core.attr(Slack, default=None)

    trendmicro: Optional[Trendmicro] = core.attr(Trendmicro, default=None)

    veeva: Optional[Veeva] = core.attr(Veeva, default=None)

    zendesk: Optional[SourceConnectorPropertiesZendesk] = core.attr(
        SourceConnectorPropertiesZendesk, default=None
    )

    def __init__(
        self,
        *,
        amplitude: Optional[Amplitude] = None,
        custom_connector: Optional[SourceConnectorPropertiesCustomConnector] = None,
        datadog: Optional[Datadog] = None,
        dynatrace: Optional[Dynatrace] = None,
        google_analytics: Optional[GoogleAnalytics] = None,
        infor_nexus: Optional[InforNexus] = None,
        marketo: Optional[SourceConnectorPropertiesMarketo] = None,
        s3: Optional[SourceConnectorPropertiesS3] = None,
        salesforce: Optional[SourceConnectorPropertiesSalesforce] = None,
        sapo_data: Optional[SourceConnectorPropertiesSapoData] = None,
        service_now: Optional[ServiceNow] = None,
        singular: Optional[Singular] = None,
        slack: Optional[Slack] = None,
        trendmicro: Optional[Trendmicro] = None,
        veeva: Optional[Veeva] = None,
        zendesk: Optional[SourceConnectorPropertiesZendesk] = None,
    ):
        super().__init__(
            args=SourceConnectorProperties.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                infor_nexus=infor_nexus,
                marketo=marketo,
                s3=s3,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: Optional[Amplitude] = core.arg(default=None)

        custom_connector: Optional[SourceConnectorPropertiesCustomConnector] = core.arg(
            default=None
        )

        datadog: Optional[Datadog] = core.arg(default=None)

        dynatrace: Optional[Dynatrace] = core.arg(default=None)

        google_analytics: Optional[GoogleAnalytics] = core.arg(default=None)

        infor_nexus: Optional[InforNexus] = core.arg(default=None)

        marketo: Optional[SourceConnectorPropertiesMarketo] = core.arg(default=None)

        s3: Optional[SourceConnectorPropertiesS3] = core.arg(default=None)

        salesforce: Optional[SourceConnectorPropertiesSalesforce] = core.arg(default=None)

        sapo_data: Optional[SourceConnectorPropertiesSapoData] = core.arg(default=None)

        service_now: Optional[ServiceNow] = core.arg(default=None)

        singular: Optional[Singular] = core.arg(default=None)

        slack: Optional[Slack] = core.arg(default=None)

        trendmicro: Optional[Trendmicro] = core.arg(default=None)

        veeva: Optional[Veeva] = core.arg(default=None)

        zendesk: Optional[SourceConnectorPropertiesZendesk] = core.arg(default=None)


@core.schema
class SourceFlowConfig(core.Schema):

    api_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connector_profile_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connector_type: Union[str, core.StringOut] = core.attr(str)

    incremental_pull_config: Optional[IncrementalPullConfig] = core.attr(
        IncrementalPullConfig, default=None
    )

    source_connector_properties: SourceConnectorProperties = core.attr(SourceConnectorProperties)

    def __init__(
        self,
        *,
        connector_type: Union[str, core.StringOut],
        source_connector_properties: SourceConnectorProperties,
        api_version: Optional[Union[str, core.StringOut]] = None,
        connector_profile_name: Optional[Union[str, core.StringOut]] = None,
        incremental_pull_config: Optional[IncrementalPullConfig] = None,
    ):
        super().__init__(
            args=SourceFlowConfig.Args(
                connector_type=connector_type,
                source_connector_properties=source_connector_properties,
                api_version=api_version,
                connector_profile_name=connector_profile_name,
                incremental_pull_config=incremental_pull_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connector_profile_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connector_type: Union[str, core.StringOut] = core.arg()

        incremental_pull_config: Optional[IncrementalPullConfig] = core.arg(default=None)

        source_connector_properties: SourceConnectorProperties = core.arg()


@core.schema
class ConnectorOperator(core.Schema):

    amplitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_connector: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    datadog: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dynatrace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    google_analytics: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    infor_nexus: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    marketo: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    salesforce: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sapo_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_now: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    singular: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    slack: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    trendmicro: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    veeva: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    zendesk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        amplitude: Optional[Union[str, core.StringOut]] = None,
        custom_connector: Optional[Union[str, core.StringOut]] = None,
        datadog: Optional[Union[str, core.StringOut]] = None,
        dynatrace: Optional[Union[str, core.StringOut]] = None,
        google_analytics: Optional[Union[str, core.StringOut]] = None,
        infor_nexus: Optional[Union[str, core.StringOut]] = None,
        marketo: Optional[Union[str, core.StringOut]] = None,
        s3: Optional[Union[str, core.StringOut]] = None,
        salesforce: Optional[Union[str, core.StringOut]] = None,
        sapo_data: Optional[Union[str, core.StringOut]] = None,
        service_now: Optional[Union[str, core.StringOut]] = None,
        singular: Optional[Union[str, core.StringOut]] = None,
        slack: Optional[Union[str, core.StringOut]] = None,
        trendmicro: Optional[Union[str, core.StringOut]] = None,
        veeva: Optional[Union[str, core.StringOut]] = None,
        zendesk: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorOperator.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                infor_nexus=infor_nexus,
                marketo=marketo,
                s3=s3,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_connector: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        datadog: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dynatrace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        google_analytics: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        infor_nexus: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        marketo: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        salesforce: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sapo_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_now: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        singular: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        slack: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        trendmicro: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        veeva: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zendesk: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Task(core.Schema):

    connector_operator: Optional[
        Union[List[ConnectorOperator], core.ArrayOut[ConnectorOperator]]
    ] = core.attr(ConnectorOperator, default=None, kind=core.Kind.array)

    destination_field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_fields: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    task_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    task_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source_fields: Union[List[str], core.ArrayOut[core.StringOut]],
        task_type: Union[str, core.StringOut],
        connector_operator: Optional[
            Union[List[ConnectorOperator], core.ArrayOut[ConnectorOperator]]
        ] = None,
        destination_field: Optional[Union[str, core.StringOut]] = None,
        task_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Task.Args(
                source_fields=source_fields,
                task_type=task_type,
                connector_operator=connector_operator,
                destination_field=destination_field,
                task_properties=task_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connector_operator: Optional[
            Union[List[ConnectorOperator], core.ArrayOut[ConnectorOperator]]
        ] = core.arg(default=None)

        destination_field: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_fields: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        task_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        task_type: Union[str, core.StringOut] = core.arg()


@core.schema
class LookoutMetrics(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class CustomerProfiles(core.Schema):

    domain_name: Union[str, core.StringOut] = core.attr(str)

    object_type_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        domain_name: Union[str, core.StringOut],
        object_type_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomerProfiles.Args(
                domain_name=domain_name,
                object_type_name=object_type_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Union[str, core.StringOut] = core.arg()

        object_type_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ErrorHandlingConfig(core.Schema):

    bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fail_on_first_destination_error: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        bucket_name: Optional[Union[str, core.StringOut]] = None,
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        fail_on_first_destination_error: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ErrorHandlingConfig.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                fail_on_first_destination_error=fail_on_first_destination_error,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fail_on_first_destination_error: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.schema
class Snowflake(core.Schema):

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    intermediate_bucket_name: Union[str, core.StringOut] = core.attr(str)

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        intermediate_bucket_name: Union[str, core.StringOut],
        object: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        error_handling_config: Optional[ErrorHandlingConfig] = None,
    ):
        super().__init__(
            args=Snowflake.Args(
                intermediate_bucket_name=intermediate_bucket_name,
                object=object,
                bucket_prefix=bucket_prefix,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        intermediate_bucket_name: Union[str, core.StringOut] = core.arg()

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class AggregationConfig(core.Schema):

    aggregation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aggregation_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AggregationConfig.Args(
                aggregation_type=aggregation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class UpsolverS3OutputFormatConfigPrefixConfig(core.Schema):

    prefix_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        prefix_type: Union[str, core.StringOut],
        prefix_format: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=UpsolverS3OutputFormatConfigPrefixConfig.Args(
                prefix_type=prefix_type,
                prefix_format=prefix_format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix_type: Union[str, core.StringOut] = core.arg()


@core.schema
class UpsolverS3OutputFormatConfig(core.Schema):

    aggregation_config: Optional[AggregationConfig] = core.attr(AggregationConfig, default=None)

    file_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix_config: UpsolverS3OutputFormatConfigPrefixConfig = core.attr(
        UpsolverS3OutputFormatConfigPrefixConfig
    )

    def __init__(
        self,
        *,
        prefix_config: UpsolverS3OutputFormatConfigPrefixConfig,
        aggregation_config: Optional[AggregationConfig] = None,
        file_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=UpsolverS3OutputFormatConfig.Args(
                prefix_config=prefix_config,
                aggregation_config=aggregation_config,
                file_type=file_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_config: Optional[AggregationConfig] = core.arg(default=None)

        file_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix_config: UpsolverS3OutputFormatConfigPrefixConfig = core.arg()


@core.schema
class Upsolver(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_output_format_config: UpsolverS3OutputFormatConfig = core.attr(UpsolverS3OutputFormatConfig)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        s3_output_format_config: UpsolverS3OutputFormatConfig,
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Upsolver.Args(
                bucket_name=bucket_name,
                s3_output_format_config=s3_output_format_config,
                bucket_prefix=bucket_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_output_format_config: UpsolverS3OutputFormatConfig = core.arg()


@core.schema
class EventBridge(core.Schema):

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        error_handling_config: Optional[ErrorHandlingConfig] = None,
    ):
        super().__init__(
            args=EventBridge.Args(
                object=object,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationConnectorPropertiesMarketo(core.Schema):

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        error_handling_config: Optional[ErrorHandlingConfig] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesMarketo.Args(
                object=object,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class Redshift(core.Schema):

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    intermediate_bucket_name: Union[str, core.StringOut] = core.attr(str)

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        intermediate_bucket_name: Union[str, core.StringOut],
        object: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        error_handling_config: Optional[ErrorHandlingConfig] = None,
    ):
        super().__init__(
            args=Redshift.Args(
                intermediate_bucket_name=intermediate_bucket_name,
                object=object,
                bucket_prefix=bucket_prefix,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        intermediate_bucket_name: Union[str, core.StringOut] = core.arg()

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(core.Schema):

    prefix_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        prefix_format: Optional[Union[str, core.StringOut]] = None,
        prefix_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig.Args(
                prefix_format=prefix_format,
                prefix_type=prefix_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesS3S3OutputFormatConfig(core.Schema):

    aggregation_config: Optional[AggregationConfig] = core.attr(AggregationConfig, default=None)

    file_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix_config: Optional[
        DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig
    ] = core.attr(DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig, default=None)

    def __init__(
        self,
        *,
        aggregation_config: Optional[AggregationConfig] = None,
        file_type: Optional[Union[str, core.StringOut]] = None,
        prefix_config: Optional[
            DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig
        ] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesS3S3OutputFormatConfig.Args(
                aggregation_config=aggregation_config,
                file_type=file_type,
                prefix_config=prefix_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_config: Optional[AggregationConfig] = core.arg(default=None)

        file_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix_config: Optional[
            DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig
        ] = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesS3(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_output_format_config: Optional[
        DestinationConnectorPropertiesS3S3OutputFormatConfig
    ] = core.attr(DestinationConnectorPropertiesS3S3OutputFormatConfig, default=None)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        s3_output_format_config: Optional[
            DestinationConnectorPropertiesS3S3OutputFormatConfig
        ] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesS3.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                s3_output_format_config=s3_output_format_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_output_format_config: Optional[
            DestinationConnectorPropertiesS3S3OutputFormatConfig
        ] = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesCustomConnector(core.Schema):

    custom_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    entity_name: Union[str, core.StringOut] = core.attr(str)

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    write_operation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        entity_name: Union[str, core.StringOut],
        custom_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        error_handling_config: Optional[ErrorHandlingConfig] = None,
        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        write_operation_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesCustomConnector.Args(
                entity_name=entity_name,
                custom_properties=custom_properties,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        entity_name: Union[str, core.StringOut] = core.arg()

        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        write_operation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Honeycode(core.Schema):

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    object: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        error_handling_config: Optional[ErrorHandlingConfig] = None,
    ):
        super().__init__(
            args=Honeycode.Args(
                object=object,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        object: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationConnectorPropertiesSalesforce(core.Schema):

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    object: Union[str, core.StringOut] = core.attr(str)

    write_operation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        error_handling_config: Optional[ErrorHandlingConfig] = None,
        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        write_operation_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesSalesforce.Args(
                object=object,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        object: Union[str, core.StringOut] = core.arg()

        write_operation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SuccessResponseHandlingConfig(core.Schema):

    bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: Optional[Union[str, core.StringOut]] = None,
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SuccessResponseHandlingConfig.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesSapoData(core.Schema):

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    object_path: Union[str, core.StringOut] = core.attr(str)

    success_response_handling_config: Optional[SuccessResponseHandlingConfig] = core.attr(
        SuccessResponseHandlingConfig, default=None
    )

    write_operation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        object_path: Union[str, core.StringOut],
        error_handling_config: Optional[ErrorHandlingConfig] = None,
        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        success_response_handling_config: Optional[SuccessResponseHandlingConfig] = None,
        write_operation_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesSapoData.Args(
                object_path=object_path,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                success_response_handling_config=success_response_handling_config,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        object_path: Union[str, core.StringOut] = core.arg()

        success_response_handling_config: Optional[SuccessResponseHandlingConfig] = core.arg(
            default=None
        )

        write_operation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesZendesk(core.Schema):

    error_handling_config: Optional[ErrorHandlingConfig] = core.attr(
        ErrorHandlingConfig, default=None
    )

    id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    object: Union[str, core.StringOut] = core.attr(str)

    write_operation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        object: Union[str, core.StringOut],
        error_handling_config: Optional[ErrorHandlingConfig] = None,
        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        write_operation_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesZendesk.Args(
                object=object,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: Optional[ErrorHandlingConfig] = core.arg(default=None)

        id_field_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        object: Union[str, core.StringOut] = core.arg()

        write_operation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DestinationConnectorProperties(core.Schema):

    custom_connector: Optional[DestinationConnectorPropertiesCustomConnector] = core.attr(
        DestinationConnectorPropertiesCustomConnector, default=None
    )

    customer_profiles: Optional[CustomerProfiles] = core.attr(CustomerProfiles, default=None)

    event_bridge: Optional[EventBridge] = core.attr(EventBridge, default=None)

    honeycode: Optional[Honeycode] = core.attr(Honeycode, default=None)

    lookout_metrics: Optional[LookoutMetrics] = core.attr(LookoutMetrics, default=None)

    marketo: Optional[DestinationConnectorPropertiesMarketo] = core.attr(
        DestinationConnectorPropertiesMarketo, default=None
    )

    redshift: Optional[Redshift] = core.attr(Redshift, default=None)

    s3: Optional[DestinationConnectorPropertiesS3] = core.attr(
        DestinationConnectorPropertiesS3, default=None
    )

    salesforce: Optional[DestinationConnectorPropertiesSalesforce] = core.attr(
        DestinationConnectorPropertiesSalesforce, default=None
    )

    sapo_data: Optional[DestinationConnectorPropertiesSapoData] = core.attr(
        DestinationConnectorPropertiesSapoData, default=None
    )

    snowflake: Optional[Snowflake] = core.attr(Snowflake, default=None)

    upsolver: Optional[Upsolver] = core.attr(Upsolver, default=None)

    zendesk: Optional[DestinationConnectorPropertiesZendesk] = core.attr(
        DestinationConnectorPropertiesZendesk, default=None
    )

    def __init__(
        self,
        *,
        custom_connector: Optional[DestinationConnectorPropertiesCustomConnector] = None,
        customer_profiles: Optional[CustomerProfiles] = None,
        event_bridge: Optional[EventBridge] = None,
        honeycode: Optional[Honeycode] = None,
        lookout_metrics: Optional[LookoutMetrics] = None,
        marketo: Optional[DestinationConnectorPropertiesMarketo] = None,
        redshift: Optional[Redshift] = None,
        s3: Optional[DestinationConnectorPropertiesS3] = None,
        salesforce: Optional[DestinationConnectorPropertiesSalesforce] = None,
        sapo_data: Optional[DestinationConnectorPropertiesSapoData] = None,
        snowflake: Optional[Snowflake] = None,
        upsolver: Optional[Upsolver] = None,
        zendesk: Optional[DestinationConnectorPropertiesZendesk] = None,
    ):
        super().__init__(
            args=DestinationConnectorProperties.Args(
                custom_connector=custom_connector,
                customer_profiles=customer_profiles,
                event_bridge=event_bridge,
                honeycode=honeycode,
                lookout_metrics=lookout_metrics,
                marketo=marketo,
                redshift=redshift,
                s3=s3,
                salesforce=salesforce,
                sapo_data=sapo_data,
                snowflake=snowflake,
                upsolver=upsolver,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_connector: Optional[DestinationConnectorPropertiesCustomConnector] = core.arg(
            default=None
        )

        customer_profiles: Optional[CustomerProfiles] = core.arg(default=None)

        event_bridge: Optional[EventBridge] = core.arg(default=None)

        honeycode: Optional[Honeycode] = core.arg(default=None)

        lookout_metrics: Optional[LookoutMetrics] = core.arg(default=None)

        marketo: Optional[DestinationConnectorPropertiesMarketo] = core.arg(default=None)

        redshift: Optional[Redshift] = core.arg(default=None)

        s3: Optional[DestinationConnectorPropertiesS3] = core.arg(default=None)

        salesforce: Optional[DestinationConnectorPropertiesSalesforce] = core.arg(default=None)

        sapo_data: Optional[DestinationConnectorPropertiesSapoData] = core.arg(default=None)

        snowflake: Optional[Snowflake] = core.arg(default=None)

        upsolver: Optional[Upsolver] = core.arg(default=None)

        zendesk: Optional[DestinationConnectorPropertiesZendesk] = core.arg(default=None)


@core.schema
class DestinationFlowConfig(core.Schema):

    api_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connector_profile_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connector_type: Union[str, core.StringOut] = core.attr(str)

    destination_connector_properties: DestinationConnectorProperties = core.attr(
        DestinationConnectorProperties
    )

    def __init__(
        self,
        *,
        connector_type: Union[str, core.StringOut],
        destination_connector_properties: DestinationConnectorProperties,
        api_version: Optional[Union[str, core.StringOut]] = None,
        connector_profile_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationFlowConfig.Args(
                connector_type=connector_type,
                destination_connector_properties=destination_connector_properties,
                api_version=api_version,
                connector_profile_name=connector_profile_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connector_profile_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connector_type: Union[str, core.StringOut] = core.arg()

        destination_connector_properties: DestinationConnectorProperties = core.arg()


@core.schema
class Scheduled(core.Schema):

    data_pull_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    first_execution_from: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schedule_end_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schedule_expression: Union[str, core.StringOut] = core.attr(str)

    schedule_offset: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    schedule_start_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timezone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        schedule_expression: Union[str, core.StringOut],
        data_pull_mode: Optional[Union[str, core.StringOut]] = None,
        first_execution_from: Optional[Union[str, core.StringOut]] = None,
        schedule_end_time: Optional[Union[str, core.StringOut]] = None,
        schedule_offset: Optional[Union[int, core.IntOut]] = None,
        schedule_start_time: Optional[Union[str, core.StringOut]] = None,
        timezone: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Scheduled.Args(
                schedule_expression=schedule_expression,
                data_pull_mode=data_pull_mode,
                first_execution_from=first_execution_from,
                schedule_end_time=schedule_end_time,
                schedule_offset=schedule_offset,
                schedule_start_time=schedule_start_time,
                timezone=timezone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_pull_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        first_execution_from: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schedule_end_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schedule_expression: Union[str, core.StringOut] = core.arg()

        schedule_offset: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        schedule_start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timezone: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TriggerProperties(core.Schema):

    scheduled: Optional[Scheduled] = core.attr(Scheduled, default=None)

    def __init__(
        self,
        *,
        scheduled: Optional[Scheduled] = None,
    ):
        super().__init__(
            args=TriggerProperties.Args(
                scheduled=scheduled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scheduled: Optional[Scheduled] = core.arg(default=None)


@core.schema
class TriggerConfig(core.Schema):

    trigger_properties: Optional[TriggerProperties] = core.attr(
        TriggerProperties, default=None, computed=True
    )

    trigger_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        trigger_type: Union[str, core.StringOut],
        trigger_properties: Optional[TriggerProperties] = None,
    ):
        super().__init__(
            args=TriggerConfig.Args(
                trigger_type=trigger_type,
                trigger_properties=trigger_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        trigger_properties: Optional[TriggerProperties] = core.arg(default=None)

        trigger_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_appflow_flow", namespace="aws_appflow")
class Flow(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_flow_config: Union[
        List[DestinationFlowConfig], core.ArrayOut[DestinationFlowConfig]
    ] = core.attr(DestinationFlowConfig, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    source_flow_config: SourceFlowConfig = core.attr(SourceFlowConfig)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task: Union[List[Task], core.ArrayOut[Task]] = core.attr(Task, kind=core.Kind.array)

    trigger_config: TriggerConfig = core.attr(TriggerConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_flow_config: Union[
            List[DestinationFlowConfig], core.ArrayOut[DestinationFlowConfig]
        ],
        name: Union[str, core.StringOut],
        source_flow_config: SourceFlowConfig,
        task: Union[List[Task], core.ArrayOut[Task]],
        trigger_config: TriggerConfig,
        description: Optional[Union[str, core.StringOut]] = None,
        kms_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Flow.Args(
                destination_flow_config=destination_flow_config,
                name=name,
                source_flow_config=source_flow_config,
                task=task,
                trigger_config=trigger_config,
                description=description,
                kms_arn=kms_arn,
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

        destination_flow_config: Union[
            List[DestinationFlowConfig], core.ArrayOut[DestinationFlowConfig]
        ] = core.arg()

        kms_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        source_flow_config: SourceFlowConfig = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        task: Union[List[Task], core.ArrayOut[Task]] = core.arg()

        trigger_config: TriggerConfig = core.arg()
