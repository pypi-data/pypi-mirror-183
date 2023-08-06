from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_organizations_account", namespace="aws_organizations")
class Account(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    close_on_deletion: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    create_govcloud: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    email: Union[str, core.StringOut] = core.attr(str)

    govcloud_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_user_access_to_billing: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    joined_method: Union[str, core.StringOut] = core.attr(str, computed=True)

    joined_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    parent_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    role_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        email: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        close_on_deletion: Optional[Union[bool, core.BoolOut]] = None,
        create_govcloud: Optional[Union[bool, core.BoolOut]] = None,
        iam_user_access_to_billing: Optional[Union[str, core.StringOut]] = None,
        parent_id: Optional[Union[str, core.StringOut]] = None,
        role_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                email=email,
                name=name,
                close_on_deletion=close_on_deletion,
                create_govcloud=create_govcloud,
                iam_user_access_to_billing=iam_user_access_to_billing,
                parent_id=parent_id,
                role_name=role_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        close_on_deletion: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        create_govcloud: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        email: Union[str, core.StringOut] = core.arg()

        iam_user_access_to_billing: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parent_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
