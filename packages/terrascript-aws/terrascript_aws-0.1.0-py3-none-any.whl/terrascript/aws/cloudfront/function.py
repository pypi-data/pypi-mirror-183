from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudfront_function", namespace="aws_cloudfront")
class Function(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    code: Union[str, core.StringOut] = core.attr(str)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    live_stage_etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    publish: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    runtime: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        code: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        runtime: Union[str, core.StringOut],
        comment: Optional[Union[str, core.StringOut]] = None,
        publish: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Function.Args(
                code=code,
                name=name,
                runtime=runtime,
                comment=comment,
                publish=publish,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        code: Union[str, core.StringOut] = core.arg()

        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        publish: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        runtime: Union[str, core.StringOut] = core.arg()
