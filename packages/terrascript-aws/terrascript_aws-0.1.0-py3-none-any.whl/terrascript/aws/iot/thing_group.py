from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RootToParentGroups(core.Schema):

    group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        group_arn: Union[str, core.StringOut],
        group_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RootToParentGroups.Args(
                group_arn=group_arn,
                group_name=group_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_arn: Union[str, core.StringOut] = core.arg()

        group_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Metadata(core.Schema):

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_to_parent_groups: Union[
        List[RootToParentGroups], core.ArrayOut[RootToParentGroups]
    ] = core.attr(RootToParentGroups, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        creation_date: Union[str, core.StringOut],
        parent_group_name: Union[str, core.StringOut],
        root_to_parent_groups: Union[List[RootToParentGroups], core.ArrayOut[RootToParentGroups]],
    ):
        super().__init__(
            args=Metadata.Args(
                creation_date=creation_date,
                parent_group_name=parent_group_name,
                root_to_parent_groups=root_to_parent_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_date: Union[str, core.StringOut] = core.arg()

        parent_group_name: Union[str, core.StringOut] = core.arg()

        root_to_parent_groups: Union[
            List[RootToParentGroups], core.ArrayOut[RootToParentGroups]
        ] = core.arg()


@core.schema
class AttributePayload(core.Schema):

    attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AttributePayload.Args(
                attributes=attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class Properties(core.Schema):

    attribute_payload: Optional[AttributePayload] = core.attr(AttributePayload, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        attribute_payload: Optional[AttributePayload] = None,
        description: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Properties.Args(
                attribute_payload=attribute_payload,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_payload: Optional[AttributePayload] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_iot_thing_group", namespace="aws_iot")
class ThingGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    metadata: Union[List[Metadata], core.ArrayOut[Metadata]] = core.attr(
        Metadata, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    parent_group_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    properties: Optional[Properties] = core.attr(Properties, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        parent_group_name: Optional[Union[str, core.StringOut]] = None,
        properties: Optional[Properties] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingGroup.Args(
                name=name,
                parent_group_name=parent_group_name,
                properties=properties,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        parent_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        properties: Optional[Properties] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
