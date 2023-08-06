from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class EnumerationValue(core.Schema):

    synonyms: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        value: Union[str, core.StringOut],
        synonyms: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=EnumerationValue.Args(
                value=value,
                synonyms=synonyms,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        synonyms: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_lex_slot_type", namespace="aws_lex")
class SlotType(core.Resource):

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    create_version: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enumeration_value: Union[List[EnumerationValue], core.ArrayOut[EnumerationValue]] = core.attr(
        EnumerationValue, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    value_selection_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        enumeration_value: Union[List[EnumerationValue], core.ArrayOut[EnumerationValue]],
        name: Union[str, core.StringOut],
        create_version: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        value_selection_strategy: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SlotType.Args(
                enumeration_value=enumeration_value,
                name=name,
                create_version=create_version,
                description=description,
                value_selection_strategy=value_selection_strategy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        create_version: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enumeration_value: Union[
            List[EnumerationValue], core.ArrayOut[EnumerationValue]
        ] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        value_selection_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)
