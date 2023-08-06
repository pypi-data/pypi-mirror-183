from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class RecordingGroup(core.Schema):

    all_supported: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_global_resource_types: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        all_supported: Optional[Union[bool, core.BoolOut]] = None,
        include_global_resource_types: Optional[Union[bool, core.BoolOut]] = None,
        resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=RecordingGroup.Args(
                all_supported=all_supported,
                include_global_resource_types=include_global_resource_types,
                resource_types=resource_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_supported: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_global_resource_types: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.resource(type="aws_config_configuration_recorder", namespace="aws_config")
class ConfigurationRecorder(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    recording_group: Optional[RecordingGroup] = core.attr(
        RecordingGroup, default=None, computed=True
    )

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        role_arn: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        recording_group: Optional[RecordingGroup] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationRecorder.Args(
                role_arn=role_arn,
                name=name,
                recording_group=recording_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        recording_group: Optional[RecordingGroup] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()
