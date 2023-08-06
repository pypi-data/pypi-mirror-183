from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudfront_origin_access_identity", namespace="aws_cloudfront")
class OriginAccessIdentity(core.Resource):

    caller_reference: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudfront_access_identity_path: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_canonical_user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        comment: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OriginAccessIdentity.Args(
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)
