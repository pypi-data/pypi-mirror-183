from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_emr_studio_session_mapping", namespace="aws_emr")
class StudioSessionMapping(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    identity_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    identity_type: Union[str, core.StringOut] = core.attr(str)

    session_policy_arn: Union[str, core.StringOut] = core.attr(str)

    studio_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_type: Union[str, core.StringOut],
        session_policy_arn: Union[str, core.StringOut],
        studio_id: Union[str, core.StringOut],
        identity_id: Optional[Union[str, core.StringOut]] = None,
        identity_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StudioSessionMapping.Args(
                identity_type=identity_type,
                session_policy_arn=session_policy_arn,
                studio_id=studio_id,
                identity_id=identity_id,
                identity_name=identity_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_type: Union[str, core.StringOut] = core.arg()

        session_policy_arn: Union[str, core.StringOut] = core.arg()

        studio_id: Union[str, core.StringOut] = core.arg()
