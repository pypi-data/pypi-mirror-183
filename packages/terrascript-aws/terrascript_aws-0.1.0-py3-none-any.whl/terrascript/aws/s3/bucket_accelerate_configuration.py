from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_s3_bucket_accelerate_configuration", namespace="aws_s3")
class BucketAccelerateConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketAccelerateConfiguration.Args(
                bucket=bucket,
                status=status,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()
