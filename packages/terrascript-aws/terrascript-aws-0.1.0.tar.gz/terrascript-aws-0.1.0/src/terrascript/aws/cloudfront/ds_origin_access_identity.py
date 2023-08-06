from typing import Union

import terrascript.core as core


@core.data(type="aws_cloudfront_origin_access_identity", namespace="aws_cloudfront")
class DsOriginAccessIdentity(core.Data):

    caller_reference: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudfront_access_identity_path: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Union[str, core.StringOut] = core.attr(str, computed=True)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    s3_canonical_user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsOriginAccessIdentity.Args(
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()
