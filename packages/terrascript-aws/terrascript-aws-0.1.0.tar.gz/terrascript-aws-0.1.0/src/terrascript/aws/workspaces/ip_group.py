from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Rules(core.Schema):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Rules.Args(
                source=source,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_workspaces_ip_group", namespace="aws_workspaces")
class IpGroup(core.Resource):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rules: Optional[Union[List[Rules], core.ArrayOut[Rules]]] = core.attr(
        Rules, default=None, kind=core.Kind.array
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
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        rules: Optional[Union[List[Rules], core.ArrayOut[Rules]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IpGroup.Args(
                name=name,
                description=description,
                rules=rules,
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

        name: Union[str, core.StringOut] = core.arg()

        rules: Optional[Union[List[Rules], core.ArrayOut[Rules]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
