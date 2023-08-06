from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_imagebuilder_component", namespace="aws_imagebuilder")
class Component(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    change_description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str)

    supported_os_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        platform: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
        change_description: Optional[Union[str, core.StringOut]] = None,
        data: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        supported_os_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        uri: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Component.Args(
                name=name,
                platform=platform,
                version=version,
                change_description=change_description,
                data=data,
                description=description,
                kms_key_id=kms_key_id,
                supported_os_versions=supported_os_versions,
                tags=tags,
                tags_all=tags_all,
                uri=uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        change_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        platform: Union[str, core.StringOut] = core.arg()

        supported_os_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Union[str, core.StringOut] = core.arg()
