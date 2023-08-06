from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_wafregional_subscribed_rule_group", namespace="aws_wafregional")
class DsSubscribedRuleGroup(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    metric_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        metric_name: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubscribedRuleGroup.Args(
                metric_name=metric_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
