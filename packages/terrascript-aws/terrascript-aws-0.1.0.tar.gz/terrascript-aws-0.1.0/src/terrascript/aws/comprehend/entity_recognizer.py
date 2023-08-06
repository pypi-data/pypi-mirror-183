from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EntityTypes(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EntityTypes.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Annotations(core.Schema):

    s3_uri: Union[str, core.StringOut] = core.attr(str)

    test_s3_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_uri: Union[str, core.StringOut],
        test_s3_uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Annotations.Args(
                s3_uri=s3_uri,
                test_s3_uri=test_s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_uri: Union[str, core.StringOut] = core.arg()

        test_s3_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AugmentedManifests(core.Schema):

    annotation_data_s3_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    attribute_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    document_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_uri: Union[str, core.StringOut] = core.attr(str)

    source_documents_s3_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    split: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        attribute_names: Union[List[str], core.ArrayOut[core.StringOut]],
        s3_uri: Union[str, core.StringOut],
        annotation_data_s3_uri: Optional[Union[str, core.StringOut]] = None,
        document_type: Optional[Union[str, core.StringOut]] = None,
        source_documents_s3_uri: Optional[Union[str, core.StringOut]] = None,
        split: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AugmentedManifests.Args(
                attribute_names=attribute_names,
                s3_uri=s3_uri,
                annotation_data_s3_uri=annotation_data_s3_uri,
                document_type=document_type,
                source_documents_s3_uri=source_documents_s3_uri,
                split=split,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        annotation_data_s3_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        attribute_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        document_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_uri: Union[str, core.StringOut] = core.arg()

        source_documents_s3_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        split: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Documents(core.Schema):

    input_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_uri: Union[str, core.StringOut] = core.attr(str)

    test_s3_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_uri: Union[str, core.StringOut],
        input_format: Optional[Union[str, core.StringOut]] = None,
        test_s3_uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Documents.Args(
                s3_uri=s3_uri,
                input_format=input_format,
                test_s3_uri=test_s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_uri: Union[str, core.StringOut] = core.arg()

        test_s3_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EntityList(core.Schema):

    s3_uri: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_uri: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EntityList.Args(
                s3_uri=s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_uri: Union[str, core.StringOut] = core.arg()


@core.schema
class InputDataConfig(core.Schema):

    annotations: Optional[Annotations] = core.attr(Annotations, default=None)

    augmented_manifests: Optional[
        Union[List[AugmentedManifests], core.ArrayOut[AugmentedManifests]]
    ] = core.attr(AugmentedManifests, default=None, kind=core.Kind.array)

    data_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    documents: Optional[Documents] = core.attr(Documents, default=None)

    entity_list: Optional[EntityList] = core.attr(EntityList, default=None)

    entity_types: Union[List[EntityTypes], core.ArrayOut[EntityTypes]] = core.attr(
        EntityTypes, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        entity_types: Union[List[EntityTypes], core.ArrayOut[EntityTypes]],
        annotations: Optional[Annotations] = None,
        augmented_manifests: Optional[
            Union[List[AugmentedManifests], core.ArrayOut[AugmentedManifests]]
        ] = None,
        data_format: Optional[Union[str, core.StringOut]] = None,
        documents: Optional[Documents] = None,
        entity_list: Optional[EntityList] = None,
    ):
        super().__init__(
            args=InputDataConfig.Args(
                entity_types=entity_types,
                annotations=annotations,
                augmented_manifests=augmented_manifests,
                data_format=data_format,
                documents=documents,
                entity_list=entity_list,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        annotations: Optional[Annotations] = core.arg(default=None)

        augmented_manifests: Optional[
            Union[List[AugmentedManifests], core.ArrayOut[AugmentedManifests]]
        ] = core.arg(default=None)

        data_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        documents: Optional[Documents] = core.arg(default=None)

        entity_list: Optional[EntityList] = core.arg(default=None)

        entity_types: Union[List[EntityTypes], core.ArrayOut[EntityTypes]] = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnets=subnets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_comprehend_entity_recognizer", namespace="aws_comprehend")
class EntityRecognizer(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_access_role_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_data_config: InputDataConfig = core.attr(InputDataConfig)

    language_code: Union[str, core.StringOut] = core.attr(str)

    model_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    version_name_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    volume_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        data_access_role_arn: Union[str, core.StringOut],
        input_data_config: InputDataConfig,
        language_code: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        model_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        version_name: Optional[Union[str, core.StringOut]] = None,
        version_name_prefix: Optional[Union[str, core.StringOut]] = None,
        volume_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        vpc_config: Optional[VpcConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EntityRecognizer.Args(
                data_access_role_arn=data_access_role_arn,
                input_data_config=input_data_config,
                language_code=language_code,
                name=name,
                model_kms_key_id=model_kms_key_id,
                tags=tags,
                tags_all=tags_all,
                version_name=version_name,
                version_name_prefix=version_name_prefix,
                volume_kms_key_id=volume_kms_key_id,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data_access_role_arn: Union[str, core.StringOut] = core.arg()

        input_data_config: InputDataConfig = core.arg()

        language_code: Union[str, core.StringOut] = core.arg()

        model_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        version_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version_name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        volume_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_config: Optional[VpcConfig] = core.arg(default=None)
