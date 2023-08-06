from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_athena_named_query", namespace="aws_athena")
class NamedQuery(core.Resource):

    database: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    query: Union[str, core.StringOut] = core.attr(str)

    workgroup: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        database: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        query: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        workgroup: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NamedQuery.Args(
                database=database,
                name=name,
                query=query,
                description=description,
                workgroup=workgroup,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        query: Union[str, core.StringOut] = core.arg()

        workgroup: Optional[Union[str, core.StringOut]] = core.arg(default=None)
