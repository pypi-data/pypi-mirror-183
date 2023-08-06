from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_network_acl_association", namespace="aws_vpc")
class NetworkAclAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_acl_id: Union[str, core.StringOut] = core.attr(str)

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        network_acl_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkAclAssociation.Args(
                network_acl_id=network_acl_id,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        network_acl_id: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()
