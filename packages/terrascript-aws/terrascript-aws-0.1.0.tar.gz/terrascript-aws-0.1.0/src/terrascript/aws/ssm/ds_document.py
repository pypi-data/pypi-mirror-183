from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_ssm_document", namespace="aws_ssm")
class DsDocument(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    content: Union[str, core.StringOut] = core.attr(str, computed=True)

    document_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    document_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        document_format: Optional[Union[str, core.StringOut]] = None,
        document_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDocument.Args(
                name=name,
                document_format=document_format,
                document_version=document_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        document_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
