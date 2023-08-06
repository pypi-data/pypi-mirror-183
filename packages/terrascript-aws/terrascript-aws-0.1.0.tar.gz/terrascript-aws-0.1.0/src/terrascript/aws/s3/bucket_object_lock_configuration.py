from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class DefaultRetention(core.Schema):

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    years: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        days: Optional[Union[int, core.IntOut]] = None,
        mode: Optional[Union[str, core.StringOut]] = None,
        years: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DefaultRetention.Args(
                days=days,
                mode=mode,
                years=years,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        years: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    default_retention: DefaultRetention = core.attr(DefaultRetention)

    def __init__(
        self,
        *,
        default_retention: DefaultRetention,
    ):
        super().__init__(
            args=Rule.Args(
                default_retention=default_retention,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_retention: DefaultRetention = core.arg()


@core.resource(type="aws_s3_bucket_object_lock_configuration", namespace="aws_s3")
class BucketObjectLockConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    object_lock_enabled: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule: Rule = core.attr(Rule)

    token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        rule: Rule,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        object_lock_enabled: Optional[Union[str, core.StringOut]] = None,
        token: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketObjectLockConfiguration.Args(
                bucket=bucket,
                rule=rule,
                expected_bucket_owner=expected_bucket_owner,
                object_lock_enabled=object_lock_enabled,
                token=token,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_lock_enabled: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule: Rule = core.arg()

        token: Optional[Union[str, core.StringOut]] = core.arg(default=None)
