from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_secretsmanager_secret_policy", namespace="aws_secretsmanager")
class SecretPolicy(core.Resource):

    block_public_policy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    secret_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        secret_arn: Union[str, core.StringOut],
        block_public_policy: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretPolicy.Args(
                policy=policy,
                secret_arn=secret_arn,
                block_public_policy=block_public_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_public_policy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy: Union[str, core.StringOut] = core.arg()

        secret_arn: Union[str, core.StringOut] = core.arg()
