from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_codebuild_source_credential", namespace="aws_codebuild")
class SourceCredential(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auth_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    server_type: Union[str, core.StringOut] = core.attr(str)

    token: Union[str, core.StringOut] = core.attr(str)

    user_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_type: Union[str, core.StringOut],
        server_type: Union[str, core.StringOut],
        token: Union[str, core.StringOut],
        user_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SourceCredential.Args(
                auth_type=auth_type,
                server_type=server_type,
                token=token,
                user_name=user_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_type: Union[str, core.StringOut] = core.arg()

        server_type: Union[str, core.StringOut] = core.arg()

        token: Union[str, core.StringOut] = core.arg()

        user_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
