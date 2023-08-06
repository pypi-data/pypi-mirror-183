from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InputParameter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InputParameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Scope(core.Schema):

    compliance_resource_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compliance_resource_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_resource_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        compliance_resource_types: Union[List[str], core.ArrayOut[core.StringOut]],
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
        compliance_resource_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        compliance_resource_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Control(core.Schema):

    input_parameter: Union[List[InputParameter], core.ArrayOut[InputParameter]] = core.attr(
        InputParameter, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    scope: Union[List[Scope], core.ArrayOut[Scope]] = core.attr(
        Scope, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        input_parameter: Union[List[InputParameter], core.ArrayOut[InputParameter]],
        name: Union[str, core.StringOut],
        scope: Union[List[Scope], core.ArrayOut[Scope]],
    ):
        super().__init__(
            args=Control.Args(
                input_parameter=input_parameter,
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_parameter: Union[List[InputParameter], core.ArrayOut[InputParameter]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        scope: Union[List[Scope], core.ArrayOut[Scope]] = core.arg()


@core.data(type="aws_backup_framework", namespace="aws_backup")
class DsFramework(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    control: Union[List[Control], core.ArrayOut[Control]] = core.attr(
        Control, computed=True, kind=core.Kind.array
    )

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFramework.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
