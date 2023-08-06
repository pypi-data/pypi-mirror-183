from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appconfig_deployment_strategy", namespace="aws_appconfig")
class DeploymentStrategy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_duration_in_minutes: Union[int, core.IntOut] = core.attr(int)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    final_bake_time_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    growth_factor: Union[float, core.FloatOut] = core.attr(float)

    growth_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    replicate_to: Union[str, core.StringOut] = core.attr(str)

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
        deployment_duration_in_minutes: Union[int, core.IntOut],
        growth_factor: Union[float, core.FloatOut],
        name: Union[str, core.StringOut],
        replicate_to: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        final_bake_time_in_minutes: Optional[Union[int, core.IntOut]] = None,
        growth_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeploymentStrategy.Args(
                deployment_duration_in_minutes=deployment_duration_in_minutes,
                growth_factor=growth_factor,
                name=name,
                replicate_to=replicate_to,
                description=description,
                final_bake_time_in_minutes=final_bake_time_in_minutes,
                growth_type=growth_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deployment_duration_in_minutes: Union[int, core.IntOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_bake_time_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        growth_factor: Union[float, core.FloatOut] = core.arg()

        growth_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        replicate_to: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
