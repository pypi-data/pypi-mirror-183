from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Vpc(core.Schema):

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    vpc_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        vpc_id: Union[str, core.StringOut],
        vpc_region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Vpc.Args(
                vpc_id=vpc_id,
                vpc_region=vpc_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_id: Union[str, core.StringOut] = core.arg()

        vpc_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_route53_zone", namespace="aws_route53")
class Zone(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    delegation_set_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    name_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc: Optional[Union[List[Vpc], core.ArrayOut[Vpc]]] = core.attr(
        Vpc, default=None, kind=core.Kind.array
    )

    zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        comment: Optional[Union[str, core.StringOut]] = None,
        delegation_set_id: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc: Optional[Union[List[Vpc], core.ArrayOut[Vpc]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Zone.Args(
                name=name,
                comment=comment,
                delegation_set_id=delegation_set_id,
                force_destroy=force_destroy,
                tags=tags,
                tags_all=tags_all,
                vpc=vpc,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delegation_set_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc: Optional[Union[List[Vpc], core.ArrayOut[Vpc]]] = core.arg(default=None)
