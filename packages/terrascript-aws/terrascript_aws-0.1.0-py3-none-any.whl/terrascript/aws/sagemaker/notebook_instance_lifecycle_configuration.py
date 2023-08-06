from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_sagemaker_notebook_instance_lifecycle_configuration", namespace="aws_sagemaker"
)
class NotebookInstanceLifecycleConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    on_create: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    on_start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        on_create: Optional[Union[str, core.StringOut]] = None,
        on_start: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NotebookInstanceLifecycleConfiguration.Args(
                name=name,
                on_create=on_create,
                on_start=on_start,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_create: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_start: Optional[Union[str, core.StringOut]] = core.arg(default=None)
