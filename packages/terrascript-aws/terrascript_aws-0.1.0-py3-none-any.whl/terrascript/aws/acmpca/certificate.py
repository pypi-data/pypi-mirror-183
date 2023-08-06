from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Validity(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Validity.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_acmpca_certificate", namespace="aws_acmpca")
class Certificate(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_authority_arn: Union[str, core.StringOut] = core.attr(str)

    certificate_chain: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_signing_request: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_algorithm: Union[str, core.StringOut] = core.attr(str)

    template_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    validity: Validity = core.attr(Validity)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_authority_arn: Union[str, core.StringOut],
        certificate_signing_request: Union[str, core.StringOut],
        signing_algorithm: Union[str, core.StringOut],
        validity: Validity,
        template_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_authority_arn=certificate_authority_arn,
                certificate_signing_request=certificate_signing_request,
                signing_algorithm=signing_algorithm,
                validity=validity,
                template_arn=template_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_authority_arn: Union[str, core.StringOut] = core.arg()

        certificate_signing_request: Union[str, core.StringOut] = core.arg()

        signing_algorithm: Union[str, core.StringOut] = core.arg()

        template_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        validity: Validity = core.arg()
