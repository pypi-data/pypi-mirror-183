from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class NetworkInterface(core.Schema):

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zone: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
        private_ip_address: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkInterface.Args(
                availability_zone=availability_zone,
                network_interface_id=network_interface_id,
                private_ip_address=private_ip_address,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()

        private_ip_address: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.schema
class VpcEndpoint(core.Schema):

    network_interface: Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]] = core.attr(
        NetworkInterface, computed=True, kind=core.Kind.array
    )

    vpc_endpoint_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        network_interface: Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]],
        vpc_endpoint_id: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcEndpoint.Args(
                network_interface=network_interface,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        network_interface: Union[
            List[NetworkInterface], core.ArrayOut[NetworkInterface]
        ] = core.arg()

        vpc_endpoint_id: Union[str, core.StringOut] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_redshift_endpoint_access", namespace="aws_redshift")
class EndpointAccess(core.Resource):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    endpoint_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    resource_owner: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    subnet_group_name: Union[str, core.StringOut] = core.attr(str)

    vpc_endpoint: Union[List[VpcEndpoint], core.ArrayOut[VpcEndpoint]] = core.attr(
        VpcEndpoint, computed=True, kind=core.Kind.array
    )

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        endpoint_name: Union[str, core.StringOut],
        subnet_group_name: Union[str, core.StringOut],
        resource_owner: Optional[Union[str, core.StringOut]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointAccess.Args(
                cluster_identifier=cluster_identifier,
                endpoint_name=endpoint_name,
                subnet_group_name=subnet_group_name,
                resource_owner=resource_owner,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: Union[str, core.StringOut] = core.arg()

        endpoint_name: Union[str, core.StringOut] = core.arg()

        resource_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_group_name: Union[str, core.StringOut] = core.arg()

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
