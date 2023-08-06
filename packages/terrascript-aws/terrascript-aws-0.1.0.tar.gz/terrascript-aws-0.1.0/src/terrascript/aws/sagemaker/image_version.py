from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sagemaker_image_version", namespace="aws_sagemaker")
class ImageVersion(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    base_image: Union[str, core.StringOut] = core.attr(str)

    container_image: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_name: Union[str, core.StringOut] = core.attr(str)

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        base_image: Union[str, core.StringOut],
        image_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImageVersion.Args(
                base_image=base_image,
                image_name=image_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        base_image: Union[str, core.StringOut] = core.arg()

        image_name: Union[str, core.StringOut] = core.arg()
