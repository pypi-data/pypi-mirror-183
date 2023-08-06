from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_guardduty_invite_accepter", namespace="aws_guardduty")
class InviteAccepter(core.Resource):

    detector_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_account_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        detector_id: Union[str, core.StringOut],
        master_account_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InviteAccepter.Args(
                detector_id=detector_id,
                master_account_id=master_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        detector_id: Union[str, core.StringOut] = core.arg()

        master_account_id: Union[str, core.StringOut] = core.arg()
