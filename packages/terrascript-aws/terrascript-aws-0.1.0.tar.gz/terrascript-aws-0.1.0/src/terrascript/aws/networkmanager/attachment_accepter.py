from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_networkmanager_attachment_accepter", namespace="aws_networkmanager")
class AttachmentAccepter(core.Resource):

    attachment_id: Union[str, core.StringOut] = core.attr(str)

    attachment_policy_rule_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    attachment_type: Union[str, core.StringOut] = core.attr(str)

    core_network_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    edge_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    segment_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        attachment_id: Union[str, core.StringOut],
        attachment_type: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AttachmentAccepter.Args(
                attachment_id=attachment_id,
                attachment_type=attachment_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachment_id: Union[str, core.StringOut] = core.arg()

        attachment_type: Union[str, core.StringOut] = core.arg()
