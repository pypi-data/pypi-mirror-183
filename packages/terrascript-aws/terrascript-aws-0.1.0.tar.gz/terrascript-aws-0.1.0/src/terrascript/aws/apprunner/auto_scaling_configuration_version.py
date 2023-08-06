from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apprunner_auto_scaling_configuration_version", namespace="aws_apprunner")
class AutoScalingConfigurationVersion(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_scaling_configuration_name: Union[str, core.StringOut] = core.attr(str)

    auto_scaling_configuration_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    max_concurrency: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        auto_scaling_configuration_name: Union[str, core.StringOut],
        max_concurrency: Optional[Union[int, core.IntOut]] = None,
        max_size: Optional[Union[int, core.IntOut]] = None,
        min_size: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AutoScalingConfigurationVersion.Args(
                auto_scaling_configuration_name=auto_scaling_configuration_name,
                max_concurrency=max_concurrency,
                max_size=max_size,
                min_size=min_size,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_configuration_name: Union[str, core.StringOut] = core.arg()

        max_concurrency: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
