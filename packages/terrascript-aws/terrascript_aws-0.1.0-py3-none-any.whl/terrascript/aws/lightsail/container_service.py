from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Certificate(core.Schema):

    certificate_name: Union[str, core.StringOut] = core.attr(str)

    domain_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        certificate_name: Union[str, core.StringOut],
        domain_names: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Certificate.Args(
                certificate_name=certificate_name,
                domain_names=domain_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_name: Union[str, core.StringOut] = core.arg()

        domain_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class PublicDomainNames(core.Schema):

    certificate: Union[List[Certificate], core.ArrayOut[Certificate]] = core.attr(
        Certificate, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        certificate: Union[List[Certificate], core.ArrayOut[Certificate]],
    ):
        super().__init__(
            args=PublicDomainNames.Args(
                certificate=certificate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: Union[List[Certificate], core.ArrayOut[Certificate]] = core.arg()


@core.resource(type="aws_lightsail_container_service", namespace="aws_lightsail")
class ContainerService(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    power: Union[str, core.StringOut] = core.attr(str)

    power_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_domain_names: Optional[PublicDomainNames] = core.attr(PublicDomainNames, default=None)

    resource_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    scale: Union[int, core.IntOut] = core.attr(int)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        power: Union[str, core.StringOut],
        scale: Union[int, core.IntOut],
        is_disabled: Optional[Union[bool, core.BoolOut]] = None,
        public_domain_names: Optional[PublicDomainNames] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContainerService.Args(
                name=name,
                power=power,
                scale=scale,
                is_disabled=is_disabled,
                public_domain_names=public_domain_names,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        is_disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        power: Union[str, core.StringOut] = core.arg()

        public_domain_names: Optional[PublicDomainNames] = core.arg(default=None)

        scale: Union[int, core.IntOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
