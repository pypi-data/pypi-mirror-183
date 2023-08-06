from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    apply_method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        apply_method: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
                apply_method=apply_method,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_docdb_cluster_parameter_group", namespace="aws_docdb")
class ClusterParameterGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    family: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

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
        family: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterParameterGroup.Args(
                family=family,
                description=description,
                name=name,
                name_prefix=name_prefix,
                parameter=parameter,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        family: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
