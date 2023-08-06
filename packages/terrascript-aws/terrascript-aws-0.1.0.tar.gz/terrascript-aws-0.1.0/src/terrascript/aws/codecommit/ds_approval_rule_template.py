from typing import Union

import terrascript.core as core


@core.data(type="aws_codecommit_approval_rule_template", namespace="aws_codecommit")
class DsApprovalRuleTemplate(core.Data):

    approval_rule_template_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    content: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_user: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule_content_sha256: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsApprovalRuleTemplate.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
