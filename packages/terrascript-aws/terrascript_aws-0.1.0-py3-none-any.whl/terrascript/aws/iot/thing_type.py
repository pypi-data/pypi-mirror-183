from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Properties(core.Schema):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    searchable_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        description: Optional[Union[str, core.StringOut]] = None,
        searchable_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Properties.Args(
                description=description,
                searchable_attributes=searchable_attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        searchable_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.resource(type="aws_iot_thing_type", namespace="aws_iot")
class ThingType(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    deprecated: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    properties: Optional[Properties] = core.attr(Properties, default=None)

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
        deprecated: Optional[Union[bool, core.BoolOut]] = None,
        properties: Optional[Properties] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingType.Args(
                name=name,
                deprecated=deprecated,
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
        deprecated: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        properties: Optional[Properties] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
