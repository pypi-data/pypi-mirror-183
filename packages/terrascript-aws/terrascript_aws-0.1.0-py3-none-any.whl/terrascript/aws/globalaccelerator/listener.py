from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PortRange(core.Schema):

    from_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    to_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: Optional[Union[int, core.IntOut]] = None,
        to_port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=PortRange.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        to_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_globalaccelerator_listener", namespace="aws_globalaccelerator")
class Listener(core.Resource):

    accelerator_arn: Union[str, core.StringOut] = core.attr(str)

    client_affinity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port_range: Union[List[PortRange], core.ArrayOut[PortRange]] = core.attr(
        PortRange, kind=core.Kind.array
    )

    protocol: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        accelerator_arn: Union[str, core.StringOut],
        port_range: Union[List[PortRange], core.ArrayOut[PortRange]],
        protocol: Union[str, core.StringOut],
        client_affinity: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Listener.Args(
                accelerator_arn=accelerator_arn,
                port_range=port_range,
                protocol=protocol,
                client_affinity=client_affinity,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accelerator_arn: Union[str, core.StringOut] = core.arg()

        client_affinity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port_range: Union[List[PortRange], core.ArrayOut[PortRange]] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()
