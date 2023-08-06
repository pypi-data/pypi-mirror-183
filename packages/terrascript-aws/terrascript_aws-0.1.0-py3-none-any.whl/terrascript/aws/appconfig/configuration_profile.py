from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Validator(core.Schema):

    content: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        content: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Validator.Args(
                type=type,
                content=content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_appconfig_configuration_profile", namespace="aws_appconfig")
class ConfigurationProfile(core.Resource):

    application_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration_profile_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location_uri: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    retrieval_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    validator: Optional[Union[List[Validator], core.ArrayOut[Validator]]] = core.attr(
        Validator, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: Union[str, core.StringOut],
        location_uri: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        retrieval_role_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        validator: Optional[Union[List[Validator], core.ArrayOut[Validator]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationProfile.Args(
                application_id=application_id,
                location_uri=location_uri,
                name=name,
                description=description,
                retrieval_role_arn=retrieval_role_arn,
                tags=tags,
                tags_all=tags_all,
                type=type,
                validator=validator,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location_uri: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        retrieval_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        validator: Optional[Union[List[Validator], core.ArrayOut[Validator]]] = core.arg(
            default=None
        )
