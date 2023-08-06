from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Options(core.Schema):

    ipv6_support: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        ipv6_support: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=Options.Args(
                ipv6_support=ipv6_support,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ipv6_support: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_networkmanager_vpc_attachment", namespace="aws_networkmanager")
class VpcAttachment(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attachment_policy_rule_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    attachment_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_id: Union[str, core.StringOut] = core.attr(str)

    edge_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    options: Optional[Options] = core.attr(Options, default=None)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    segment_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        core_network_id: Union[str, core.StringOut],
        subnet_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_arn: Union[str, core.StringOut],
        options: Optional[Options] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VpcAttachment.Args(
                core_network_id=core_network_id,
                subnet_arns=subnet_arns,
                vpc_arn=vpc_arn,
                options=options,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        core_network_id: Union[str, core.StringOut] = core.arg()

        options: Optional[Options] = core.arg(default=None)

        subnet_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_arn: Union[str, core.StringOut] = core.arg()
