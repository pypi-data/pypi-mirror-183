from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class QueryArgProfilesItems(core.Schema):

    profile_id: Union[str, core.StringOut] = core.attr(str)

    query_arg: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        profile_id: Union[str, core.StringOut],
        query_arg: Union[str, core.StringOut],
    ):
        super().__init__(
            args=QueryArgProfilesItems.Args(
                profile_id=profile_id,
                query_arg=query_arg,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        profile_id: Union[str, core.StringOut] = core.arg()

        query_arg: Union[str, core.StringOut] = core.arg()


@core.schema
class QueryArgProfiles(core.Schema):

    items: Optional[
        Union[List[QueryArgProfilesItems], core.ArrayOut[QueryArgProfilesItems]]
    ] = core.attr(QueryArgProfilesItems, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        items: Optional[
            Union[List[QueryArgProfilesItems], core.ArrayOut[QueryArgProfilesItems]]
        ] = None,
    ):
        super().__init__(
            args=QueryArgProfiles.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[
            Union[List[QueryArgProfilesItems], core.ArrayOut[QueryArgProfilesItems]]
        ] = core.arg(default=None)


@core.schema
class QueryArgProfileConfig(core.Schema):

    forward_when_query_arg_profile_is_unknown: Union[bool, core.BoolOut] = core.attr(bool)

    query_arg_profiles: Optional[QueryArgProfiles] = core.attr(QueryArgProfiles, default=None)

    def __init__(
        self,
        *,
        forward_when_query_arg_profile_is_unknown: Union[bool, core.BoolOut],
        query_arg_profiles: Optional[QueryArgProfiles] = None,
    ):
        super().__init__(
            args=QueryArgProfileConfig.Args(
                forward_when_query_arg_profile_is_unknown=forward_when_query_arg_profile_is_unknown,
                query_arg_profiles=query_arg_profiles,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        forward_when_query_arg_profile_is_unknown: Union[bool, core.BoolOut] = core.arg()

        query_arg_profiles: Optional[QueryArgProfiles] = core.arg(default=None)


@core.schema
class ContentTypeProfilesItems(core.Schema):

    content_type: Union[str, core.StringOut] = core.attr(str)

    format: Union[str, core.StringOut] = core.attr(str)

    profile_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        content_type: Union[str, core.StringOut],
        format: Union[str, core.StringOut],
        profile_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ContentTypeProfilesItems.Args(
                content_type=content_type,
                format=format,
                profile_id=profile_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_type: Union[str, core.StringOut] = core.arg()

        format: Union[str, core.StringOut] = core.arg()

        profile_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ContentTypeProfiles(core.Schema):

    items: Union[
        List[ContentTypeProfilesItems], core.ArrayOut[ContentTypeProfilesItems]
    ] = core.attr(ContentTypeProfilesItems, kind=core.Kind.array)

    def __init__(
        self,
        *,
        items: Union[List[ContentTypeProfilesItems], core.ArrayOut[ContentTypeProfilesItems]],
    ):
        super().__init__(
            args=ContentTypeProfiles.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[
            List[ContentTypeProfilesItems], core.ArrayOut[ContentTypeProfilesItems]
        ] = core.arg()


@core.schema
class ContentTypeProfileConfig(core.Schema):

    content_type_profiles: ContentTypeProfiles = core.attr(ContentTypeProfiles)

    forward_when_content_type_is_unknown: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        content_type_profiles: ContentTypeProfiles,
        forward_when_content_type_is_unknown: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ContentTypeProfileConfig.Args(
                content_type_profiles=content_type_profiles,
                forward_when_content_type_is_unknown=forward_when_content_type_is_unknown,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_type_profiles: ContentTypeProfiles = core.arg()

        forward_when_content_type_is_unknown: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_cloudfront_field_level_encryption_config", namespace="aws_cloudfront")
class FieldLevelEncryptionConfig(core.Resource):

    caller_reference: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_type_profile_config: ContentTypeProfileConfig = core.attr(ContentTypeProfileConfig)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    query_arg_profile_config: QueryArgProfileConfig = core.attr(QueryArgProfileConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        content_type_profile_config: ContentTypeProfileConfig,
        query_arg_profile_config: QueryArgProfileConfig,
        comment: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FieldLevelEncryptionConfig.Args(
                content_type_profile_config=content_type_profile_config,
                query_arg_profile_config=query_arg_profile_config,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_type_profile_config: ContentTypeProfileConfig = core.arg()

        query_arg_profile_config: QueryArgProfileConfig = core.arg()
