from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InsightsConfiguration(core.Schema):

    insights_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    notifications_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        *,
        insights_enabled: Union[bool, core.BoolOut],
        notifications_enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=InsightsConfiguration.Args(
                insights_enabled=insights_enabled,
                notifications_enabled=notifications_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insights_enabled: Union[bool, core.BoolOut] = core.arg()

        notifications_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_xray_group", namespace="aws_x_ray")
class XrayGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter_expression: Union[str, core.StringOut] = core.attr(str)

    group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    insights_configuration: Optional[InsightsConfiguration] = core.attr(
        InsightsConfiguration, default=None, computed=True
    )

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
        filter_expression: Union[str, core.StringOut],
        group_name: Union[str, core.StringOut],
        insights_configuration: Optional[InsightsConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=XrayGroup.Args(
                filter_expression=filter_expression,
                group_name=group_name,
                insights_configuration=insights_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        filter_expression: Union[str, core.StringOut] = core.arg()

        group_name: Union[str, core.StringOut] = core.arg()

        insights_configuration: Optional[InsightsConfiguration] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
