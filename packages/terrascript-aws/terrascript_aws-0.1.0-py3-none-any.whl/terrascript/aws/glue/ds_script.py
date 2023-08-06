from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Args(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    param: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        param: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Args.Args(
                name=name,
                value=value,
                param=param,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        param: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class DagNode(core.Schema):

    args: Union[List[Args], core.ArrayOut[Args]] = core.attr(Args, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str)

    line_number: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    node_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        args: Union[List[Args], core.ArrayOut[Args]],
        id: Union[str, core.StringOut],
        node_type: Union[str, core.StringOut],
        line_number: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DagNode.Args(
                args=args,
                id=id,
                node_type=node_type,
                line_number=line_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        args: Union[List[Args], core.ArrayOut[Args]] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        line_number: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        node_type: Union[str, core.StringOut] = core.arg()


@core.schema
class DagEdge(core.Schema):

    source: Union[str, core.StringOut] = core.attr(str)

    target: Union[str, core.StringOut] = core.attr(str)

    target_parameter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        source: Union[str, core.StringOut],
        target: Union[str, core.StringOut],
        target_parameter: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DagEdge.Args(
                source=source,
                target=target,
                target_parameter=target_parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source: Union[str, core.StringOut] = core.arg()

        target: Union[str, core.StringOut] = core.arg()

        target_parameter: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.data(type="aws_glue_script", namespace="aws_glue")
class DsScript(core.Data):

    dag_edge: Union[List[DagEdge], core.ArrayOut[DagEdge]] = core.attr(
        DagEdge, kind=core.Kind.array
    )

    dag_node: Union[List[DagNode], core.ArrayOut[DagNode]] = core.attr(
        DagNode, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    python_script: Union[str, core.StringOut] = core.attr(str, computed=True)

    scala_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        dag_edge: Union[List[DagEdge], core.ArrayOut[DagEdge]],
        dag_node: Union[List[DagNode], core.ArrayOut[DagNode]],
        language: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsScript.Args(
                dag_edge=dag_edge,
                dag_node=dag_node,
                language=language,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dag_edge: Union[List[DagEdge], core.ArrayOut[DagEdge]] = core.arg()

        dag_node: Union[List[DagNode], core.ArrayOut[DagNode]] = core.arg()

        language: Optional[Union[str, core.StringOut]] = core.arg(default=None)
