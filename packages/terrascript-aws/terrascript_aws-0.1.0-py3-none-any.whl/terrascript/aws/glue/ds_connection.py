from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PhysicalConnectionRequirements(core.Schema):

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_id_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zone: Union[str, core.StringOut],
        security_group_id_list: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PhysicalConnectionRequirements.Args(
                availability_zone=availability_zone,
                security_group_id_list=security_group_id_list,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Union[str, core.StringOut] = core.arg()

        security_group_id_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_glue_connection", namespace="aws_glue")
class DsConnection(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_properties: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    connection_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    match_criteria: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    physical_connection_requirements: Union[
        List[PhysicalConnectionRequirements], core.ArrayOut[PhysicalConnectionRequirements]
    ] = core.attr(PhysicalConnectionRequirements, computed=True, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConnection.Args(
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
