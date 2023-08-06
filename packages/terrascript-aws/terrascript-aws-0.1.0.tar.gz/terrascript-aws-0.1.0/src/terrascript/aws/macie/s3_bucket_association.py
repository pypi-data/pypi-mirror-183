from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ClassificationType(core.Schema):

    continuous: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    one_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        continuous: Optional[Union[str, core.StringOut]] = None,
        one_time: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ClassificationType.Args(
                continuous=continuous,
                one_time=one_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        continuous: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        one_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_macie_s3_bucket_association", namespace="aws_macie")
class S3BucketAssociation(core.Resource):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    classification_type: Optional[ClassificationType] = core.attr(
        ClassificationType, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    member_account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket_name: Union[str, core.StringOut],
        classification_type: Optional[ClassificationType] = None,
        member_account_id: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=S3BucketAssociation.Args(
                bucket_name=bucket_name,
                classification_type=classification_type,
                member_account_id=member_account_id,
                prefix=prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket_name: Union[str, core.StringOut] = core.arg()

        classification_type: Optional[ClassificationType] = core.arg(default=None)

        member_account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
