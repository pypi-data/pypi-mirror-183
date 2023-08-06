from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ConstraintSummaries(core.Schema):

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        description: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConstraintSummaries.Args(
                description=description,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Summaries(core.Schema):

    constraint_summaries: Union[
        List[ConstraintSummaries], core.ArrayOut[ConstraintSummaries]
    ] = core.attr(ConstraintSummaries, computed=True, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    path_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        constraint_summaries: Union[List[ConstraintSummaries], core.ArrayOut[ConstraintSummaries]],
        name: Union[str, core.StringOut],
        path_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Summaries.Args(
                constraint_summaries=constraint_summaries,
                name=name,
                path_id=path_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        constraint_summaries: Union[
            List[ConstraintSummaries], core.ArrayOut[ConstraintSummaries]
        ] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        path_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.data(type="aws_servicecatalog_launch_paths", namespace="aws_servicecatalog")
class DsLaunchPaths(core.Data):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    product_id: Union[str, core.StringOut] = core.attr(str)

    summaries: Union[List[Summaries], core.ArrayOut[Summaries]] = core.attr(
        Summaries, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        product_id: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLaunchPaths.Args(
                product_id=product_id,
                accept_language=accept_language,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        product_id: Union[str, core.StringOut] = core.arg()
