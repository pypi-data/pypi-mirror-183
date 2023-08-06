from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class FieldPatterns(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=FieldPatterns.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Items(core.Schema):

    field_patterns: FieldPatterns = core.attr(FieldPatterns)

    provider_id: Union[str, core.StringOut] = core.attr(str)

    public_key_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        field_patterns: FieldPatterns,
        provider_id: Union[str, core.StringOut],
        public_key_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Items.Args(
                field_patterns=field_patterns,
                provider_id=provider_id,
                public_key_id=public_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_patterns: FieldPatterns = core.arg()

        provider_id: Union[str, core.StringOut] = core.arg()

        public_key_id: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptionEntities(core.Schema):

    items: Optional[Union[List[Items], core.ArrayOut[Items]]] = core.attr(
        Items, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[Items], core.ArrayOut[Items]]] = None,
    ):
        super().__init__(
            args=EncryptionEntities.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[Items], core.ArrayOut[Items]]] = core.arg(default=None)


@core.resource(type="aws_cloudfront_field_level_encryption_profile", namespace="aws_cloudfront")
class FieldLevelEncryptionProfile(core.Resource):

    caller_reference: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_entities: EncryptionEntities = core.attr(EncryptionEntities)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        encryption_entities: EncryptionEntities,
        name: Union[str, core.StringOut],
        comment: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FieldLevelEncryptionProfile.Args(
                encryption_entities=encryption_entities,
                name=name,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_entities: EncryptionEntities = core.arg()

        name: Union[str, core.StringOut] = core.arg()
