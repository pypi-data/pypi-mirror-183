from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class NlbResource(core.Schema):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NlbResource.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class R53Resource(core.Schema):

    domain_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    record_set_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        domain_name: Optional[Union[str, core.StringOut]] = None,
        record_set_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=R53Resource.Args(
                domain_name=domain_name,
                record_set_id=record_set_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        record_set_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TargetResource(core.Schema):

    nlb_resource: Optional[NlbResource] = core.attr(NlbResource, default=None)

    r53_resource: Optional[R53Resource] = core.attr(R53Resource, default=None)

    def __init__(
        self,
        *,
        nlb_resource: Optional[NlbResource] = None,
        r53_resource: Optional[R53Resource] = None,
    ):
        super().__init__(
            args=TargetResource.Args(
                nlb_resource=nlb_resource,
                r53_resource=r53_resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        nlb_resource: Optional[NlbResource] = core.arg(default=None)

        r53_resource: Optional[R53Resource] = core.arg(default=None)


@core.schema
class DnsTargetResource(core.Schema):

    domain_name: Union[str, core.StringOut] = core.attr(str)

    hosted_zone_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    record_set_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    record_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_resource: Optional[TargetResource] = core.attr(TargetResource, default=None)

    def __init__(
        self,
        *,
        domain_name: Union[str, core.StringOut],
        hosted_zone_arn: Optional[Union[str, core.StringOut]] = None,
        record_set_id: Optional[Union[str, core.StringOut]] = None,
        record_type: Optional[Union[str, core.StringOut]] = None,
        target_resource: Optional[TargetResource] = None,
    ):
        super().__init__(
            args=DnsTargetResource.Args(
                domain_name=domain_name,
                hosted_zone_arn=hosted_zone_arn,
                record_set_id=record_set_id,
                record_type=record_type,
                target_resource=target_resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Union[str, core.StringOut] = core.arg()

        hosted_zone_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        record_set_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        record_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_resource: Optional[TargetResource] = core.arg(default=None)


@core.schema
class Resources(core.Schema):

    component_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_target_resource: Optional[DnsTargetResource] = core.attr(DnsTargetResource, default=None)

    readiness_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    resource_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        component_id: Union[str, core.StringOut],
        dns_target_resource: Optional[DnsTargetResource] = None,
        readiness_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resource_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Resources.Args(
                component_id=component_id,
                dns_target_resource=dns_target_resource,
                readiness_scopes=readiness_scopes,
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        component_id: Union[str, core.StringOut] = core.arg()

        dns_target_resource: Optional[DnsTargetResource] = core.arg(default=None)

        readiness_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        resource_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(
    type="aws_route53recoveryreadiness_resource_set", namespace="aws_route53recoveryreadiness"
)
class ResourceSet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_set_name: Union[str, core.StringOut] = core.attr(str)

    resource_set_type: Union[str, core.StringOut] = core.attr(str)

    resources: Union[List[Resources], core.ArrayOut[Resources]] = core.attr(
        Resources, kind=core.Kind.array
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
        resource_set_name: Union[str, core.StringOut],
        resource_set_type: Union[str, core.StringOut],
        resources: Union[List[Resources], core.ArrayOut[Resources]],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceSet.Args(
                resource_set_name=resource_set_name,
                resource_set_type=resource_set_type,
                resources=resources,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_set_name: Union[str, core.StringOut] = core.arg()

        resource_set_type: Union[str, core.StringOut] = core.arg()

        resources: Union[List[Resources], core.ArrayOut[Resources]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
