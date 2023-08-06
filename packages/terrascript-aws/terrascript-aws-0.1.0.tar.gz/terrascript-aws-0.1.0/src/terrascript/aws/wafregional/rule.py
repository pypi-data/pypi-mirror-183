from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Predicate(core.Schema):

    data_id: Union[str, core.StringOut] = core.attr(str)

    negated: Union[bool, core.BoolOut] = core.attr(bool)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        data_id: Union[str, core.StringOut],
        negated: Union[bool, core.BoolOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Predicate.Args(
                data_id=data_id,
                negated=negated,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_id: Union[str, core.StringOut] = core.arg()

        negated: Union[bool, core.BoolOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_rule", namespace="aws_wafregional")
class Rule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    metric_name: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    predicate: Optional[Union[List[Predicate], core.ArrayOut[Predicate]]] = core.attr(
        Predicate, default=None, kind=core.Kind.array
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
        metric_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        predicate: Optional[Union[List[Predicate], core.ArrayOut[Predicate]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Rule.Args(
                metric_name=metric_name,
                name=name,
                predicate=predicate,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        metric_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        predicate: Optional[Union[List[Predicate], core.ArrayOut[Predicate]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
