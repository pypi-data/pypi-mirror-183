from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_acmpca_certificate_authority_certificate", namespace="aws_acmpca")
class CertificateAuthorityCertificate(core.Resource):

    certificate: Union[str, core.StringOut] = core.attr(str)

    certificate_authority_arn: Union[str, core.StringOut] = core.attr(str)

    certificate_chain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate: Union[str, core.StringOut],
        certificate_authority_arn: Union[str, core.StringOut],
        certificate_chain: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CertificateAuthorityCertificate.Args(
                certificate=certificate,
                certificate_authority_arn=certificate_authority_arn,
                certificate_chain=certificate_chain,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate: Union[str, core.StringOut] = core.arg()

        certificate_authority_arn: Union[str, core.StringOut] = core.arg()

        certificate_chain: Optional[Union[str, core.StringOut]] = core.arg(default=None)
