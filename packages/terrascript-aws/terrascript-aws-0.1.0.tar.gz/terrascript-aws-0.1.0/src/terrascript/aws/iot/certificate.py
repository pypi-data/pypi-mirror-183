from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_certificate", namespace="aws_iot")
class Certificate(core.Resource):

    active: Union[bool, core.BoolOut] = core.attr(bool)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    ca_pem: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_pem: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    csr: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        active: Union[bool, core.BoolOut],
        ca_pem: Optional[Union[str, core.StringOut]] = None,
        certificate_pem: Optional[Union[str, core.StringOut]] = None,
        csr: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                active=active,
                ca_pem=ca_pem,
                certificate_pem=certificate_pem,
                csr=csr,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active: Union[bool, core.BoolOut] = core.arg()

        ca_pem: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_pem: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        csr: Optional[Union[str, core.StringOut]] = core.arg(default=None)
