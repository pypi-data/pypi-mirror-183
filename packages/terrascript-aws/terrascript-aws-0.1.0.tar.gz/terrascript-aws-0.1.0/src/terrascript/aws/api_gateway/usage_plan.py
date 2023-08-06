from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class QuotaSettings(core.Schema):

    limit: Union[int, core.IntOut] = core.attr(int)

    offset: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    period: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        limit: Union[int, core.IntOut],
        period: Union[str, core.StringOut],
        offset: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=QuotaSettings.Args(
                limit=limit,
                period=period,
                offset=offset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        limit: Union[int, core.IntOut] = core.arg()

        offset: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        period: Union[str, core.StringOut] = core.arg()


@core.schema
class ThrottleSettings(core.Schema):

    burst_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    rate_limit: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        burst_limit: Optional[Union[int, core.IntOut]] = None,
        rate_limit: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=ThrottleSettings.Args(
                burst_limit=burst_limit,
                rate_limit=rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        burst_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        rate_limit: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class Throttle(core.Schema):

    burst_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    path: Union[str, core.StringOut] = core.attr(str)

    rate_limit: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        path: Union[str, core.StringOut],
        burst_limit: Optional[Union[int, core.IntOut]] = None,
        rate_limit: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=Throttle.Args(
                path=path,
                burst_limit=burst_limit,
                rate_limit=rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        burst_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        path: Union[str, core.StringOut] = core.arg()

        rate_limit: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class ApiStages(core.Schema):

    api_id: Union[str, core.StringOut] = core.attr(str)

    stage: Union[str, core.StringOut] = core.attr(str)

    throttle: Optional[Union[List[Throttle], core.ArrayOut[Throttle]]] = core.attr(
        Throttle, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        api_id: Union[str, core.StringOut],
        stage: Union[str, core.StringOut],
        throttle: Optional[Union[List[Throttle], core.ArrayOut[Throttle]]] = None,
    ):
        super().__init__(
            args=ApiStages.Args(
                api_id=api_id,
                stage=stage,
                throttle=throttle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_id: Union[str, core.StringOut] = core.arg()

        stage: Union[str, core.StringOut] = core.arg()

        throttle: Optional[Union[List[Throttle], core.ArrayOut[Throttle]]] = core.arg(default=None)


@core.resource(type="aws_api_gateway_usage_plan", namespace="aws_api_gateway")
class UsagePlan(core.Resource):

    api_stages: Optional[Union[List[ApiStages], core.ArrayOut[ApiStages]]] = core.attr(
        ApiStages, default=None, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    product_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    quota_settings: Optional[QuotaSettings] = core.attr(QuotaSettings, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throttle_settings: Optional[ThrottleSettings] = core.attr(ThrottleSettings, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        api_stages: Optional[Union[List[ApiStages], core.ArrayOut[ApiStages]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        product_code: Optional[Union[str, core.StringOut]] = None,
        quota_settings: Optional[QuotaSettings] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        throttle_settings: Optional[ThrottleSettings] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UsagePlan.Args(
                name=name,
                api_stages=api_stages,
                description=description,
                product_code=product_code,
                quota_settings=quota_settings,
                tags=tags,
                tags_all=tags_all,
                throttle_settings=throttle_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_stages: Optional[Union[List[ApiStages], core.ArrayOut[ApiStages]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        product_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        quota_settings: Optional[QuotaSettings] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        throttle_settings: Optional[ThrottleSettings] = core.arg(default=None)
