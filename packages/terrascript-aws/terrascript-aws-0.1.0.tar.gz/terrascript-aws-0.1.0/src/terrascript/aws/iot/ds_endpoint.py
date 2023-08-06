from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_iot_endpoint", namespace="aws_iot")
class DsEndpoint(core.Data):

    endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        endpoint_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpoint.Args(
                endpoint_type=endpoint_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
