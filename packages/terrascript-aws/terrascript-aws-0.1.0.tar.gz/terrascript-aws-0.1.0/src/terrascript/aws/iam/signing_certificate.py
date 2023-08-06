from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_signing_certificate", namespace="aws_iam")
class SigningCertificate(core.Resource):

    certificate_body: Union[str, core.StringOut] = core.attr(str)

    certificate_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_body: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningCertificate.Args(
                certificate_body=certificate_body,
                user_name=user_name,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_body: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_name: Union[str, core.StringOut] = core.arg()
