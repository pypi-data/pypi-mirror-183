from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Subscriber(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Subscriber.Args(
                address=address,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ce_anomaly_subscription", namespace="aws_ce")
class AnomalySubscription(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    frequency: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    monitor_arn_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    subscriber: Union[List[Subscriber], core.ArrayOut[Subscriber]] = core.attr(
        Subscriber, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    threshold: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        resource_name: str,
        *,
        frequency: Union[str, core.StringOut],
        monitor_arn_list: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        subscriber: Union[List[Subscriber], core.ArrayOut[Subscriber]],
        threshold: Union[float, core.FloatOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AnomalySubscription.Args(
                frequency=frequency,
                monitor_arn_list=monitor_arn_list,
                name=name,
                subscriber=subscriber,
                threshold=threshold,
                account_id=account_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        frequency: Union[str, core.StringOut] = core.arg()

        monitor_arn_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        subscriber: Union[List[Subscriber], core.ArrayOut[Subscriber]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        threshold: Union[float, core.FloatOut] = core.arg()
