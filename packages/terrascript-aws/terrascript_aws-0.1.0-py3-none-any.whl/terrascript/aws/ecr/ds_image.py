from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_ecr_image", namespace="aws_ecr")
class DsImage(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_digest: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    image_pushed_at: Union[int, core.IntOut] = core.attr(int, computed=True)

    image_size_in_bytes: Union[int, core.IntOut] = core.attr(int, computed=True)

    image_tag: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    image_tags: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    registry_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    repository_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: Union[str, core.StringOut],
        image_digest: Optional[Union[str, core.StringOut]] = None,
        image_tag: Optional[Union[str, core.StringOut]] = None,
        registry_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImage.Args(
                repository_name=repository_name,
                image_digest=image_digest,
                image_tag=image_tag,
                registry_id=registry_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_digest: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_tag: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        registry_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        repository_name: Union[str, core.StringOut] = core.arg()
