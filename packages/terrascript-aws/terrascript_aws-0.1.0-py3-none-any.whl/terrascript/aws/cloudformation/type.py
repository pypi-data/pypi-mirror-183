from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class LoggingConfig(core.Schema):

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    log_role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        log_group_name: Union[str, core.StringOut],
        log_role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LoggingConfig.Args(
                log_group_name=log_group_name,
                log_role_arn=log_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name: Union[str, core.StringOut] = core.arg()

        log_role_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudformation_type", namespace="aws_cloudformation")
class Type(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    deprecated_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    documentation_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    execution_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_default_version: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    logging_config: Optional[LoggingConfig] = core.attr(LoggingConfig, default=None)

    provisioning_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    schema: Union[str, core.StringOut] = core.attr(str, computed=True)

    schema_handler_package: Union[str, core.StringOut] = core.attr(str)

    source_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    type_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    type_name: Union[str, core.StringOut] = core.attr(str)

    version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    visibility: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        schema_handler_package: Union[str, core.StringOut],
        type_name: Union[str, core.StringOut],
        execution_role_arn: Optional[Union[str, core.StringOut]] = None,
        logging_config: Optional[LoggingConfig] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Type.Args(
                schema_handler_package=schema_handler_package,
                type_name=type_name,
                execution_role_arn=execution_role_arn,
                logging_config=logging_config,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        execution_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logging_config: Optional[LoggingConfig] = core.arg(default=None)

        schema_handler_package: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type_name: Union[str, core.StringOut] = core.arg()
