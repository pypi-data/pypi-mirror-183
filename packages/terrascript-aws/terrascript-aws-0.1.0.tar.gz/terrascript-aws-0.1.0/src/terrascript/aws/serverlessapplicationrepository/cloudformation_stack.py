from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_serverlessapplicationrepository_cloudformation_stack",
    namespace="aws_serverlessapplicationrepository",
)
class CloudformationStack(core.Resource):

    application_id: Union[str, core.StringOut] = core.attr(str)

    capabilities: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    outputs: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    semantic_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
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
        application_id: Union[str, core.StringOut],
        capabilities: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        semantic_version: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudformationStack.Args(
                application_id=application_id,
                capabilities=capabilities,
                name=name,
                parameters=parameters,
                semantic_version=semantic_version,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        capabilities: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        semantic_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
