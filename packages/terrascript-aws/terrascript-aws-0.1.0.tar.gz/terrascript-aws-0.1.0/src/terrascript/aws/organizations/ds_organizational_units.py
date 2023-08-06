from typing import List, Union

import terrascript.core as core


@core.schema
class Children(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Children.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_organizations_organizational_units", namespace="aws_organizations")
class DsOrganizationalUnits(core.Data):

    children: Union[List[Children], core.ArrayOut[Children]] = core.attr(
        Children, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        parent_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsOrganizationalUnits.Args(
                parent_id=parent_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parent_id: Union[str, core.StringOut] = core.arg()
