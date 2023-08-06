from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class UserPausedDetails(core.Schema):

    job_expires_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_imminent_expiration_health_event_arn: Union[str, core.StringOut] = core.attr(
        str, computed=True
    )

    job_paused_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        job_expires_at: Union[str, core.StringOut],
        job_imminent_expiration_health_event_arn: Union[str, core.StringOut],
        job_paused_at: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserPausedDetails.Args(
                job_expires_at=job_expires_at,
                job_imminent_expiration_health_event_arn=job_imminent_expiration_health_event_arn,
                job_paused_at=job_paused_at,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        job_expires_at: Union[str, core.StringOut] = core.arg()

        job_imminent_expiration_health_event_arn: Union[str, core.StringOut] = core.arg()

        job_paused_at: Union[str, core.StringOut] = core.arg()


@core.schema
class SimpleCriterion(core.Schema):

    comparator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparator: Optional[Union[str, core.StringOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=SimpleCriterion.Args(
                comparator=comparator,
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class TagValues(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TagValues.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TagCriterion(core.Schema):

    comparator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = core.attr(
        TagValues, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparator: Optional[Union[str, core.StringOut]] = None,
        tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = None,
    ):
        super().__init__(
            args=TagCriterion.Args(
                comparator=comparator,
                tag_values=tag_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = core.arg(
            default=None
        )


@core.schema
class BucketCriteriaExcludesAnd(core.Schema):

    simple_criterion: Optional[SimpleCriterion] = core.attr(
        SimpleCriterion, default=None, computed=True
    )

    tag_criterion: Optional[TagCriterion] = core.attr(TagCriterion, default=None, computed=True)

    def __init__(
        self,
        *,
        simple_criterion: Optional[SimpleCriterion] = None,
        tag_criterion: Optional[TagCriterion] = None,
    ):
        super().__init__(
            args=BucketCriteriaExcludesAnd.Args(
                simple_criterion=simple_criterion,
                tag_criterion=tag_criterion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        simple_criterion: Optional[SimpleCriterion] = core.arg(default=None)

        tag_criterion: Optional[TagCriterion] = core.arg(default=None)


@core.schema
class BucketCriteriaExcludes(core.Schema):

    and_: Optional[
        Union[List[BucketCriteriaExcludesAnd], core.ArrayOut[BucketCriteriaExcludesAnd]]
    ] = core.attr(
        BucketCriteriaExcludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: Optional[
            Union[List[BucketCriteriaExcludesAnd], core.ArrayOut[BucketCriteriaExcludesAnd]]
        ] = None,
    ):
        super().__init__(
            args=BucketCriteriaExcludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[
            Union[List[BucketCriteriaExcludesAnd], core.ArrayOut[BucketCriteriaExcludesAnd]]
        ] = core.arg(default=None)


@core.schema
class BucketCriteriaIncludes(core.Schema):

    and_: Optional[
        Union[List[BucketCriteriaExcludesAnd], core.ArrayOut[BucketCriteriaExcludesAnd]]
    ] = core.attr(
        BucketCriteriaExcludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: Optional[
            Union[List[BucketCriteriaExcludesAnd], core.ArrayOut[BucketCriteriaExcludesAnd]]
        ] = None,
    ):
        super().__init__(
            args=BucketCriteriaIncludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[
            Union[List[BucketCriteriaExcludesAnd], core.ArrayOut[BucketCriteriaExcludesAnd]]
        ] = core.arg(default=None)


@core.schema
class BucketCriteria(core.Schema):

    excludes: Optional[BucketCriteriaExcludes] = core.attr(
        BucketCriteriaExcludes, default=None, computed=True
    )

    includes: Optional[BucketCriteriaIncludes] = core.attr(
        BucketCriteriaIncludes, default=None, computed=True
    )

    def __init__(
        self,
        *,
        excludes: Optional[BucketCriteriaExcludes] = None,
        includes: Optional[BucketCriteriaIncludes] = None,
    ):
        super().__init__(
            args=BucketCriteria.Args(
                excludes=excludes,
                includes=includes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        excludes: Optional[BucketCriteriaExcludes] = core.arg(default=None)

        includes: Optional[BucketCriteriaIncludes] = core.arg(default=None)


@core.schema
class SimpleScopeTerm(core.Schema):

    comparator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparator: Optional[Union[str, core.StringOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=SimpleScopeTerm.Args(
                comparator=comparator,
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class ScopingExcludesAndTagScopeTerm(core.Schema):

    comparator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = core.attr(
        TagValues, default=None, computed=True, kind=core.Kind.array
    )

    target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        comparator: Optional[Union[str, core.StringOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = None,
        target: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScopingExcludesAndTagScopeTerm.Args(
                comparator=comparator,
                key=key,
                tag_values=tag_values,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = core.arg(
            default=None
        )

        target: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ScopingExcludesAnd(core.Schema):

    simple_scope_term: Optional[SimpleScopeTerm] = core.attr(
        SimpleScopeTerm, default=None, computed=True
    )

    tag_scope_term: Optional[ScopingExcludesAndTagScopeTerm] = core.attr(
        ScopingExcludesAndTagScopeTerm, default=None, computed=True
    )

    def __init__(
        self,
        *,
        simple_scope_term: Optional[SimpleScopeTerm] = None,
        tag_scope_term: Optional[ScopingExcludesAndTagScopeTerm] = None,
    ):
        super().__init__(
            args=ScopingExcludesAnd.Args(
                simple_scope_term=simple_scope_term,
                tag_scope_term=tag_scope_term,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        simple_scope_term: Optional[SimpleScopeTerm] = core.arg(default=None)

        tag_scope_term: Optional[ScopingExcludesAndTagScopeTerm] = core.arg(default=None)


@core.schema
class ScopingExcludes(core.Schema):

    and_: Optional[Union[List[ScopingExcludesAnd], core.ArrayOut[ScopingExcludesAnd]]] = core.attr(
        ScopingExcludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: Optional[Union[List[ScopingExcludesAnd], core.ArrayOut[ScopingExcludesAnd]]] = None,
    ):
        super().__init__(
            args=ScopingExcludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[
            Union[List[ScopingExcludesAnd], core.ArrayOut[ScopingExcludesAnd]]
        ] = core.arg(default=None)


@core.schema
class ScopingIncludesAndTagScopeTerm(core.Schema):

    comparator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = core.attr(
        TagValues, default=None, kind=core.Kind.array
    )

    target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        comparator: Optional[Union[str, core.StringOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
        tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = None,
        target: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScopingIncludesAndTagScopeTerm.Args(
                comparator=comparator,
                key=key,
                tag_values=tag_values,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_values: Optional[Union[List[TagValues], core.ArrayOut[TagValues]]] = core.arg(
            default=None
        )

        target: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ScopingIncludesAnd(core.Schema):

    simple_scope_term: Optional[SimpleScopeTerm] = core.attr(
        SimpleScopeTerm, default=None, computed=True
    )

    tag_scope_term: Optional[ScopingIncludesAndTagScopeTerm] = core.attr(
        ScopingIncludesAndTagScopeTerm, default=None, computed=True
    )

    def __init__(
        self,
        *,
        simple_scope_term: Optional[SimpleScopeTerm] = None,
        tag_scope_term: Optional[ScopingIncludesAndTagScopeTerm] = None,
    ):
        super().__init__(
            args=ScopingIncludesAnd.Args(
                simple_scope_term=simple_scope_term,
                tag_scope_term=tag_scope_term,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        simple_scope_term: Optional[SimpleScopeTerm] = core.arg(default=None)

        tag_scope_term: Optional[ScopingIncludesAndTagScopeTerm] = core.arg(default=None)


@core.schema
class ScopingIncludes(core.Schema):

    and_: Optional[Union[List[ScopingIncludesAnd], core.ArrayOut[ScopingIncludesAnd]]] = core.attr(
        ScopingIncludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: Optional[Union[List[ScopingIncludesAnd], core.ArrayOut[ScopingIncludesAnd]]] = None,
    ):
        super().__init__(
            args=ScopingIncludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[
            Union[List[ScopingIncludesAnd], core.ArrayOut[ScopingIncludesAnd]]
        ] = core.arg(default=None)


@core.schema
class Scoping(core.Schema):

    excludes: Optional[ScopingExcludes] = core.attr(ScopingExcludes, default=None, computed=True)

    includes: Optional[ScopingIncludes] = core.attr(ScopingIncludes, default=None, computed=True)

    def __init__(
        self,
        *,
        excludes: Optional[ScopingExcludes] = None,
        includes: Optional[ScopingIncludes] = None,
    ):
        super().__init__(
            args=Scoping.Args(
                excludes=excludes,
                includes=includes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        excludes: Optional[ScopingExcludes] = core.arg(default=None)

        includes: Optional[ScopingIncludes] = core.arg(default=None)


@core.schema
class BucketDefinitions(core.Schema):

    account_id: Union[str, core.StringOut] = core.attr(str)

    buckets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        account_id: Union[str, core.StringOut],
        buckets: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=BucketDefinitions.Args(
                account_id=account_id,
                buckets=buckets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Union[str, core.StringOut] = core.arg()

        buckets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class S3JobDefinition(core.Schema):

    bucket_criteria: Optional[BucketCriteria] = core.attr(
        BucketCriteria, default=None, computed=True
    )

    bucket_definitions: Optional[
        Union[List[BucketDefinitions], core.ArrayOut[BucketDefinitions]]
    ] = core.attr(BucketDefinitions, default=None, kind=core.Kind.array)

    scoping: Optional[Scoping] = core.attr(Scoping, default=None, computed=True)

    def __init__(
        self,
        *,
        bucket_criteria: Optional[BucketCriteria] = None,
        bucket_definitions: Optional[
            Union[List[BucketDefinitions], core.ArrayOut[BucketDefinitions]]
        ] = None,
        scoping: Optional[Scoping] = None,
    ):
        super().__init__(
            args=S3JobDefinition.Args(
                bucket_criteria=bucket_criteria,
                bucket_definitions=bucket_definitions,
                scoping=scoping,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_criteria: Optional[BucketCriteria] = core.arg(default=None)

        bucket_definitions: Optional[
            Union[List[BucketDefinitions], core.ArrayOut[BucketDefinitions]]
        ] = core.arg(default=None)

        scoping: Optional[Scoping] = core.arg(default=None)


@core.schema
class ScheduleFrequency(core.Schema):

    daily_schedule: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    monthly_schedule: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    weekly_schedule: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        daily_schedule: Optional[Union[bool, core.BoolOut]] = None,
        monthly_schedule: Optional[Union[int, core.IntOut]] = None,
        weekly_schedule: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScheduleFrequency.Args(
                daily_schedule=daily_schedule,
                monthly_schedule=monthly_schedule,
                weekly_schedule=weekly_schedule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        daily_schedule: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        monthly_schedule: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        weekly_schedule: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_macie2_classification_job", namespace="aws_macie2")
class ClassificationJob(core.Resource):

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    custom_data_identifier_ids: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, computed=True, kind=core.Kind.array)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    initial_run: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    job_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    job_type: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    s3_job_definition: S3JobDefinition = core.attr(S3JobDefinition)

    sampling_percentage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    schedule_frequency: Optional[ScheduleFrequency] = core.attr(
        ScheduleFrequency, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_paused_details: Union[
        List[UserPausedDetails], core.ArrayOut[UserPausedDetails]
    ] = core.attr(UserPausedDetails, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        job_type: Union[str, core.StringOut],
        s3_job_definition: S3JobDefinition,
        custom_data_identifier_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        initial_run: Optional[Union[bool, core.BoolOut]] = None,
        job_status: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        sampling_percentage: Optional[Union[int, core.IntOut]] = None,
        schedule_frequency: Optional[ScheduleFrequency] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClassificationJob.Args(
                job_type=job_type,
                s3_job_definition=s3_job_definition,
                custom_data_identifier_ids=custom_data_identifier_ids,
                description=description,
                initial_run=initial_run,
                job_status=job_status,
                name=name,
                name_prefix=name_prefix,
                sampling_percentage=sampling_percentage,
                schedule_frequency=schedule_frequency,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        custom_data_identifier_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        initial_run: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        job_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        job_type: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_job_definition: S3JobDefinition = core.arg()

        sampling_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        schedule_frequency: Optional[ScheduleFrequency] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
