from typing import Union

import terrascript.core as core


@core.data(type="aws_cloudfront_function", namespace="aws_cloudfront")
class DsFunction(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    code: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Union[str, core.StringOut] = core.attr(str, computed=True)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    runtime: Union[str, core.StringOut] = core.attr(str, computed=True)

    stage: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        stage: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsFunction.Args(
                name=name,
                stage=stage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        stage: Union[str, core.StringOut] = core.arg()
