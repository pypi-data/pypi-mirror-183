from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_directory_service_conditional_forwarder", namespace="aws_ds")
class DirectoryServiceConditionalForwarder(core.Resource):

    directory_id: Union[str, core.StringOut] = core.attr(str)

    dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    remote_domain_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        dns_ips: Union[List[str], core.ArrayOut[core.StringOut]],
        remote_domain_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceConditionalForwarder.Args(
                directory_id=directory_id,
                dns_ips=dns_ips,
                remote_domain_name=remote_domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: Union[str, core.StringOut] = core.arg()

        dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        remote_domain_name: Union[str, core.StringOut] = core.arg()
