from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OutputConfig(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_output_location: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_output_location: Union[str, core.StringOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OutputConfig.Args(
                s3_output_location=s3_output_location,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_output_location: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_sagemaker_device_fleet", namespace="aws_sagemaker")
class DeviceFleet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_fleet_name: Union[str, core.StringOut] = core.attr(str)

    enable_iot_role_alias: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iot_role_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    output_config: OutputConfig = core.attr(OutputConfig)

    role_arn: Union[str, core.StringOut] = core.attr(str)

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
        device_fleet_name: Union[str, core.StringOut],
        output_config: OutputConfig,
        role_arn: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        enable_iot_role_alias: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeviceFleet.Args(
                device_fleet_name=device_fleet_name,
                output_config=output_config,
                role_arn=role_arn,
                description=description,
                enable_iot_role_alias=enable_iot_role_alias,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_fleet_name: Union[str, core.StringOut] = core.arg()

        enable_iot_role_alias: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        output_config: OutputConfig = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
