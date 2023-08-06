from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_connect_contact_flow", namespace="aws_connect")
class ContactFlow(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    contact_flow_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    content: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    content_hash: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filename: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        content: Optional[Union[str, core.StringOut]] = None,
        content_hash: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        filename: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContactFlow.Args(
                instance_id=instance_id,
                name=name,
                content=content,
                content_hash=content_hash,
                description=description,
                filename=filename,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_hash: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filename: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
