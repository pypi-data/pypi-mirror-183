from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ResourceSpec(core.Schema):

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lifecycle_config_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemaker_image_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    sagemaker_image_version_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        lifecycle_config_arn: Optional[Union[str, core.StringOut]] = None,
        sagemaker_image_arn: Optional[Union[str, core.StringOut]] = None,
        sagemaker_image_version_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ResourceSpec.Args(
                instance_type=instance_type,
                lifecycle_config_arn=lifecycle_config_arn,
                sagemaker_image_arn=sagemaker_image_arn,
                sagemaker_image_version_arn=sagemaker_image_version_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lifecycle_config_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemaker_image_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemaker_image_version_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sagemaker_app", namespace="aws_sagemaker")
class App(core.Resource):

    app_name: Union[str, core.StringOut] = core.attr(str)

    app_type: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_spec: Optional[ResourceSpec] = core.attr(ResourceSpec, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_profile_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        app_name: Union[str, core.StringOut],
        app_type: Union[str, core.StringOut],
        domain_id: Union[str, core.StringOut],
        user_profile_name: Union[str, core.StringOut],
        resource_spec: Optional[ResourceSpec] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=App.Args(
                app_name=app_name,
                app_type=app_type,
                domain_id=domain_id,
                user_profile_name=user_profile_name,
                resource_spec=resource_spec,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_name: Union[str, core.StringOut] = core.arg()

        app_type: Union[str, core.StringOut] = core.arg()

        domain_id: Union[str, core.StringOut] = core.arg()

        resource_spec: Optional[ResourceSpec] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_profile_name: Union[str, core.StringOut] = core.arg()
