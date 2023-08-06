from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ses_identity_policy", namespace="aws_ses")
class IdentityPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        identity: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        policy: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityPolicy.Args(
                identity=identity,
                name=name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        policy: Union[str, core.StringOut] = core.arg()
