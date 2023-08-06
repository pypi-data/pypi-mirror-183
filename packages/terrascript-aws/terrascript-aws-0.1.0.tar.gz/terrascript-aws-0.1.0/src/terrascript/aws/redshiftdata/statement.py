from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Parameters(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Parameters.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_redshiftdata_statement", namespace="aws_redshiftdata")
class Statement(core.Resource):

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    database: Union[str, core.StringOut] = core.attr(str)

    db_user: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameters: Optional[Union[List[Parameters], core.ArrayOut[Parameters]]] = core.attr(
        Parameters, default=None, kind=core.Kind.array
    )

    secret_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sql: Union[str, core.StringOut] = core.attr(str)

    statement_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    with_event: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        database: Union[str, core.StringOut],
        sql: Union[str, core.StringOut],
        db_user: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[List[Parameters], core.ArrayOut[Parameters]]] = None,
        secret_arn: Optional[Union[str, core.StringOut]] = None,
        statement_name: Optional[Union[str, core.StringOut]] = None,
        with_event: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Statement.Args(
                cluster_identifier=cluster_identifier,
                database=database,
                sql=sql,
                db_user=db_user,
                parameters=parameters,
                secret_arn=secret_arn,
                statement_name=statement_name,
                with_event=with_event,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: Union[str, core.StringOut] = core.arg()

        database: Union[str, core.StringOut] = core.arg()

        db_user: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameters: Optional[Union[List[Parameters], core.ArrayOut[Parameters]]] = core.arg(
            default=None
        )

        secret_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sql: Union[str, core.StringOut] = core.arg()

        statement_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        with_event: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
