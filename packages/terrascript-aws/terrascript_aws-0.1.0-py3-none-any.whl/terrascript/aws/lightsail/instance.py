from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lightsail_instance", namespace="aws_lightsail")
class Instance(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str)

    blueprint_id: Union[str, core.StringOut] = core.attr(str)

    bundle_id: Union[str, core.StringOut] = core.attr(str)

    cpu_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    is_static_ip: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    key_pair_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    private_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    ram_size: Union[float, core.FloatOut] = core.attr(float, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    username: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: Union[str, core.StringOut],
        blueprint_id: Union[str, core.StringOut],
        bundle_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        key_pair_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_data: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                availability_zone=availability_zone,
                blueprint_id=blueprint_id,
                bundle_id=bundle_id,
                name=name,
                key_pair_name=key_pair_name,
                tags=tags,
                tags_all=tags_all,
                user_data=user_data,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: Union[str, core.StringOut] = core.arg()

        blueprint_id: Union[str, core.StringOut] = core.arg()

        bundle_id: Union[str, core.StringOut] = core.arg()

        key_pair_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)
