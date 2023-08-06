from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ce_anomaly_monitor", namespace="aws_ce")
class AnomalyMonitor(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    monitor_dimension: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    monitor_specification: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    monitor_type: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        monitor_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        monitor_dimension: Optional[Union[str, core.StringOut]] = None,
        monitor_specification: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AnomalyMonitor.Args(
                monitor_type=monitor_type,
                name=name,
                monitor_dimension=monitor_dimension,
                monitor_specification=monitor_specification,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        monitor_dimension: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        monitor_specification: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        monitor_type: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
