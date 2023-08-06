from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_acm_certificate_validation", namespace="aws_acm")
class CertificateValidation(core.Resource):

    certificate_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    validation_record_fqdns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_arn: Union[str, core.StringOut],
        validation_record_fqdns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CertificateValidation.Args(
                certificate_arn=certificate_arn,
                validation_record_fqdns=validation_record_fqdns,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: Union[str, core.StringOut] = core.arg()

        validation_record_fqdns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
