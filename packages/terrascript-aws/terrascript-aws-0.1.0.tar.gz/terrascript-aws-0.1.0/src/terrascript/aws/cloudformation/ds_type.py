from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class LoggingConfig(core.Schema):

    log_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_cloudformation_type", namespace="aws_cloudformation")
class DsType(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    default_version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    deprecated_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    documentation_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    execution_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_default_version: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    logging_config: Union[List[LoggingConfig], core.ArrayOut[LoggingConfig]] = core.attr(
        LoggingConfig, computed=True, kind=core.Kind.array
    )

    provisioning_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    schema: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    type_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    type_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    visibility: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        type_name: Optional[Union[str, core.StringOut]] = None,
        version_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsType.Args(
                arn=arn,
                type=type,
                type_name=type_name,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
