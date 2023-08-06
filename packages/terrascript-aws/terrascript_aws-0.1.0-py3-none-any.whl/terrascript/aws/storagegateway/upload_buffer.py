from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_storagegateway_upload_buffer", namespace="aws_storagegateway")
class UploadBuffer(core.Resource):

    disk_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    disk_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    gateway_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: Union[str, core.StringOut],
        disk_id: Optional[Union[str, core.StringOut]] = None,
        disk_path: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UploadBuffer.Args(
                gateway_arn=gateway_arn,
                disk_id=disk_id,
                disk_path=disk_path,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disk_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disk_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_arn: Union[str, core.StringOut] = core.arg()
