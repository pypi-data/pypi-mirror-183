from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_s3control_access_point_policy", namespace="aws_s3control")
class AccessPointPolicy(core.Resource):

    access_point_arn: Union[str, core.StringOut] = core.attr(str)

    has_public_access_policy: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_point_arn: Union[str, core.StringOut],
        policy: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessPointPolicy.Args(
                access_point_arn=access_point_arn,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_point_arn: Union[str, core.StringOut] = core.arg()

        policy: Union[str, core.StringOut] = core.arg()
