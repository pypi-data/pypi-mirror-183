from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PortInfo(core.Schema):

    cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    from_port: Union[int, core.IntOut] = core.attr(int)

    protocol: Union[str, core.StringOut] = core.attr(str)

    to_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        from_port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        to_port: Union[int, core.IntOut],
        cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=PortInfo.Args(
                from_port=from_port,
                protocol=protocol,
                to_port=to_port,
                cidrs=cidrs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        from_port: Union[int, core.IntOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        to_port: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_lightsail_instance_public_ports", namespace="aws_lightsail")
class InstancePublicPorts(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_name: Union[str, core.StringOut] = core.attr(str)

    port_info: Union[List[PortInfo], core.ArrayOut[PortInfo]] = core.attr(
        PortInfo, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        instance_name: Union[str, core.StringOut],
        port_info: Union[List[PortInfo], core.ArrayOut[PortInfo]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstancePublicPorts.Args(
                instance_name=instance_name,
                port_info=port_info,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_name: Union[str, core.StringOut] = core.arg()

        port_info: Union[List[PortInfo], core.ArrayOut[PortInfo]] = core.arg()
