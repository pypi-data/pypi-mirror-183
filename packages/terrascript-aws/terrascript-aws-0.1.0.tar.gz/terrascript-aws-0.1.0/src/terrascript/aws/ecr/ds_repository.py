from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        encryption_type: Union[str, core.StringOut],
        kms_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_type=encryption_type,
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: Union[str, core.StringOut] = core.arg()

        kms_key: Union[str, core.StringOut] = core.arg()


@core.schema
class ImageScanningConfiguration(core.Schema):

    scan_on_push: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

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


@core.data(type="aws_ecr_repository", namespace="aws_ecr")
class DsRepository(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_configuration: Union[
        List[EncryptionConfiguration], core.ArrayOut[EncryptionConfiguration]
    ] = core.attr(EncryptionConfiguration, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_scanning_configuration: Union[
        List[ImageScanningConfiguration], core.ArrayOut[ImageScanningConfiguration]
    ] = core.attr(ImageScanningConfiguration, computed=True, kind=core.Kind.array)

    image_tag_mutability: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    registry_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    repository_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        registry_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRepository.Args(
                name=name,
                registry_id=registry_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        registry_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
