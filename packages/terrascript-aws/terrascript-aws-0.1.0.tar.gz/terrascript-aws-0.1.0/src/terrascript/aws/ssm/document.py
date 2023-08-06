from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AttachmentsSource(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AttachmentsSource.Args(
                key=key,
                values=values,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Parameter(core.Schema):

    default_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_value: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Parameter.Args(
                default_value=default_value,
                description=description,
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ssm_document", namespace="aws_ssm")
class Document(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attachments_source: Optional[
        Union[List[AttachmentsSource], core.ArrayOut[AttachmentsSource]]
    ] = core.attr(AttachmentsSource, default=None, kind=core.Kind.array)

    content: Union[str, core.StringOut] = core.attr(str)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    document_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_type: Union[str, core.StringOut] = core.attr(str)

    document_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    hash: Union[str, core.StringOut] = core.attr(str, computed=True)

    hash_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameter: Union[List[Parameter], core.ArrayOut[Parameter]] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    permissions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    platform_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    schema_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content: Union[str, core.StringOut],
        document_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        attachments_source: Optional[
            Union[List[AttachmentsSource], core.ArrayOut[AttachmentsSource]]
        ] = None,
        document_format: Optional[Union[str, core.StringOut]] = None,
        permissions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_type: Optional[Union[str, core.StringOut]] = None,
        version_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Document.Args(
                content=content,
                document_type=document_type,
                name=name,
                attachments_source=attachments_source,
                document_format=document_format,
                permissions=permissions,
                tags=tags,
                tags_all=tags_all,
                target_type=target_type,
                version_name=version_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachments_source: Optional[
            Union[List[AttachmentsSource], core.ArrayOut[AttachmentsSource]]
        ] = core.arg(default=None)

        content: Union[str, core.StringOut] = core.arg()

        document_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_type: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        permissions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
