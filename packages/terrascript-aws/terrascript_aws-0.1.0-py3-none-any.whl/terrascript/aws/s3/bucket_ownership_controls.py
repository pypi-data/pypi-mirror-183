from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Rule(core.Schema):

    object_ownership: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        object_ownership: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Rule.Args(
                object_ownership=object_ownership,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object_ownership: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3_bucket_ownership_controls", namespace="aws_s3")
class BucketOwnershipControls(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule: Rule = core.attr(Rule)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        rule: Rule,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketOwnershipControls.Args(
                bucket=bucket,
                rule=rule,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        rule: Rule = core.arg()
