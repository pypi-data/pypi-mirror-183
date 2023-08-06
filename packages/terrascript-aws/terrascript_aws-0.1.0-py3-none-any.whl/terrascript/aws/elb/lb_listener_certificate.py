from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lb_listener_certificate", namespace="aws_elb")
class LbListenerCertificate(core.Resource):

    certificate_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    listener_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_arn: Union[str, core.StringOut],
        listener_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbListenerCertificate.Args(
                certificate_arn=certificate_arn,
                listener_arn=listener_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: Union[str, core.StringOut] = core.arg()

        listener_arn: Union[str, core.StringOut] = core.arg()
