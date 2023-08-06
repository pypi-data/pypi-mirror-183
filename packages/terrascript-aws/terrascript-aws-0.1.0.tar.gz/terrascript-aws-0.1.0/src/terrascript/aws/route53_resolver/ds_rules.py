from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_route53_resolver_rules", namespace="aws_route53_resolver")
class DsRules(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resolver_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resolver_rule_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    rule_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    share_status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: Optional[Union[str, core.StringOut]] = None,
        owner_id: Optional[Union[str, core.StringOut]] = None,
        resolver_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        rule_type: Optional[Union[str, core.StringOut]] = None,
        share_status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRules.Args(
                name_regex=name_regex,
                owner_id=owner_id,
                resolver_endpoint_id=resolver_endpoint_id,
                rule_type=rule_type,
                share_status=share_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resolver_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        share_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)
