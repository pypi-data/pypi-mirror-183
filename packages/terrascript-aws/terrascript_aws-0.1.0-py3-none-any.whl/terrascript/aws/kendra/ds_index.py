from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class JsonTokenTypeConfiguration(core.Schema):

    group_attribute_field: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_name_attribute_field: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    claim_regex: Union[str, core.StringOut] = core.attr(str, computed=True)

    group_attribute_field: Union[str, core.StringOut] = core.attr(str, computed=True)

    issuer: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    secrets_manager_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_name_attribute_field: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        claim_regex: Union[str, core.StringOut],
        group_attribute_field: Union[str, core.StringOut],
        issuer: Union[str, core.StringOut],
        key_location: Union[str, core.StringOut],
        secrets_manager_arn: Union[str, core.StringOut],
        url: Union[str, core.StringOut],
        user_name_attribute_field: Union[str, core.StringOut],
    ):
        super().__init__(
            args=JwtTokenTypeConfiguration.Args(
                claim_regex=claim_regex,
                group_attribute_field=group_attribute_field,
                issuer=issuer,
                key_location=key_location,
                secrets_manager_arn=secrets_manager_arn,
                url=url,
                user_name_attribute_field=user_name_attribute_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        claim_regex: Union[str, core.StringOut] = core.arg()

        group_attribute_field: Union[str, core.StringOut] = core.arg()

        issuer: Union[str, core.StringOut] = core.arg()

        key_location: Union[str, core.StringOut] = core.arg()

        secrets_manager_arn: Union[str, core.StringOut] = core.arg()

        url: Union[str, core.StringOut] = core.arg()

        user_name_attribute_field: Union[str, core.StringOut] = core.arg()


@core.schema
class UserTokenConfigurations(core.Schema):

    json_token_type_configuration: Union[
        List[JsonTokenTypeConfiguration], core.ArrayOut[JsonTokenTypeConfiguration]
    ] = core.attr(JsonTokenTypeConfiguration, computed=True, kind=core.Kind.array)

    jwt_token_type_configuration: Union[
        List[JwtTokenTypeConfiguration], core.ArrayOut[JwtTokenTypeConfiguration]
    ] = core.attr(JwtTokenTypeConfiguration, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        json_token_type_configuration: Union[
            List[JsonTokenTypeConfiguration], core.ArrayOut[JsonTokenTypeConfiguration]
        ],
        jwt_token_type_configuration: Union[
            List[JwtTokenTypeConfiguration], core.ArrayOut[JwtTokenTypeConfiguration]
        ],
    ):
        super().__init__(
            args=UserTokenConfigurations.Args(
                json_token_type_configuration=json_token_type_configuration,
                jwt_token_type_configuration=jwt_token_type_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_token_type_configuration: Union[
            List[JsonTokenTypeConfiguration], core.ArrayOut[JsonTokenTypeConfiguration]
        ] = core.arg()

        jwt_token_type_configuration: Union[
            List[JwtTokenTypeConfiguration], core.ArrayOut[JwtTokenTypeConfiguration]
        ] = core.arg()


@core.schema
class CapacityUnits(core.Schema):

    query_capacity_units: Union[int, core.IntOut] = core.attr(int, computed=True)

    storage_capacity_units: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        query_capacity_units: Union[int, core.IntOut],
        storage_capacity_units: Union[int, core.IntOut],
    ):
        super().__init__(
            args=CapacityUnits.Args(
                query_capacity_units=query_capacity_units,
                storage_capacity_units=storage_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query_capacity_units: Union[int, core.IntOut] = core.arg()

        storage_capacity_units: Union[int, core.IntOut] = core.arg()


@core.schema
class Relevance(core.Schema):

    duration: Union[str, core.StringOut] = core.attr(str, computed=True)

    freshness: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    importance: Union[int, core.IntOut] = core.attr(int, computed=True)

    rank_order: Union[str, core.StringOut] = core.attr(str, computed=True)

    values_importance_map: Union[Dict[str, int], core.MapOut[core.IntOut]] = core.attr(
        int, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        duration: Union[str, core.StringOut],
        freshness: Union[bool, core.BoolOut],
        importance: Union[int, core.IntOut],
        rank_order: Union[str, core.StringOut],
        values_importance_map: Union[Dict[str, int], core.MapOut[core.IntOut]],
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
        duration: Union[str, core.StringOut] = core.arg()

        freshness: Union[bool, core.BoolOut] = core.arg()

        importance: Union[int, core.IntOut] = core.arg()

        rank_order: Union[str, core.StringOut] = core.arg()

        values_importance_map: Union[Dict[str, int], core.MapOut[core.IntOut]] = core.arg()


@core.schema
class Search(core.Schema):

    displayable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    facetable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    searchable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    sortable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        displayable: Union[bool, core.BoolOut],
        facetable: Union[bool, core.BoolOut],
        searchable: Union[bool, core.BoolOut],
        sortable: Union[bool, core.BoolOut],
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
        displayable: Union[bool, core.BoolOut] = core.arg()

        facetable: Union[bool, core.BoolOut] = core.arg()

        searchable: Union[bool, core.BoolOut] = core.arg()

        sortable: Union[bool, core.BoolOut] = core.arg()


@core.schema
class DocumentMetadataConfigurationUpdates(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    relevance: Union[List[Relevance], core.ArrayOut[Relevance]] = core.attr(
        Relevance, computed=True, kind=core.Kind.array
    )

    search: Union[List[Search], core.ArrayOut[Search]] = core.attr(
        Search, computed=True, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        relevance: Union[List[Relevance], core.ArrayOut[Relevance]],
        search: Union[List[Search], core.ArrayOut[Search]],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DocumentMetadataConfigurationUpdates.Args(
                name=name,
                relevance=relevance,
                search=search,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        relevance: Union[List[Relevance], core.ArrayOut[Relevance]] = core.arg()

        search: Union[List[Search], core.ArrayOut[Search]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ServerSideEncryptionConfiguration(core.Schema):

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        kms_key_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ServerSideEncryptionConfiguration.Args(
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Union[str, core.StringOut] = core.arg()


@core.schema
class UserGroupResolutionConfiguration(core.Schema):

    user_group_resolution_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_kendra_index", namespace="aws_kendra")
class DsIndex(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity_units: Union[List[CapacityUnits], core.ArrayOut[CapacityUnits]] = core.attr(
        CapacityUnits, computed=True, kind=core.Kind.array
    )

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    document_metadata_configuration_updates: Union[
        List[DocumentMetadataConfigurationUpdates],
        core.ArrayOut[DocumentMetadataConfigurationUpdates],
    ] = core.attr(DocumentMetadataConfigurationUpdates, computed=True, kind=core.Kind.array)

    edition: Union[str, core.StringOut] = core.attr(str, computed=True)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    index_statistics: Union[List[IndexStatistics], core.ArrayOut[IndexStatistics]] = core.attr(
        IndexStatistics, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    server_side_encryption_configuration: Union[
        List[ServerSideEncryptionConfiguration], core.ArrayOut[ServerSideEncryptionConfiguration]
    ] = core.attr(ServerSideEncryptionConfiguration, computed=True, kind=core.Kind.array)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_context_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_group_resolution_configuration: Union[
        List[UserGroupResolutionConfiguration], core.ArrayOut[UserGroupResolutionConfiguration]
    ] = core.attr(UserGroupResolutionConfiguration, computed=True, kind=core.Kind.array)

    user_token_configurations: Union[
        List[UserTokenConfigurations], core.ArrayOut[UserTokenConfigurations]
    ] = core.attr(UserTokenConfigurations, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsIndex.Args(
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
