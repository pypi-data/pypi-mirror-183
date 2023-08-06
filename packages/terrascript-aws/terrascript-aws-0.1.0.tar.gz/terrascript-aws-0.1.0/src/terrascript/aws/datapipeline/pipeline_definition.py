from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ParameterValue(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str)

    string_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        string_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ParameterValue.Args(
                id=id,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        string_value: Union[str, core.StringOut] = core.arg()


@core.schema
class Field(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    ref_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    string_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        ref_value: Optional[Union[str, core.StringOut]] = None,
        string_value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Field.Args(
                key=key,
                ref_value=ref_value,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        ref_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        string_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PipelineObject(core.Schema):

    field: Optional[Union[List[Field], core.ArrayOut[Field]]] = core.attr(
        Field, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        field: Optional[Union[List[Field], core.ArrayOut[Field]]] = None,
    ):
        super().__init__(
            args=PipelineObject.Args(
                id=id,
                name=name,
                field=field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field: Optional[Union[List[Field], core.ArrayOut[Field]]] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Attribute(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    string_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        string_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attribute.Args(
                key=key,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        string_value: Union[str, core.StringOut] = core.arg()


@core.schema
class ParameterObject(core.Schema):

    attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = core.attr(
        Attribute, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = None,
    ):
        super().__init__(
            args=ParameterObject.Args(
                id=id,
                attribute=attribute,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = core.arg(
            default=None
        )

        id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_datapipeline_pipeline_definition", namespace="aws_datapipeline")
class PipelineDefinition(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameter_object: Optional[
        Union[List[ParameterObject], core.ArrayOut[ParameterObject]]
    ] = core.attr(ParameterObject, default=None, kind=core.Kind.array)

    parameter_value: Optional[
        Union[List[ParameterValue], core.ArrayOut[ParameterValue]]
    ] = core.attr(ParameterValue, default=None, kind=core.Kind.array)

    pipeline_id: Union[str, core.StringOut] = core.attr(str)

    pipeline_object: Union[List[PipelineObject], core.ArrayOut[PipelineObject]] = core.attr(
        PipelineObject, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        pipeline_id: Union[str, core.StringOut],
        pipeline_object: Union[List[PipelineObject], core.ArrayOut[PipelineObject]],
        parameter_object: Optional[
            Union[List[ParameterObject], core.ArrayOut[ParameterObject]]
        ] = None,
        parameter_value: Optional[
            Union[List[ParameterValue], core.ArrayOut[ParameterValue]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PipelineDefinition.Args(
                pipeline_id=pipeline_id,
                pipeline_object=pipeline_object,
                parameter_object=parameter_object,
                parameter_value=parameter_value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        parameter_object: Optional[
            Union[List[ParameterObject], core.ArrayOut[ParameterObject]]
        ] = core.arg(default=None)

        parameter_value: Optional[
            Union[List[ParameterValue], core.ArrayOut[ParameterValue]]
        ] = core.arg(default=None)

        pipeline_id: Union[str, core.StringOut] = core.arg()

        pipeline_object: Union[List[PipelineObject], core.ArrayOut[PipelineObject]] = core.arg()
