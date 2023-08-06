from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_region", namespace="aws_meta_data_sources")
class DsRegion(core.Data):

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        endpoint: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRegion.Args(
                endpoint=endpoint,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
