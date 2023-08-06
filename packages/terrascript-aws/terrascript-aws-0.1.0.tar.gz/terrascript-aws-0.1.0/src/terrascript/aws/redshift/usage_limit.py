from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_redshift_usage_limit", namespace="aws_redshift")
class UsageLimit(core.Resource):

    amount: Union[int, core.IntOut] = core.attr(int)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    breach_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    feature_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    limit_type: Union[str, core.StringOut] = core.attr(str)

    period: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        amount: Union[int, core.IntOut],
        cluster_identifier: Union[str, core.StringOut],
        feature_type: Union[str, core.StringOut],
        limit_type: Union[str, core.StringOut],
        breach_action: Optional[Union[str, core.StringOut]] = None,
        period: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UsageLimit.Args(
                amount=amount,
                cluster_identifier=cluster_identifier,
                feature_type=feature_type,
                limit_type=limit_type,
                breach_action=breach_action,
                period=period,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        amount: Union[int, core.IntOut] = core.arg()

        breach_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        feature_type: Union[str, core.StringOut] = core.arg()

        limit_type: Union[str, core.StringOut] = core.arg()

        period: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
