from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_codeartifact_domain_permissions_policy", namespace="aws_codeartifact")
class DomainPermissionsPolicy(core.Resource):

    domain: Union[str, core.StringOut] = core.attr(str)

    domain_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy_document: Union[str, core.StringOut] = core.attr(str)

    policy_revision: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain: Union[str, core.StringOut],
        policy_document: Union[str, core.StringOut],
        domain_owner: Optional[Union[str, core.StringOut]] = None,
        policy_revision: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainPermissionsPolicy.Args(
                domain=domain,
                policy_document=policy_document,
                domain_owner=domain_owner,
                policy_revision=policy_revision,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: Union[str, core.StringOut] = core.arg()

        domain_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy_document: Union[str, core.StringOut] = core.arg()

        policy_revision: Optional[Union[str, core.StringOut]] = core.arg(default=None)
