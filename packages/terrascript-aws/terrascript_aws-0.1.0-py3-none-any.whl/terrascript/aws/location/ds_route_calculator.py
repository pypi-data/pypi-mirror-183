from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_location_route_calculator", namespace="aws_location")
class DsRouteCalculator(core.Data):

    calculator_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    calculator_name: Union[str, core.StringOut] = core.attr(str)

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_source: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        calculator_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRouteCalculator.Args(
                calculator_name=calculator_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        calculator_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
