from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Rule(core.Schema):

    attribute: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    operator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        attribute: Optional[Union[str, core.StringOut]] = None,
        operator: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                attribute=attribute,
                operator=operator,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_devicefarm_device_pool", namespace="aws_devicefarm")
class DevicePool(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_devices: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    project_arn: Union[str, core.StringOut] = core.attr(str)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        project_arn: Union[str, core.StringOut],
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        description: Optional[Union[str, core.StringOut]] = None,
        max_devices: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DevicePool.Args(
                name=name,
                project_arn=project_arn,
                rule=rule,
                description=description,
                max_devices=max_devices,
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

        max_devices: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        project_arn: Union[str, core.StringOut] = core.arg()

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
