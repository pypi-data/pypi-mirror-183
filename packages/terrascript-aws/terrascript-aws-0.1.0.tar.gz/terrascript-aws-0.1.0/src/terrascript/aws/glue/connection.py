from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PhysicalConnectionRequirements(core.Schema):

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_group_id_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        security_group_id_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
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
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_id_list: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_glue_connection", namespace="aws_glue")
class Connection(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    connection_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    connection_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    match_criteria: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    physical_connection_requirements: Optional[PhysicalConnectionRequirements] = core.attr(
        PhysicalConnectionRequirements, default=None
    )

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
        name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        connection_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        connection_type: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        match_criteria: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        physical_connection_requirements: Optional[PhysicalConnectionRequirements] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                name=name,
                catalog_id=catalog_id,
                connection_properties=connection_properties,
                connection_type=connection_type,
                description=description,
                match_criteria=match_criteria,
                physical_connection_requirements=physical_connection_requirements,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_properties: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        connection_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        match_criteria: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        physical_connection_requirements: Optional[PhysicalConnectionRequirements] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
