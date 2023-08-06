from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_directory_service_shared_directory_accepter", namespace="aws_ds")
class DirectoryServiceSharedDirectoryAccepter(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    method: Union[str, core.StringOut] = core.attr(str, computed=True)

    notes: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_directory_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    shared_directory_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        shared_directory_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceSharedDirectoryAccepter.Args(
                shared_directory_id=shared_directory_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        shared_directory_id: Union[str, core.StringOut] = core.arg()
