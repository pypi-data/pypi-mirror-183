from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_iam_server_certificate", namespace="aws_iam")
class DsServerCertificate(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_body: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_chain: Union[str, core.StringOut] = core.attr(str, computed=True)

    expiration_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    path_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    upload_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        latest: Optional[Union[bool, core.BoolOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        path_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServerCertificate.Args(
                latest=latest,
                name=name,
                name_prefix=name_prefix,
                path_prefix=path_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        latest: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
