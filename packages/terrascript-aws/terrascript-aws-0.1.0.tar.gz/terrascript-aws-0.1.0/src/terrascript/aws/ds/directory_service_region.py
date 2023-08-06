from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VpcSettings(core.Schema):

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcSettings.Args(
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_directory_service_region", namespace="aws_ds")
class DirectoryServiceRegion(core.Resource):

    desired_number_of_domain_controllers: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    directory_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    region_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_settings: VpcSettings = core.attr(VpcSettings)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        region_name: Union[str, core.StringOut],
        vpc_settings: VpcSettings,
        desired_number_of_domain_controllers: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceRegion.Args(
                directory_id=directory_id,
                region_name=region_name,
                vpc_settings=vpc_settings,
                desired_number_of_domain_controllers=desired_number_of_domain_controllers,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        desired_number_of_domain_controllers: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        directory_id: Union[str, core.StringOut] = core.arg()

        region_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_settings: VpcSettings = core.arg()
