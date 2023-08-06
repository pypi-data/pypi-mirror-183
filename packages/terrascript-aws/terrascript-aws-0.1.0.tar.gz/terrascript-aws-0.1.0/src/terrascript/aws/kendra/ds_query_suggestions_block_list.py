from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SourceS3Path(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceS3Path.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_kendra_query_suggestions_block_list", namespace="aws_kendra")
class DsQuerySuggestionsBlockList(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_size_bytes: Union[int, core.IntOut] = core.attr(int, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_id: Union[str, core.StringOut] = core.attr(str)

    item_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    query_suggestions_block_list_id: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_s3_path: Union[List[SourceS3Path], core.ArrayOut[SourceS3Path]] = core.attr(
        SourceS3Path, computed=True, kind=core.Kind.array
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
        index_id: Union[str, core.StringOut],
        query_suggestions_block_list_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsQuerySuggestionsBlockList.Args(
                index_id=index_id,
                query_suggestions_block_list_id=query_suggestions_block_list_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_id: Union[str, core.StringOut] = core.arg()

        query_suggestions_block_list_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
