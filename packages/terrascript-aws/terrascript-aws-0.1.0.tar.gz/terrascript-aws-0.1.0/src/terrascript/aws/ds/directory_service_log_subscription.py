from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_directory_service_log_subscription", namespace="aws_ds")
class DirectoryServiceLogSubscription(core.Resource):

    directory_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        log_group_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceLogSubscription.Args(
                directory_id=directory_id,
                log_group_name=log_group_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: Union[str, core.StringOut] = core.arg()

        log_group_name: Union[str, core.StringOut] = core.arg()
