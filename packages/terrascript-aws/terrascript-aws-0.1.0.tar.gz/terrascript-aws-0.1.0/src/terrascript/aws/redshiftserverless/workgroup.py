from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ConfigParameter(core.Schema):

    parameter_key: Union[str, core.StringOut] = core.attr(str)

    parameter_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        parameter_key: Union[str, core.StringOut],
        parameter_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConfigParameter.Args(
                parameter_key=parameter_key,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_key: Union[str, core.StringOut] = core.arg()

        parameter_value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_redshiftserverless_workgroup", namespace="aws_redshiftserverless")
class Workgroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    base_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    config_parameter: Optional[
        Union[List[ConfigParameter], core.ArrayOut[ConfigParameter]]
    ] = core.attr(ConfigParameter, default=None, computed=True, kind=core.Kind.array)

    enhanced_vpc_routing: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    namespace_name: Union[str, core.StringOut] = core.attr(str)

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    workgroup_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    workgroup_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        namespace_name: Union[str, core.StringOut],
        workgroup_name: Union[str, core.StringOut],
        base_capacity: Optional[Union[int, core.IntOut]] = None,
        config_parameter: Optional[
            Union[List[ConfigParameter], core.ArrayOut[ConfigParameter]]
        ] = None,
        enhanced_vpc_routing: Optional[Union[bool, core.BoolOut]] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workgroup.Args(
                namespace_name=namespace_name,
                workgroup_name=workgroup_name,
                base_capacity=base_capacity,
                config_parameter=config_parameter,
                enhanced_vpc_routing=enhanced_vpc_routing,
                publicly_accessible=publicly_accessible,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        base_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        config_parameter: Optional[
            Union[List[ConfigParameter], core.ArrayOut[ConfigParameter]]
        ] = core.arg(default=None)

        enhanced_vpc_routing: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        namespace_name: Union[str, core.StringOut] = core.arg()

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        workgroup_name: Union[str, core.StringOut] = core.arg()
