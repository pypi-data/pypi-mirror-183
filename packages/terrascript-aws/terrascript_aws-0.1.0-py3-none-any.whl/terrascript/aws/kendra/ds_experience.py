from typing import List, Union

import terrascript.core as core


@core.schema
class Endpoints(core.Schema):

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint: Union[str, core.StringOut],
        endpoint_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Endpoints.Args(
                endpoint=endpoint,
                endpoint_type=endpoint_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: Union[str, core.StringOut] = core.arg()

        endpoint_type: Union[str, core.StringOut] = core.arg()


@core.schema
class ContentSourceConfiguration(core.Schema):

    data_source_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    direct_put_content: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    faq_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        data_source_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        direct_put_content: Union[bool, core.BoolOut],
        faq_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ContentSourceConfiguration.Args(
                data_source_ids=data_source_ids,
                direct_put_content=direct_put_content,
                faq_ids=faq_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_source_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        direct_put_content: Union[bool, core.BoolOut] = core.arg()

        faq_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class UserIdentityConfiguration(core.Schema):

    identity_attribute_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        identity_attribute_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserIdentityConfiguration.Args(
                identity_attribute_name=identity_attribute_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identity_attribute_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Configuration(core.Schema):

    content_source_configuration: Union[
        List[ContentSourceConfiguration], core.ArrayOut[ContentSourceConfiguration]
    ] = core.attr(ContentSourceConfiguration, computed=True, kind=core.Kind.array)

    user_identity_configuration: Union[
        List[UserIdentityConfiguration], core.ArrayOut[UserIdentityConfiguration]
    ] = core.attr(UserIdentityConfiguration, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        content_source_configuration: Union[
            List[ContentSourceConfiguration], core.ArrayOut[ContentSourceConfiguration]
        ],
        user_identity_configuration: Union[
            List[UserIdentityConfiguration], core.ArrayOut[UserIdentityConfiguration]
        ],
    ):
        super().__init__(
            args=Configuration.Args(
                content_source_configuration=content_source_configuration,
                user_identity_configuration=user_identity_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_source_configuration: Union[
            List[ContentSourceConfiguration], core.ArrayOut[ContentSourceConfiguration]
        ] = core.arg()

        user_identity_configuration: Union[
            List[UserIdentityConfiguration], core.ArrayOut[UserIdentityConfiguration]
        ] = core.arg()


@core.data(type="aws_kendra_experience", namespace="aws_kendra")
class DsExperience(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration: Union[List[Configuration], core.ArrayOut[Configuration]] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoints: Union[List[Endpoints], core.ArrayOut[Endpoints]] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    experience_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        experience_id: Union[str, core.StringOut],
        index_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsExperience.Args(
                experience_id=experience_id,
                index_id=index_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        experience_id: Union[str, core.StringOut] = core.arg()

        index_id: Union[str, core.StringOut] = core.arg()
