from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_storagegateway_working_storage", namespace="aws_storagegateway")
class WorkingStorage(core.Resource):

    disk_id: Union[str, core.StringOut] = core.attr(str)

    gateway_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        disk_id: Union[str, core.StringOut],
        gateway_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=WorkingStorage.Args(
                disk_id=disk_id,
                gateway_arn=gateway_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disk_id: Union[str, core.StringOut] = core.arg()

        gateway_arn: Union[str, core.StringOut] = core.arg()
