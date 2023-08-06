from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class NetworkInterfaces(core.Schema):

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        network_interface_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkInterfaces.Args(
                network_interface_id=network_interface_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        network_interface_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3outposts_endpoint", namespace="aws_s3outposts")
class Endpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interfaces: Union[
        List[NetworkInterfaces], core.ArrayOut[NetworkInterfaces]
    ] = core.attr(NetworkInterfaces, computed=True, kind=core.Kind.array)

    outpost_id: Union[str, core.StringOut] = core.attr(str)

    security_group_id: Union[str, core.StringOut] = core.attr(str)

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        outpost_id: Union[str, core.StringOut],
        security_group_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                outpost_id=outpost_id,
                security_group_id=security_group_id,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        outpost_id: Union[str, core.StringOut] = core.arg()

        security_group_id: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()
