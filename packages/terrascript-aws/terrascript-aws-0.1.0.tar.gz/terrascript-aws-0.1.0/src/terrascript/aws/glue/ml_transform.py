from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Schema(core.Schema):

    data_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        data_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Schema.Args(
                data_type=data_type,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_type: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class InputRecordTables(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connection_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    database_name: Union[str, core.StringOut] = core.attr(str)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        database_name: Union[str, core.StringOut],
        table_name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        connection_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InputRecordTables.Args(
                database_name=database_name,
                table_name=table_name,
                catalog_id=catalog_id,
                connection_name=connection_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()


@core.schema
class FindMatchesParameters(core.Schema):

    accuracy_cost_trade_off: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    enforce_provided_labels: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    precision_recall_trade_off: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    primary_key_column_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        accuracy_cost_trade_off: Optional[Union[float, core.FloatOut]] = None,
        enforce_provided_labels: Optional[Union[bool, core.BoolOut]] = None,
        precision_recall_trade_off: Optional[Union[float, core.FloatOut]] = None,
        primary_key_column_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FindMatchesParameters.Args(
                accuracy_cost_trade_off=accuracy_cost_trade_off,
                enforce_provided_labels=enforce_provided_labels,
                precision_recall_trade_off=precision_recall_trade_off,
                primary_key_column_name=primary_key_column_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accuracy_cost_trade_off: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        enforce_provided_labels: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        precision_recall_trade_off: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        primary_key_column_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Parameters(core.Schema):

    find_matches_parameters: FindMatchesParameters = core.attr(FindMatchesParameters)

    transform_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        find_matches_parameters: FindMatchesParameters,
        transform_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Parameters.Args(
                find_matches_parameters=find_matches_parameters,
                transform_type=transform_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        find_matches_parameters: FindMatchesParameters = core.arg()

        transform_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_glue_ml_transform", namespace="aws_glue")
class MlTransform(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    glue_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_record_tables: Union[
        List[InputRecordTables], core.ArrayOut[InputRecordTables]
    ] = core.attr(InputRecordTables, kind=core.Kind.array)

    label_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    max_capacity: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None, computed=True
    )

    max_retries: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    number_of_workers: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    parameters: Parameters = core.attr(Parameters)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    schema: Union[List[Schema], core.ArrayOut[Schema]] = core.attr(
        Schema, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    worker_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        input_record_tables: Union[List[InputRecordTables], core.ArrayOut[InputRecordTables]],
        name: Union[str, core.StringOut],
        parameters: Parameters,
        role_arn: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        glue_version: Optional[Union[str, core.StringOut]] = None,
        max_capacity: Optional[Union[float, core.FloatOut]] = None,
        max_retries: Optional[Union[int, core.IntOut]] = None,
        number_of_workers: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timeout: Optional[Union[int, core.IntOut]] = None,
        worker_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MlTransform.Args(
                input_record_tables=input_record_tables,
                name=name,
                parameters=parameters,
                role_arn=role_arn,
                description=description,
                glue_version=glue_version,
                max_capacity=max_capacity,
                max_retries=max_retries,
                number_of_workers=number_of_workers,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                worker_type=worker_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        glue_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        input_record_tables: Union[
            List[InputRecordTables], core.ArrayOut[InputRecordTables]
        ] = core.arg()

        max_capacity: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        max_retries: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        number_of_workers: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parameters: Parameters = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        worker_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
