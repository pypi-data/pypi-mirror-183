from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Path(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=S3Path.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_kendra_faq", namespace="aws_kendra")
class DsFaq(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    faq_id: Union[str, core.StringOut] = core.attr(str)

    file_format: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_id: Union[str, core.StringOut] = core.attr(str)

    language_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_path: Union[List[S3Path], core.ArrayOut[S3Path]] = core.attr(
        S3Path, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        faq_id: Union[str, core.StringOut],
        index_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFaq.Args(
                faq_id=faq_id,
                index_id=index_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        faq_id: Union[str, core.StringOut] = core.arg()

        index_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
