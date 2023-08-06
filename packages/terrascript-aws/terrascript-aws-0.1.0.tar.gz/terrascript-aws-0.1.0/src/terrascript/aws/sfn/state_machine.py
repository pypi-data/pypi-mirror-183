from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TracingConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=TracingConfiguration.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class LoggingConfiguration(core.Schema):

    include_execution_data: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_destination: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        include_execution_data: Optional[Union[bool, core.BoolOut]] = None,
        level: Optional[Union[str, core.StringOut]] = None,
        log_destination: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LoggingConfiguration.Args(
                include_execution_data=include_execution_data,
                level=level,
                log_destination=log_destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        include_execution_data: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_destination: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sfn_state_machine", namespace="aws_sfn")
class StateMachine(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    definition: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    logging_configuration: Optional[LoggingConfiguration] = core.attr(
        LoggingConfiguration, default=None, computed=True
    )

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tracing_configuration: Optional[TracingConfiguration] = core.attr(
        TracingConfiguration, default=None, computed=True
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        definition: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        logging_configuration: Optional[LoggingConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tracing_configuration: Optional[TracingConfiguration] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StateMachine.Args(
                definition=definition,
                name=name,
                role_arn=role_arn,
                logging_configuration=logging_configuration,
                tags=tags,
                tags_all=tags_all,
                tracing_configuration=tracing_configuration,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        definition: Union[str, core.StringOut] = core.arg()

        logging_configuration: Optional[LoggingConfiguration] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tracing_configuration: Optional[TracingConfiguration] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
