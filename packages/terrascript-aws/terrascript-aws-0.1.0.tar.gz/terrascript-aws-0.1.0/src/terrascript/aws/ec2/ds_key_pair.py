from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_key_pair", namespace="aws_ec2")
class DsKeyPair(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_public_key: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key_pair_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        include_public_key: Optional[Union[bool, core.BoolOut]] = None,
        key_name: Optional[Union[str, core.StringOut]] = None,
        key_pair_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsKeyPair.Args(
                filter=filter,
                include_public_key=include_public_key,
                key_name=key_name,
                key_pair_id=key_pair_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        include_public_key: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key_pair_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
