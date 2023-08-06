from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LogDestinationConfig(core.Schema):

    log_destination: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    log_destination_type: Union[str, core.StringOut] = core.attr(str)

    log_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        log_destination: Union[Dict[str, str], core.MapOut[core.StringOut]],
        log_destination_type: Union[str, core.StringOut],
        log_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LogDestinationConfig.Args(
                log_destination=log_destination,
                log_destination_type=log_destination_type,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_destination: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        log_destination_type: Union[str, core.StringOut] = core.arg()

        log_type: Union[str, core.StringOut] = core.arg()


@core.schema
class LoggingConfigurationBlk(core.Schema):

    log_destination_config: Union[
        List[LogDestinationConfig], core.ArrayOut[LogDestinationConfig]
    ] = core.attr(LogDestinationConfig, kind=core.Kind.array)

    def __init__(
        self,
        *,
        log_destination_config: Union[
            List[LogDestinationConfig], core.ArrayOut[LogDestinationConfig]
        ],
    ):
        super().__init__(
            args=LoggingConfigurationBlk.Args(
                log_destination_config=log_destination_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_destination_config: Union[
            List[LogDestinationConfig], core.ArrayOut[LogDestinationConfig]
        ] = core.arg()


@core.resource(type="aws_networkfirewall_logging_configuration", namespace="aws_networkfirewall")
class LoggingConfiguration(core.Resource):

    firewall_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    logging_configuration: LoggingConfigurationBlk = core.attr(LoggingConfigurationBlk)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_arn: Union[str, core.StringOut],
        logging_configuration: LoggingConfigurationBlk,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoggingConfiguration.Args(
                firewall_arn=firewall_arn,
                logging_configuration=logging_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        firewall_arn: Union[str, core.StringOut] = core.arg()

        logging_configuration: LoggingConfigurationBlk = core.arg()
