from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CustomField(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomField.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ManagedField(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ManagedField.Args(
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ThingIndexingConfiguration(core.Schema):

    custom_field: Optional[Union[List[CustomField], core.ArrayOut[CustomField]]] = core.attr(
        CustomField, default=None, kind=core.Kind.array
    )

    device_defender_indexing_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    managed_field: Optional[Union[List[ManagedField], core.ArrayOut[ManagedField]]] = core.attr(
        ManagedField, default=None, computed=True, kind=core.Kind.array
    )

    named_shadow_indexing_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    thing_connectivity_indexing_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    thing_indexing_mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        thing_indexing_mode: Union[str, core.StringOut],
        custom_field: Optional[Union[List[CustomField], core.ArrayOut[CustomField]]] = None,
        device_defender_indexing_mode: Optional[Union[str, core.StringOut]] = None,
        managed_field: Optional[Union[List[ManagedField], core.ArrayOut[ManagedField]]] = None,
        named_shadow_indexing_mode: Optional[Union[str, core.StringOut]] = None,
        thing_connectivity_indexing_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ThingIndexingConfiguration.Args(
                thing_indexing_mode=thing_indexing_mode,
                custom_field=custom_field,
                device_defender_indexing_mode=device_defender_indexing_mode,
                managed_field=managed_field,
                named_shadow_indexing_mode=named_shadow_indexing_mode,
                thing_connectivity_indexing_mode=thing_connectivity_indexing_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_field: Optional[Union[List[CustomField], core.ArrayOut[CustomField]]] = core.arg(
            default=None
        )

        device_defender_indexing_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        managed_field: Optional[Union[List[ManagedField], core.ArrayOut[ManagedField]]] = core.arg(
            default=None
        )

        named_shadow_indexing_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        thing_connectivity_indexing_mode: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        thing_indexing_mode: Union[str, core.StringOut] = core.arg()


@core.schema
class ThingGroupIndexingConfiguration(core.Schema):

    custom_field: Optional[Union[List[CustomField], core.ArrayOut[CustomField]]] = core.attr(
        CustomField, default=None, kind=core.Kind.array
    )

    managed_field: Optional[Union[List[ManagedField], core.ArrayOut[ManagedField]]] = core.attr(
        ManagedField, default=None, computed=True, kind=core.Kind.array
    )

    thing_group_indexing_mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        thing_group_indexing_mode: Union[str, core.StringOut],
        custom_field: Optional[Union[List[CustomField], core.ArrayOut[CustomField]]] = None,
        managed_field: Optional[Union[List[ManagedField], core.ArrayOut[ManagedField]]] = None,
    ):
        super().__init__(
            args=ThingGroupIndexingConfiguration.Args(
                thing_group_indexing_mode=thing_group_indexing_mode,
                custom_field=custom_field,
                managed_field=managed_field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_field: Optional[Union[List[CustomField], core.ArrayOut[CustomField]]] = core.arg(
            default=None
        )

        managed_field: Optional[Union[List[ManagedField], core.ArrayOut[ManagedField]]] = core.arg(
            default=None
        )

        thing_group_indexing_mode: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_iot_indexing_configuration", namespace="aws_iot")
class IndexingConfiguration(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    thing_group_indexing_configuration: Optional[ThingGroupIndexingConfiguration] = core.attr(
        ThingGroupIndexingConfiguration, default=None, computed=True
    )

    thing_indexing_configuration: Optional[ThingIndexingConfiguration] = core.attr(
        ThingIndexingConfiguration, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        thing_group_indexing_configuration: Optional[ThingGroupIndexingConfiguration] = None,
        thing_indexing_configuration: Optional[ThingIndexingConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IndexingConfiguration.Args(
                thing_group_indexing_configuration=thing_group_indexing_configuration,
                thing_indexing_configuration=thing_indexing_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        thing_group_indexing_configuration: Optional[ThingGroupIndexingConfiguration] = core.arg(
            default=None
        )

        thing_indexing_configuration: Optional[ThingIndexingConfiguration] = core.arg(default=None)
