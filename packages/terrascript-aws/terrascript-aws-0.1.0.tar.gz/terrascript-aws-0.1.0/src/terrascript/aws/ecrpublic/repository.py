from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CatalogData(core.Schema):

    about_text: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    logo_image_blob: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    operating_systems: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    usage_text: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        about_text: Optional[Union[str, core.StringOut]] = None,
        architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        logo_image_blob: Optional[Union[str, core.StringOut]] = None,
        operating_systems: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        usage_text: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CatalogData.Args(
                about_text=about_text,
                architectures=architectures,
                description=description,
                logo_image_blob=logo_image_blob,
                operating_systems=operating_systems,
                usage_text=usage_text,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        about_text: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logo_image_blob: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operating_systems: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        usage_text: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ecrpublic_repository", namespace="aws_ecrpublic")
class Repository(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_data: Optional[CatalogData] = core.attr(CatalogData, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    registry_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository_name: Union[str, core.StringOut] = core.attr(str)

    repository_uri: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        repository_name: Union[str, core.StringOut],
        catalog_data: Optional[CatalogData] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Repository.Args(
                repository_name=repository_name,
                catalog_data=catalog_data,
                force_destroy=force_destroy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_data: Optional[CatalogData] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        repository_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
