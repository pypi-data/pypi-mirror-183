from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TraceConfiguration(core.Schema):

    vendor: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        vendor: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TraceConfiguration.Args(
                vendor=vendor,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vendor: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_apprunner_observability_configuration", namespace="aws_apprunner")
class ObservabilityConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    observability_configuration_name: Union[str, core.StringOut] = core.attr(str)

    observability_configuration_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    trace_configuration: Optional[TraceConfiguration] = core.attr(TraceConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        observability_configuration_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        trace_configuration: Optional[TraceConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ObservabilityConfiguration.Args(
                observability_configuration_name=observability_configuration_name,
                tags=tags,
                tags_all=tags_all,
                trace_configuration=trace_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        observability_configuration_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        trace_configuration: Optional[TraceConfiguration] = core.arg(default=None)
