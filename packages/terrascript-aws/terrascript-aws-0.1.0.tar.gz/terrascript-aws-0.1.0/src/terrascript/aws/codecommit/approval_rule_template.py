from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_codecommit_approval_rule_template", namespace="aws_codecommit")
class ApprovalRuleTemplate(core.Resource):

    approval_rule_template_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    content: Union[str, core.StringOut] = core.attr(str)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_user: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule_content_sha256: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        content: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApprovalRuleTemplate.Args(
                content=content,
                name=name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
