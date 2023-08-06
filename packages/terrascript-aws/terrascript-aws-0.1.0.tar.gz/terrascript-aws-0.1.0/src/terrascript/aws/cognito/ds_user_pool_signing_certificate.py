from typing import Union

import terrascript.core as core


@core.data(type="aws_cognito_user_pool_signing_certificate", namespace="aws_cognito")
class DsUserPoolSigningCertificate(core.Data):
    """
    The certificate string
    """

    certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (required) The Cognito user pool ID.
    """
    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        user_pool_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsUserPoolSigningCertificate.Args(
                user_pool_id=user_pool_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        user_pool_id: Union[str, core.StringOut] = core.arg()
