from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AccessControlListConfiguration(core.Schema):

    key_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key_path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AccessControlListConfiguration.Args(
                key_path=key_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DocumentsMetadataConfiguration(core.Schema):

    s3_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DocumentsMetadataConfiguration.Args(
                s3_prefix=s3_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3Configuration(core.Schema):

    access_control_list_configuration: Optional[AccessControlListConfiguration] = core.attr(
        AccessControlListConfiguration, default=None
    )

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    documents_metadata_configuration: Optional[DocumentsMetadataConfiguration] = core.attr(
        DocumentsMetadataConfiguration, default=None
    )

    exclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    inclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    inclusion_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        access_control_list_configuration: Optional[AccessControlListConfiguration] = None,
        documents_metadata_configuration: Optional[DocumentsMetadataConfiguration] = None,
        exclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        inclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        inclusion_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=S3Configuration.Args(
                bucket_name=bucket_name,
                access_control_list_configuration=access_control_list_configuration,
                documents_metadata_configuration=documents_metadata_configuration,
                exclusion_patterns=exclusion_patterns,
                inclusion_patterns=inclusion_patterns,
                inclusion_prefixes=inclusion_prefixes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_list_configuration: Optional[AccessControlListConfiguration] = core.arg(
            default=None
        )

        bucket_name: Union[str, core.StringOut] = core.arg()

        documents_metadata_configuration: Optional[DocumentsMetadataConfiguration] = core.arg(
            default=None
        )

        exclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        inclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        inclusion_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class BasicAuthentication(core.Schema):

    credentials: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        credentials: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=BasicAuthentication.Args(
                credentials=credentials,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class AuthenticationConfiguration(core.Schema):

    basic_authentication: Optional[
        Union[List[BasicAuthentication], core.ArrayOut[BasicAuthentication]]
    ] = core.attr(BasicAuthentication, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        basic_authentication: Optional[
            Union[List[BasicAuthentication], core.ArrayOut[BasicAuthentication]]
        ] = None,
    ):
        super().__init__(
            args=AuthenticationConfiguration.Args(
                basic_authentication=basic_authentication,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        basic_authentication: Optional[
            Union[List[BasicAuthentication], core.ArrayOut[BasicAuthentication]]
        ] = core.arg(default=None)


@core.schema
class ProxyConfiguration(core.Schema):

    credentials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
        credentials: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProxyConfiguration.Args(
                host=host,
                port=port,
                credentials=credentials,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class SeedUrlConfiguration(core.Schema):

    seed_urls: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    web_crawler_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        seed_urls: Union[List[str], core.ArrayOut[core.StringOut]],
        web_crawler_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SeedUrlConfiguration.Args(
                seed_urls=seed_urls,
                web_crawler_mode=web_crawler_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        seed_urls: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        web_crawler_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SiteMapsConfiguration(core.Schema):

    site_maps: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        site_maps: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=SiteMapsConfiguration.Args(
                site_maps=site_maps,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        site_maps: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Urls(core.Schema):

    seed_url_configuration: Optional[SeedUrlConfiguration] = core.attr(
        SeedUrlConfiguration, default=None
    )

    site_maps_configuration: Optional[SiteMapsConfiguration] = core.attr(
        SiteMapsConfiguration, default=None
    )

    def __init__(
        self,
        *,
        seed_url_configuration: Optional[SeedUrlConfiguration] = None,
        site_maps_configuration: Optional[SiteMapsConfiguration] = None,
    ):
        super().__init__(
            args=Urls.Args(
                seed_url_configuration=seed_url_configuration,
                site_maps_configuration=site_maps_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        seed_url_configuration: Optional[SeedUrlConfiguration] = core.arg(default=None)

        site_maps_configuration: Optional[SiteMapsConfiguration] = core.arg(default=None)


@core.schema
class WebCrawlerConfiguration(core.Schema):

    authentication_configuration: Optional[AuthenticationConfiguration] = core.attr(
        AuthenticationConfiguration, default=None
    )

    crawl_depth: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_content_size_per_page_in_mega_bytes: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    max_links_per_page: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_urls_per_minute_crawl_rate: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    proxy_configuration: Optional[ProxyConfiguration] = core.attr(ProxyConfiguration, default=None)

    url_exclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    url_inclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    urls: Urls = core.attr(Urls)

    def __init__(
        self,
        *,
        urls: Urls,
        authentication_configuration: Optional[AuthenticationConfiguration] = None,
        crawl_depth: Optional[Union[int, core.IntOut]] = None,
        max_content_size_per_page_in_mega_bytes: Optional[Union[float, core.FloatOut]] = None,
        max_links_per_page: Optional[Union[int, core.IntOut]] = None,
        max_urls_per_minute_crawl_rate: Optional[Union[int, core.IntOut]] = None,
        proxy_configuration: Optional[ProxyConfiguration] = None,
        url_exclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        url_inclusion_patterns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=WebCrawlerConfiguration.Args(
                urls=urls,
                authentication_configuration=authentication_configuration,
                crawl_depth=crawl_depth,
                max_content_size_per_page_in_mega_bytes=max_content_size_per_page_in_mega_bytes,
                max_links_per_page=max_links_per_page,
                max_urls_per_minute_crawl_rate=max_urls_per_minute_crawl_rate,
                proxy_configuration=proxy_configuration,
                url_exclusion_patterns=url_exclusion_patterns,
                url_inclusion_patterns=url_inclusion_patterns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_configuration: Optional[AuthenticationConfiguration] = core.arg(default=None)

        crawl_depth: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_content_size_per_page_in_mega_bytes: Optional[Union[float, core.FloatOut]] = core.arg(
            default=None
        )

        max_links_per_page: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_urls_per_minute_crawl_rate: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        proxy_configuration: Optional[ProxyConfiguration] = core.arg(default=None)

        url_exclusion_patterns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        url_inclusion_patterns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        urls: Urls = core.arg()


@core.schema
class Configuration(core.Schema):

    s3_configuration: Optional[S3Configuration] = core.attr(S3Configuration, default=None)

    web_crawler_configuration: Optional[WebCrawlerConfiguration] = core.attr(
        WebCrawlerConfiguration, default=None
    )

    def __init__(
        self,
        *,
        s3_configuration: Optional[S3Configuration] = None,
        web_crawler_configuration: Optional[WebCrawlerConfiguration] = None,
    ):
        super().__init__(
            args=Configuration.Args(
                s3_configuration=s3_configuration,
                web_crawler_configuration=web_crawler_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_configuration: Optional[S3Configuration] = core.arg(default=None)

        web_crawler_configuration: Optional[WebCrawlerConfiguration] = core.arg(default=None)


@core.schema
class ConditionOnValue(core.Schema):

    date_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    long_value: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    string_list_value: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    string_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_value: Optional[Union[str, core.StringOut]] = None,
        long_value: Optional[Union[int, core.IntOut]] = None,
        string_list_value: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        string_value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConditionOnValue.Args(
                date_value=date_value,
                long_value=long_value,
                string_list_value=string_list_value,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        long_value: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        string_list_value: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        string_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Condition(core.Schema):

    condition_document_attribute_key: Union[str, core.StringOut] = core.attr(str)

    condition_on_value: Optional[ConditionOnValue] = core.attr(ConditionOnValue, default=None)

    operator: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        condition_document_attribute_key: Union[str, core.StringOut],
        operator: Union[str, core.StringOut],
        condition_on_value: Optional[ConditionOnValue] = None,
    ):
        super().__init__(
            args=Condition.Args(
                condition_document_attribute_key=condition_document_attribute_key,
                operator=operator,
                condition_on_value=condition_on_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition_document_attribute_key: Union[str, core.StringOut] = core.arg()

        condition_on_value: Optional[ConditionOnValue] = core.arg(default=None)

        operator: Union[str, core.StringOut] = core.arg()


@core.schema
class TargetDocumentAttributeValue(core.Schema):

    date_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    long_value: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    string_list_value: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    string_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_value: Optional[Union[str, core.StringOut]] = None,
        long_value: Optional[Union[int, core.IntOut]] = None,
        string_list_value: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        string_value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TargetDocumentAttributeValue.Args(
                date_value=date_value,
                long_value=long_value,
                string_list_value=string_list_value,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        long_value: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        string_list_value: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        string_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Target(core.Schema):

    target_document_attribute_key: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    target_document_attribute_value: Optional[TargetDocumentAttributeValue] = core.attr(
        TargetDocumentAttributeValue, default=None
    )

    target_document_attribute_value_deletion: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        target_document_attribute_key: Optional[Union[str, core.StringOut]] = None,
        target_document_attribute_value: Optional[TargetDocumentAttributeValue] = None,
        target_document_attribute_value_deletion: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Target.Args(
                target_document_attribute_key=target_document_attribute_key,
                target_document_attribute_value=target_document_attribute_value,
                target_document_attribute_value_deletion=target_document_attribute_value_deletion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_document_attribute_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_document_attribute_value: Optional[TargetDocumentAttributeValue] = core.arg(
            default=None
        )

        target_document_attribute_value_deletion: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.schema
class InlineConfigurations(core.Schema):

    condition: Optional[Condition] = core.attr(Condition, default=None)

    document_content_deletion: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    target: Optional[Target] = core.attr(Target, default=None)

    def __init__(
        self,
        *,
        condition: Optional[Condition] = None,
        document_content_deletion: Optional[Union[bool, core.BoolOut]] = None,
        target: Optional[Target] = None,
    ):
        super().__init__(
            args=InlineConfigurations.Args(
                condition=condition,
                document_content_deletion=document_content_deletion,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition: Optional[Condition] = core.arg(default=None)

        document_content_deletion: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        target: Optional[Target] = core.arg(default=None)


@core.schema
class InvocationCondition(core.Schema):

    condition_document_attribute_key: Union[str, core.StringOut] = core.attr(str)

    condition_on_value: Optional[ConditionOnValue] = core.attr(ConditionOnValue, default=None)

    operator: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        condition_document_attribute_key: Union[str, core.StringOut],
        operator: Union[str, core.StringOut],
        condition_on_value: Optional[ConditionOnValue] = None,
    ):
        super().__init__(
            args=InvocationCondition.Args(
                condition_document_attribute_key=condition_document_attribute_key,
                operator=operator,
                condition_on_value=condition_on_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition_document_attribute_key: Union[str, core.StringOut] = core.arg()

        condition_on_value: Optional[ConditionOnValue] = core.arg(default=None)

        operator: Union[str, core.StringOut] = core.arg()


@core.schema
class PostExtractionHookConfiguration(core.Schema):

    invocation_condition: Optional[InvocationCondition] = core.attr(
        InvocationCondition, default=None
    )

    lambda_arn: Union[str, core.StringOut] = core.attr(str)

    s3_bucket: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: Union[str, core.StringOut],
        s3_bucket: Union[str, core.StringOut],
        invocation_condition: Optional[InvocationCondition] = None,
    ):
        super().__init__(
            args=PostExtractionHookConfiguration.Args(
                lambda_arn=lambda_arn,
                s3_bucket=s3_bucket,
                invocation_condition=invocation_condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invocation_condition: Optional[InvocationCondition] = core.arg(default=None)

        lambda_arn: Union[str, core.StringOut] = core.arg()

        s3_bucket: Union[str, core.StringOut] = core.arg()


@core.schema
class PreExtractionHookConfiguration(core.Schema):

    invocation_condition: Optional[InvocationCondition] = core.attr(
        InvocationCondition, default=None
    )

    lambda_arn: Union[str, core.StringOut] = core.attr(str)

    s3_bucket: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: Union[str, core.StringOut],
        s3_bucket: Union[str, core.StringOut],
        invocation_condition: Optional[InvocationCondition] = None,
    ):
        super().__init__(
            args=PreExtractionHookConfiguration.Args(
                lambda_arn=lambda_arn,
                s3_bucket=s3_bucket,
                invocation_condition=invocation_condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invocation_condition: Optional[InvocationCondition] = core.arg(default=None)

        lambda_arn: Union[str, core.StringOut] = core.arg()

        s3_bucket: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomDocumentEnrichmentConfiguration(core.Schema):

    inline_configurations: Optional[
        Union[List[InlineConfigurations], core.ArrayOut[InlineConfigurations]]
    ] = core.attr(InlineConfigurations, default=None, kind=core.Kind.array)

    post_extraction_hook_configuration: Optional[PostExtractionHookConfiguration] = core.attr(
        PostExtractionHookConfiguration, default=None
    )

    pre_extraction_hook_configuration: Optional[PreExtractionHookConfiguration] = core.attr(
        PreExtractionHookConfiguration, default=None
    )

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        inline_configurations: Optional[
            Union[List[InlineConfigurations], core.ArrayOut[InlineConfigurations]]
        ] = None,
        post_extraction_hook_configuration: Optional[PostExtractionHookConfiguration] = None,
        pre_extraction_hook_configuration: Optional[PreExtractionHookConfiguration] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomDocumentEnrichmentConfiguration.Args(
                inline_configurations=inline_configurations,
                post_extraction_hook_configuration=post_extraction_hook_configuration,
                pre_extraction_hook_configuration=pre_extraction_hook_configuration,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        inline_configurations: Optional[
            Union[List[InlineConfigurations], core.ArrayOut[InlineConfigurations]]
        ] = core.arg(default=None)

        post_extraction_hook_configuration: Optional[PostExtractionHookConfiguration] = core.arg(
            default=None
        )

        pre_extraction_hook_configuration: Optional[PreExtractionHookConfiguration] = core.arg(
            default=None
        )

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_kendra_data_source", namespace="aws_kendra")
class DataSource(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration: Optional[Configuration] = core.attr(Configuration, default=None)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    custom_document_enrichment_configuration: Optional[
        CustomDocumentEnrichmentConfiguration
    ] = core.attr(CustomDocumentEnrichmentConfiguration, default=None)

    data_source_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_id: Union[str, core.StringOut] = core.attr(str)

    language_code: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schedule: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        configuration: Optional[Configuration] = None,
        custom_document_enrichment_configuration: Optional[
            CustomDocumentEnrichmentConfiguration
        ] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        language_code: Optional[Union[str, core.StringOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        schedule: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataSource.Args(
                index_id=index_id,
                name=name,
                type=type,
                configuration=configuration,
                custom_document_enrichment_configuration=custom_document_enrichment_configuration,
                description=description,
                language_code=language_code,
                role_arn=role_arn,
                schedule=schedule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Optional[Configuration] = core.arg(default=None)

        custom_document_enrichment_configuration: Optional[
            CustomDocumentEnrichmentConfiguration
        ] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_id: Union[str, core.StringOut] = core.arg()

        language_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schedule: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
