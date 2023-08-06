from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ContentSourceConfiguration(core.Schema):

    data_source_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    direct_put_content: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    faq_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        data_source_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        direct_put_content: Optional[Union[bool, core.BoolOut]] = None,
        faq_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
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
        data_source_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        direct_put_content: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        faq_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class UserIdentityConfiguration(core.Schema):

    identity_attribute_name: Union[str, core.StringOut] = core.attr(str)

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

    content_source_configuration: Optional[ContentSourceConfiguration] = core.attr(
        ContentSourceConfiguration, default=None, computed=True
    )

    user_identity_configuration: Optional[UserIdentityConfiguration] = core.attr(
        UserIdentityConfiguration, default=None
    )

    def __init__(
        self,
        *,
        content_source_configuration: Optional[ContentSourceConfiguration] = None,
        user_identity_configuration: Optional[UserIdentityConfiguration] = None,
    ):
        super().__init__(
            args=Configuration.Args(
                content_source_configuration=content_source_configuration,
                user_identity_configuration=user_identity_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_source_configuration: Optional[ContentSourceConfiguration] = core.arg(default=None)

        user_identity_configuration: Optional[UserIdentityConfiguration] = core.arg(default=None)


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


@core.resource(type="aws_kendra_experience", namespace="aws_kendra")
class Experience(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration: Optional[Configuration] = core.attr(Configuration, default=None, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoints: Union[List[Endpoints], core.ArrayOut[Endpoints]] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    experience_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        configuration: Optional[Configuration] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Experience.Args(
                index_id=index_id,
                name=name,
                role_arn=role_arn,
                configuration=configuration,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Optional[Configuration] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()
