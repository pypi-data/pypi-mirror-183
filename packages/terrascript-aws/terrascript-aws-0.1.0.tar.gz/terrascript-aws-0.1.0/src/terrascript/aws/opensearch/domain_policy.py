from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_opensearch_domain_policy", namespace="aws_opensearch")
class DomainPolicy(core.Resource):

    access_policies: Union[str, core.StringOut] = core.attr(str)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_policies: Union[str, core.StringOut],
        domain_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainPolicy.Args(
                access_policies=access_policies,
                domain_name=domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policies: Union[str, core.StringOut] = core.arg()

        domain_name: Union[str, core.StringOut] = core.arg()
