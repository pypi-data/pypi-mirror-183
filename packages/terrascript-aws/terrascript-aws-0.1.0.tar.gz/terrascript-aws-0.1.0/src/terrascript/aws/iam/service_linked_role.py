from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_service_linked_role", namespace="aws_iam")
class ServiceLinkedRole(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_service_name: Union[str, core.StringOut] = core.attr(str)

    create_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    custom_suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    unique_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        aws_service_name: Union[str, core.StringOut],
        custom_suffix: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceLinkedRole.Args(
                aws_service_name=aws_service_name,
                custom_suffix=custom_suffix,
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
        aws_service_name: Union[str, core.StringOut] = core.arg()

        custom_suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
