from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_applicationinsights_application", namespace="aws_applicationinsights")
class Application(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_config_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    auto_create: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cwe_monitor_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    grouping_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ops_center_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ops_item_sns_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_group_name: Union[str, core.StringOut] = core.attr(str)

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
        resource_group_name: Union[str, core.StringOut],
        auto_config_enabled: Optional[Union[bool, core.BoolOut]] = None,
        auto_create: Optional[Union[bool, core.BoolOut]] = None,
        cwe_monitor_enabled: Optional[Union[bool, core.BoolOut]] = None,
        grouping_type: Optional[Union[str, core.StringOut]] = None,
        ops_center_enabled: Optional[Union[bool, core.BoolOut]] = None,
        ops_item_sns_topic_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                resource_group_name=resource_group_name,
                auto_config_enabled=auto_config_enabled,
                auto_create=auto_create,
                cwe_monitor_enabled=cwe_monitor_enabled,
                grouping_type=grouping_type,
                ops_center_enabled=ops_center_enabled,
                ops_item_sns_topic_arn=ops_item_sns_topic_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_config_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        auto_create: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cwe_monitor_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        grouping_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ops_center_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ops_item_sns_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_group_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
