from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TieringPolicy(core.Schema):

    cooling_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cooling_period: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TieringPolicy.Args(
                cooling_period=cooling_period,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cooling_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_fsx_ontap_volume", namespace="aws_fsx")
class OntapVolume(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    flexcache_endpoint_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    junction_path: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    ontap_volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_style: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    size_in_megabytes: Union[int, core.IntOut] = core.attr(int)

    storage_efficiency_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    storage_virtual_machine_id: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tiering_policy: Optional[TieringPolicy] = core.attr(TieringPolicy, default=None)

    uuid: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        junction_path: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        size_in_megabytes: Union[int, core.IntOut],
        storage_efficiency_enabled: Union[bool, core.BoolOut],
        storage_virtual_machine_id: Union[str, core.StringOut],
        security_style: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tiering_policy: Optional[TieringPolicy] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OntapVolume.Args(
                junction_path=junction_path,
                name=name,
                size_in_megabytes=size_in_megabytes,
                storage_efficiency_enabled=storage_efficiency_enabled,
                storage_virtual_machine_id=storage_virtual_machine_id,
                security_style=security_style,
                tags=tags,
                tags_all=tags_all,
                tiering_policy=tiering_policy,
                volume_type=volume_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        junction_path: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        security_style: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        size_in_megabytes: Union[int, core.IntOut] = core.arg()

        storage_efficiency_enabled: Union[bool, core.BoolOut] = core.arg()

        storage_virtual_machine_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tiering_policy: Optional[TieringPolicy] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
