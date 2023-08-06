from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_managed_prefix_list_entry", namespace="aws_vpc")
class Ec2ManagedPrefixListEntry(core.Resource):

    cidr: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    prefix_list_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cidr: Union[str, core.StringOut],
        prefix_list_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ManagedPrefixListEntry.Args(
                cidr=cidr,
                prefix_list_id=prefix_list_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix_list_id: Union[str, core.StringOut] = core.arg()
