from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_s3_objects", namespace="aws_s3")
class DsObjects(core.Data):

    bucket: Union[str, core.StringOut] = core.attr(str)

    common_prefixes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    delimiter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encoding_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fetch_owner: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    keys: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_keys: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    owners: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start_after: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: Union[str, core.StringOut],
        delimiter: Optional[Union[str, core.StringOut]] = None,
        encoding_type: Optional[Union[str, core.StringOut]] = None,
        fetch_owner: Optional[Union[bool, core.BoolOut]] = None,
        max_keys: Optional[Union[int, core.IntOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        start_after: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsObjects.Args(
                bucket=bucket,
                delimiter=delimiter,
                encoding_type=encoding_type,
                fetch_owner=fetch_owner,
                max_keys=max_keys,
                prefix=prefix,
                start_after=start_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        delimiter: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encoding_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fetch_owner: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_keys: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start_after: Optional[Union[str, core.StringOut]] = core.arg(default=None)
