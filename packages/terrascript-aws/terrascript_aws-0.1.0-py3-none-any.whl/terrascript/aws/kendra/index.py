from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ServerSideEncryptionConfiguration(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ServerSideEncryptionConfiguration.Args(
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Search(core.Schema):

    displayable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    facetable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    searchable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    sortable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        displayable: Optional[Union[bool, core.BoolOut]] = None,
        facetable: Optional[Union[bool, core.BoolOut]] = None,
        searchable: Optional[Union[bool, core.BoolOut]] = None,
        sortable: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Search.Args(
                displayable=displayable,
                facetable=facetable,
                searchable=searchable,
                sortable=sortable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        displayable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        facetable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        searchable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sortable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Relevance(core.Schema):

    duration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    freshness: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    importance: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    rank_order: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    values_importance_map: Optional[Union[Dict[str, int], core.MapOut[core.IntOut]]] = core.attr(
        int, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        duration: Optional[Union[str, core.StringOut]] = None,
        freshness: Optional[Union[bool, core.BoolOut]] = None,
        importance: Optional[Union[int, core.IntOut]] = None,
        rank_order: Optional[Union[str, core.StringOut]] = None,
        values_importance_map: Optional[Union[Dict[str, int], core.MapOut[core.IntOut]]] = None,
    ):
        super().__init__(
            args=Relevance.Args(
                duration=duration,
                freshness=freshness,
                importance=importance,
                rank_order=rank_order,
                values_importance_map=values_importance_map,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        freshness: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        importance: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        rank_order: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        values_importance_map: Optional[Union[Dict[str, int], core.MapOut[core.IntOut]]] = core.arg(
            default=None
        )


@core.schema
class DocumentMetadataConfigurationUpdates(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    relevance: Optional[Relevance] = core.attr(Relevance, default=None, computed=True)

    search: Optional[Search] = core.attr(Search, default=None, computed=True)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        relevance: Optional[Relevance] = None,
        search: Optional[Search] = None,
    ):
        super().__init__(
            args=DocumentMetadataConfigurationUpdates.Args(
                name=name,
                type=type,
                relevance=relevance,
                search=search,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        relevance: Optional[Relevance] = core.arg(default=None)

        search: Optional[Search] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class CapacityUnits(core.Schema):

    query_capacity_units: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    storage_capacity_units: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        query_capacity_units: Optional[Union[int, core.IntOut]] = None,
        storage_capacity_units: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CapacityUnits.Args(
                query_capacity_units=query_capacity_units,
                storage_capacity_units=storage_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query_capacity_units: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_capacity_units: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class JsonTokenTypeConfiguration(core.Schema):

    group_attribute_field: Union[str, core.StringOut] = core.attr(str)

    user_name_attribute_field: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        group_attribute_field: Union[str, core.StringOut],
        user_name_attribute_field: Union[str, core.StringOut],
    ):
        super().__init__(
            args=JsonTokenTypeConfiguration.Args(
                group_attribute_field=group_attribute_field,
                user_name_attribute_field=user_name_attribute_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_attribute_field: Union[str, core.StringOut] = core.arg()

        user_name_attribute_field: Union[str, core.StringOut] = core.arg()


@core.schema
class JwtTokenTypeConfiguration(core.Schema):

    claim_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    group_attribute_field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    issuer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key_location: Union[str, core.StringOut] = core.attr(str)

    secrets_manager_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_name_attribute_field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key_location: Union[str, core.StringOut],
        claim_regex: Optional[Union[str, core.StringOut]] = None,
        group_attribute_field: Optional[Union[str, core.StringOut]] = None,
        issuer: Optional[Union[str, core.StringOut]] = None,
        secrets_manager_arn: Optional[Union[str, core.StringOut]] = None,
        url: Optional[Union[str, core.StringOut]] = None,
        user_name_attribute_field: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=JwtTokenTypeConfiguration.Args(
                key_location=key_location,
                claim_regex=claim_regex,
                group_attribute_field=group_attribute_field,
                issuer=issuer,
                secrets_manager_arn=secrets_manager_arn,
                url=url,
                user_name_attribute_field=user_name_attribute_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        claim_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        group_attribute_field: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        issuer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key_location: Union[str, core.StringOut] = core.arg()

        secrets_manager_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_name_attribute_field: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class UserTokenConfigurations(core.Schema):

    json_token_type_configuration: Optional[JsonTokenTypeConfiguration] = core.attr(
        JsonTokenTypeConfiguration, default=None
    )

    jwt_token_type_configuration: Optional[JwtTokenTypeConfiguration] = core.attr(
        JwtTokenTypeConfiguration, default=None
    )

    def __init__(
        self,
        *,
        json_token_type_configuration: Optional[JsonTokenTypeConfiguration] = None,
        jwt_token_type_configuration: Optional[JwtTokenTypeConfiguration] = None,
    ):
        super().__init__(
            args=UserTokenConfigurations.Args(
                json_token_type_configuration=json_token_type_configuration,
                jwt_token_type_configuration=jwt_token_type_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_token_type_configuration: Optional[JsonTokenTypeConfiguration] = core.arg(default=None)

        jwt_token_type_configuration: Optional[JwtTokenTypeConfiguration] = core.arg(default=None)


@core.schema
class UserGroupResolutionConfiguration(core.Schema):

    user_group_resolution_mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        user_group_resolution_mode: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserGroupResolutionConfiguration.Args(
                user_group_resolution_mode=user_group_resolution_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        user_group_resolution_mode: Union[str, core.StringOut] = core.arg()


@core.schema
class TextDocumentStatistics(core.Schema):

    indexed_text_bytes: Union[int, core.IntOut] = core.attr(int, computed=True)

    indexed_text_documents_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        indexed_text_bytes: Union[int, core.IntOut],
        indexed_text_documents_count: Union[int, core.IntOut],
    ):
        super().__init__(
            args=TextDocumentStatistics.Args(
                indexed_text_bytes=indexed_text_bytes,
                indexed_text_documents_count=indexed_text_documents_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        indexed_text_bytes: Union[int, core.IntOut] = core.arg()

        indexed_text_documents_count: Union[int, core.IntOut] = core.arg()


@core.schema
class FaqStatistics(core.Schema):

    indexed_question_answers_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        indexed_question_answers_count: Union[int, core.IntOut],
    ):
        super().__init__(
            args=FaqStatistics.Args(
                indexed_question_answers_count=indexed_question_answers_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        indexed_question_answers_count: Union[int, core.IntOut] = core.arg()


@core.schema
class IndexStatistics(core.Schema):

    faq_statistics: Union[List[FaqStatistics], core.ArrayOut[FaqStatistics]] = core.attr(
        FaqStatistics, computed=True, kind=core.Kind.array
    )

    text_document_statistics: Union[
        List[TextDocumentStatistics], core.ArrayOut[TextDocumentStatistics]
    ] = core.attr(TextDocumentStatistics, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        faq_statistics: Union[List[FaqStatistics], core.ArrayOut[FaqStatistics]],
        text_document_statistics: Union[
            List[TextDocumentStatistics], core.ArrayOut[TextDocumentStatistics]
        ],
    ):
        super().__init__(
            args=IndexStatistics.Args(
                faq_statistics=faq_statistics,
                text_document_statistics=text_document_statistics,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        faq_statistics: Union[List[FaqStatistics], core.ArrayOut[FaqStatistics]] = core.arg()

        text_document_statistics: Union[
            List[TextDocumentStatistics], core.ArrayOut[TextDocumentStatistics]
        ] = core.arg()


@core.resource(type="aws_kendra_index", namespace="aws_kendra")
class Index(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity_units: Optional[CapacityUnits] = core.attr(CapacityUnits, default=None, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_metadata_configuration_updates: Optional[
        Union[
            List[DocumentMetadataConfigurationUpdates],
            core.ArrayOut[DocumentMetadataConfigurationUpdates],
        ]
    ] = core.attr(
        DocumentMetadataConfigurationUpdates, default=None, computed=True, kind=core.Kind.array
    )

    edition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_statistics: Union[List[IndexStatistics], core.ArrayOut[IndexStatistics]] = core.attr(
        IndexStatistics, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    server_side_encryption_configuration: Optional[ServerSideEncryptionConfiguration] = core.attr(
        ServerSideEncryptionConfiguration, default=None
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_context_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_group_resolution_configuration: Optional[UserGroupResolutionConfiguration] = core.attr(
        UserGroupResolutionConfiguration, default=None
    )

    user_token_configurations: Optional[UserTokenConfigurations] = core.attr(
        UserTokenConfigurations, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        capacity_units: Optional[CapacityUnits] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        document_metadata_configuration_updates: Optional[
            Union[
                List[DocumentMetadataConfigurationUpdates],
                core.ArrayOut[DocumentMetadataConfigurationUpdates],
            ]
        ] = None,
        edition: Optional[Union[str, core.StringOut]] = None,
        server_side_encryption_configuration: Optional[ServerSideEncryptionConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_context_policy: Optional[Union[str, core.StringOut]] = None,
        user_group_resolution_configuration: Optional[UserGroupResolutionConfiguration] = None,
        user_token_configurations: Optional[UserTokenConfigurations] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Index.Args(
                name=name,
                role_arn=role_arn,
                capacity_units=capacity_units,
                description=description,
                document_metadata_configuration_updates=document_metadata_configuration_updates,
                edition=edition,
                server_side_encryption_configuration=server_side_encryption_configuration,
                tags=tags,
                tags_all=tags_all,
                user_context_policy=user_context_policy,
                user_group_resolution_configuration=user_group_resolution_configuration,
                user_token_configurations=user_token_configurations,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_units: Optional[CapacityUnits] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_metadata_configuration_updates: Optional[
            Union[
                List[DocumentMetadataConfigurationUpdates],
                core.ArrayOut[DocumentMetadataConfigurationUpdates],
            ]
        ] = core.arg(default=None)

        edition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        server_side_encryption_configuration: Optional[
            ServerSideEncryptionConfiguration
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_context_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_group_resolution_configuration: Optional[UserGroupResolutionConfiguration] = core.arg(
            default=None
        )

        user_token_configurations: Optional[UserTokenConfigurations] = core.arg(default=None)
