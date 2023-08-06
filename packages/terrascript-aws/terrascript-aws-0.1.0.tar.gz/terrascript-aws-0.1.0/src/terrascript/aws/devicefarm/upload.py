from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_devicefarm_upload", namespace="aws_devicefarm")
class Upload(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    category: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    metadata: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    project_arn: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        project_arn: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        content_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Upload.Args(
                name=name,
                project_arn=project_arn,
                type=type,
                content_type=content_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        project_arn: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()
