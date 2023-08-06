from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_route53_resolver_rule", namespace="aws_route53_resolver")
class DsRule(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resolver_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    resolver_rule_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    rule_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    share_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        resolver_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        resolver_rule_id: Optional[Union[str, core.StringOut]] = None,
        rule_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRule.Args(
                domain_name=domain_name,
                name=name,
                resolver_endpoint_id=resolver_endpoint_id,
                resolver_rule_id=resolver_rule_id,
                rule_type=rule_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resolver_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resolver_rule_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
