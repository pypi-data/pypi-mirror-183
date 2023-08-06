from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Scope(core.Schema):

    compliance_resource_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    compliance_resource_types: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_resource_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        compliance_resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Scope.Args(
                compliance_resource_ids=compliance_resource_ids,
                compliance_resource_types=compliance_resource_types,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_resource_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        compliance_resource_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class InputParameter(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InputParameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Control(core.Schema):

    input_parameter: Optional[
        Union[List[InputParameter], core.ArrayOut[InputParameter]]
    ] = core.attr(InputParameter, default=None, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    scope: Optional[Scope] = core.attr(Scope, default=None)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        input_parameter: Optional[
            Union[List[InputParameter], core.ArrayOut[InputParameter]]
        ] = None,
        scope: Optional[Scope] = None,
    ):
        super().__init__(
            args=Control.Args(
                name=name,
                input_parameter=input_parameter,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_parameter: Optional[
            Union[List[InputParameter], core.ArrayOut[InputParameter]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        scope: Optional[Scope] = core.arg(default=None)


@core.resource(type="aws_backup_framework", namespace="aws_backup")
class Framework(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    control: Union[List[Control], core.ArrayOut[Control]] = core.attr(Control, kind=core.Kind.array)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        control: Union[List[Control], core.ArrayOut[Control]],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Framework.Args(
                control=control,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        control: Union[List[Control], core.ArrayOut[Control]] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
