from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class EnumerationValue(core.Schema):

    synonyms: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        synonyms: Union[List[str], core.ArrayOut[core.StringOut]],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EnumerationValue.Args(
                synonyms=synonyms,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        synonyms: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_lex_slot_type", namespace="aws_lex")
class DsSlotType(core.Data):

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    enumeration_value: Union[List[EnumerationValue], core.ArrayOut[EnumerationValue]] = core.attr(
        EnumerationValue, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    value_selection_strategy: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSlotType.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
