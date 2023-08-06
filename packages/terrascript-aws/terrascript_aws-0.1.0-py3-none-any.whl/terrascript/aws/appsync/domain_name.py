from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appsync_domain_name", namespace="aws_appsync")
class DomainName(core.Resource):

    appsync_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_arn: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_arn: Union[str, core.StringOut],
        domain_name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainName.Args(
                certificate_arn=certificate_arn,
                domain_name=domain_name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()
