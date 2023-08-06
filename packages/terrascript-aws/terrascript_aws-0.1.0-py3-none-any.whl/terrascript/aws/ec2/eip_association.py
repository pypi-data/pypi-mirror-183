from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_eip_association", namespace="aws_ec2")
class EipAssociation(core.Resource):

    allocation_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    allow_reassociation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    network_interface_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    private_ip_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    public_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        allocation_id: Optional[Union[str, core.StringOut]] = None,
        allow_reassociation: Optional[Union[bool, core.BoolOut]] = None,
        instance_id: Optional[Union[str, core.StringOut]] = None,
        network_interface_id: Optional[Union[str, core.StringOut]] = None,
        private_ip_address: Optional[Union[str, core.StringOut]] = None,
        public_ip: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EipAssociation.Args(
                allocation_id=allocation_id,
                allow_reassociation=allow_reassociation,
                instance_id=instance_id,
                network_interface_id=network_interface_id,
                private_ip_address=private_ip_address,
                public_ip=public_ip,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocation_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        allow_reassociation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_interface_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        public_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)
