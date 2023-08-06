from typing import Union

import terrascript.core as core


@core.data(type="aws_wafv2_rule_group", namespace="aws_waf")
class DsV2RuleGroup(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    scope: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsV2RuleGroup.Args(
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()
