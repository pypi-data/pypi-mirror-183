from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_amplify_backend_environment", namespace="aws_amplify")
class BackendEnvironment(core.Resource):

    app_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_artifacts: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    environment_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    stack_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: Union[str, core.StringOut],
        environment_name: Union[str, core.StringOut],
        deployment_artifacts: Optional[Union[str, core.StringOut]] = None,
        stack_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BackendEnvironment.Args(
                app_id=app_id,
                environment_name=environment_name,
                deployment_artifacts=deployment_artifacts,
                stack_name=stack_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: Union[str, core.StringOut] = core.arg()

        deployment_artifacts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment_name: Union[str, core.StringOut] = core.arg()

        stack_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
