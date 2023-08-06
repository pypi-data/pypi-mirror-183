from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_grafana_role_association", namespace="aws_grafana")
class RoleAssociation(core.Resource):

    group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role: Union[str, core.StringOut] = core.attr(str)

    user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    workspace_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        role: Union[str, core.StringOut],
        workspace_id: Union[str, core.StringOut],
        group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoleAssociation.Args(
                role=role,
                workspace_id=workspace_id,
                group_ids=group_ids,
                user_ids=user_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        role: Union[str, core.StringOut] = core.arg()

        user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        workspace_id: Union[str, core.StringOut] = core.arg()
