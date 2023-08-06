from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_rds_certificate", namespace="aws_rds")
class DsCertificate(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    customer_override_valid_till: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    latest_valid_till: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    thumbprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    valid_from: Union[str, core.StringOut] = core.attr(str, computed=True)

    valid_till: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
        latest_valid_till: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificate.Args(
                id=id,
                latest_valid_till=latest_valid_till,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        latest_valid_till: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
