from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_sagemaker_prebuilt_ecr_image", namespace="aws_sagemaker")
class DsPrebuiltEcrImage(core.Data):

    dns_suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_tag: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    registry_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    registry_path: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: Union[str, core.StringOut],
        dns_suffix: Optional[Union[str, core.StringOut]] = None,
        image_tag: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPrebuiltEcrImage.Args(
                repository_name=repository_name,
                dns_suffix=dns_suffix,
                image_tag=image_tag,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_tag: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        repository_name: Union[str, core.StringOut] = core.arg()
