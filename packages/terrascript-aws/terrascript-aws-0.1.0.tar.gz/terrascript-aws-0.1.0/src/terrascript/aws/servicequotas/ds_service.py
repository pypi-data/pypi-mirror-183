from typing import Union

import terrascript.core as core


@core.data(type="aws_servicequotas_service", namespace="aws_servicequotas")
class DsService(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        service_name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsService.Args(
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        service_name: Union[str, core.StringOut] = core.arg()
