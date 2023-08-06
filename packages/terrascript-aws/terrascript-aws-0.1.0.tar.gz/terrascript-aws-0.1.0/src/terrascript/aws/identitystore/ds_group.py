from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    attribute_path: Union[str, core.StringOut] = core.attr(str)

    attribute_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        attribute_path: Union[str, core.StringOut],
        attribute_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                attribute_path=attribute_path,
                attribute_value=attribute_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_path: Union[str, core.StringOut] = core.arg()

        attribute_value: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_identitystore_group", namespace="aws_identitystore")
class DsGroup(core.Data):

    display_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Union[List[Filter], core.ArrayOut[Filter]] = core.attr(Filter, kind=core.Kind.array)

    group_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_store_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Union[List[Filter], core.ArrayOut[Filter]],
        identity_store_id: Union[str, core.StringOut],
        group_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                filter=filter,
                identity_store_id=identity_store_id,
                group_id=group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Union[List[Filter], core.ArrayOut[Filter]] = core.arg()

        group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_store_id: Union[str, core.StringOut] = core.arg()
