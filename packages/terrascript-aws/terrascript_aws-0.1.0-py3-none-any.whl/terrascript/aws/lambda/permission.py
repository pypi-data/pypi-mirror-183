from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lambda_permission", namespace="aws_lambda")
class Permission(core.Resource):

    action: Union[str, core.StringOut] = core.attr(str)

    event_source_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    function_name: Union[str, core.StringOut] = core.attr(str)

    function_url_auth_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal: Union[str, core.StringOut] = core.attr(str)

    principal_org_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_account: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    statement_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    statement_id_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        action: Union[str, core.StringOut],
        function_name: Union[str, core.StringOut],
        principal: Union[str, core.StringOut],
        event_source_token: Optional[Union[str, core.StringOut]] = None,
        function_url_auth_type: Optional[Union[str, core.StringOut]] = None,
        principal_org_id: Optional[Union[str, core.StringOut]] = None,
        qualifier: Optional[Union[str, core.StringOut]] = None,
        source_account: Optional[Union[str, core.StringOut]] = None,
        source_arn: Optional[Union[str, core.StringOut]] = None,
        statement_id: Optional[Union[str, core.StringOut]] = None,
        statement_id_prefix: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                action=action,
                function_name=function_name,
                principal=principal,
                event_source_token=event_source_token,
                function_url_auth_type=function_url_auth_type,
                principal_org_id=principal_org_id,
                qualifier=qualifier,
                source_account=source_account,
                source_arn=source_arn,
                statement_id=statement_id,
                statement_id_prefix=statement_id_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[str, core.StringOut] = core.arg()

        event_source_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        function_name: Union[str, core.StringOut] = core.arg()

        function_url_auth_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        principal: Union[str, core.StringOut] = core.arg()

        principal_org_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_account: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        statement_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        statement_id_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
