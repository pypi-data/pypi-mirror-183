from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class DelegatedAdministratorsBlk(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delegation_enabled_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    email: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    joined_method: Union[str, core.StringOut] = core.attr(str, computed=True)

    joined_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        delegation_enabled_date: Union[str, core.StringOut],
        email: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        joined_method: Union[str, core.StringOut],
        joined_timestamp: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DelegatedAdministratorsBlk.Args(
                arn=arn,
                delegation_enabled_date=delegation_enabled_date,
                email=email,
                id=id,
                joined_method=joined_method,
                joined_timestamp=joined_timestamp,
                name=name,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        delegation_enabled_date: Union[str, core.StringOut] = core.arg()

        email: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        joined_method: Union[str, core.StringOut] = core.arg()

        joined_timestamp: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_organizations_delegated_administrators", namespace="aws_organizations")
class DsDelegatedAdministrators(core.Data):

    delegated_administrators: Union[
        List[DelegatedAdministratorsBlk], core.ArrayOut[DelegatedAdministratorsBlk]
    ] = core.attr(DelegatedAdministratorsBlk, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_principal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        service_principal: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDelegatedAdministrators.Args(
                service_principal=service_principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        service_principal: Optional[Union[str, core.StringOut]] = core.arg(default=None)
