from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_elasticache_user_group_association", namespace="aws_elasticache")
class UserGroupAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_group_id: Union[str, core.StringOut] = core.attr(str)

    user_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_group_id: Union[str, core.StringOut],
        user_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroupAssociation.Args(
                user_group_id=user_group_id,
                user_id=user_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        user_group_id: Union[str, core.StringOut] = core.arg()

        user_id: Union[str, core.StringOut] = core.arg()
