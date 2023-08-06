from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        encryption_type: Optional[Union[str, core.StringOut]] = None,
        kms_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_type=encryption_type,
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ImageScanningConfiguration(core.Schema):

    scan_on_push: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        scan_on_push: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ImageScanningConfiguration.Args(
                scan_on_push=scan_on_push,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scan_on_push: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_ecr_repository", namespace="aws_ecr")
class Repository(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_configuration: Optional[
        Union[List[EncryptionConfiguration], core.ArrayOut[EncryptionConfiguration]]
    ] = core.attr(EncryptionConfiguration, default=None, kind=core.Kind.array)

    force_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_scanning_configuration: Optional[ImageScanningConfiguration] = core.attr(
        ImageScanningConfiguration, default=None
    )

    image_tag_mutability: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    registry_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository_url: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        encryption_configuration: Optional[
            Union[List[EncryptionConfiguration], core.ArrayOut[EncryptionConfiguration]]
        ] = None,
        force_delete: Optional[Union[bool, core.BoolOut]] = None,
        image_scanning_configuration: Optional[ImageScanningConfiguration] = None,
        image_tag_mutability: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Repository.Args(
                name=name,
                encryption_configuration=encryption_configuration,
                force_delete=force_delete,
                image_scanning_configuration=image_scanning_configuration,
                image_tag_mutability=image_tag_mutability,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        encryption_configuration: Optional[
            Union[List[EncryptionConfiguration], core.ArrayOut[EncryptionConfiguration]]
        ] = core.arg(default=None)

        force_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        image_scanning_configuration: Optional[ImageScanningConfiguration] = core.arg(default=None)

        image_tag_mutability: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
