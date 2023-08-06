from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_backup_region_settings", namespace="aws_backup")
class RegionSettings(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_type_management_preference: Optional[
        Union[Dict[str, bool], core.MapOut[core.BoolOut]]
    ] = core.attr(bool, default=None, computed=True, kind=core.Kind.map)

    resource_type_opt_in_preference: Union[Dict[str, bool], core.MapOut[core.BoolOut]] = core.attr(
        bool, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        resource_type_opt_in_preference: Union[Dict[str, bool], core.MapOut[core.BoolOut]],
        resource_type_management_preference: Optional[
            Union[Dict[str, bool], core.MapOut[core.BoolOut]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegionSettings.Args(
                resource_type_opt_in_preference=resource_type_opt_in_preference,
                resource_type_management_preference=resource_type_management_preference,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_type_management_preference: Optional[
            Union[Dict[str, bool], core.MapOut[core.BoolOut]]
        ] = core.arg(default=None)

        resource_type_opt_in_preference: Union[
            Dict[str, bool], core.MapOut[core.BoolOut]
        ] = core.arg()
