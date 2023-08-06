from typing import Union

import terrascript.core as core


@core.data(type="aws_ses_domain_identity", namespace="aws_ses")
class DsDomainIdentity(core.Data):
    """
    The ARN of the domain identity.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The name of the domain
    """
    domain: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    A code which when added to the domain as a TXT record will signal to SES that the owner of the domai
    n has authorized SES to act on their behalf.
    """
    verification_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        domain: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsDomainIdentity.Args(
                domain=domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: Union[str, core.StringOut] = core.arg()
