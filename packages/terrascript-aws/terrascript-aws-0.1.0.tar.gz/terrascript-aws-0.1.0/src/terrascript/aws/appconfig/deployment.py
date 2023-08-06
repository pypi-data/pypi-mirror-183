from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appconfig_deployment", namespace="aws_appconfig")
class Deployment(core.Resource):

    application_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration_profile_id: Union[str, core.StringOut] = core.attr(str)

    configuration_version: Union[str, core.StringOut] = core.attr(str)

    deployment_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    deployment_strategy_id: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    environment_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: Union[str, core.StringOut],
        configuration_profile_id: Union[str, core.StringOut],
        configuration_version: Union[str, core.StringOut],
        deployment_strategy_id: Union[str, core.StringOut],
        environment_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                application_id=application_id,
                configuration_profile_id=configuration_profile_id,
                configuration_version=configuration_version,
                deployment_strategy_id=deployment_strategy_id,
                environment_id=environment_id,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        configuration_profile_id: Union[str, core.StringOut] = core.arg()

        configuration_version: Union[str, core.StringOut] = core.arg()

        deployment_strategy_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
