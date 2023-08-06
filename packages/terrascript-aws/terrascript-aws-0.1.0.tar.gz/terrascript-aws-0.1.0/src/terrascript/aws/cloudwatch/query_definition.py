from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_query_definition", namespace="aws_cloudwatch")
class QueryDefinition(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    query_definition_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    query_string: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        query_string: Union[str, core.StringOut],
        log_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueryDefinition.Args(
                name=name,
                query_string=query_string,
                log_group_names=log_group_names,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        query_string: Union[str, core.StringOut] = core.arg()
