from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_quicksight_group_membership", namespace="aws_quicksight")
class GroupMembership(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_account_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    member_name: Union[str, core.StringOut] = core.attr(str)

    namespace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: Union[str, core.StringOut],
        member_name: Union[str, core.StringOut],
        aws_account_id: Optional[Union[str, core.StringOut]] = None,
        namespace: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupMembership.Args(
                group_name=group_name,
                member_name=member_name,
                aws_account_id=aws_account_id,
                namespace=namespace,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        group_name: Union[str, core.StringOut] = core.arg()

        member_name: Union[str, core.StringOut] = core.arg()

        namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)
