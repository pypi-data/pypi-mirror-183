from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appconfig_hosted_configuration_version", namespace="aws_appconfig")
class HostedConfigurationVersion(core.Resource):

    application_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration_profile_id: Union[str, core.StringOut] = core.attr(str)

    content: Union[str, core.StringOut] = core.attr(str)

    content_type: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    version_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: Union[str, core.StringOut],
        configuration_profile_id: Union[str, core.StringOut],
        content: Union[str, core.StringOut],
        content_type: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=HostedConfigurationVersion.Args(
                application_id=application_id,
                configuration_profile_id=configuration_profile_id,
                content=content,
                content_type=content_type,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        configuration_profile_id: Union[str, core.StringOut] = core.arg()

        content: Union[str, core.StringOut] = core.arg()

        content_type: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)
