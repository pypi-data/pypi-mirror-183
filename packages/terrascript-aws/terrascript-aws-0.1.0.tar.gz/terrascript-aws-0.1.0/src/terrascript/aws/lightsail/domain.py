from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lightsail_domain", namespace="aws_lightsail")
class Domain(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                domain_name=domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: Union[str, core.StringOut] = core.arg()
