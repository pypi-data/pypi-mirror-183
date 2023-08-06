from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_redshiftserverless_namespace", namespace="aws_redshiftserverless")
class Namespace(core.Resource):

    admin_user_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    admin_username: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    default_iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    log_exports: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    namespace_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    namespace_name: Union[str, core.StringOut] = core.attr(str)

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
        namespace_name: Union[str, core.StringOut],
        admin_user_password: Optional[Union[str, core.StringOut]] = None,
        admin_username: Optional[Union[str, core.StringOut]] = None,
        db_name: Optional[Union[str, core.StringOut]] = None,
        default_iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        log_exports: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Namespace.Args(
                namespace_name=namespace_name,
                admin_user_password=admin_user_password,
                admin_username=admin_username,
                db_name=db_name,
                default_iam_role_arn=default_iam_role_arn,
                iam_roles=iam_roles,
                kms_key_id=kms_key_id,
                log_exports=log_exports,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_user_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        admin_username: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_exports: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        namespace_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
