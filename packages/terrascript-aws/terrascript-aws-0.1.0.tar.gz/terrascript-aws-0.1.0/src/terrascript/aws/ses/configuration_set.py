from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class TrackingOptions(core.Schema):

    custom_redirect_domain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        custom_redirect_domain: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TrackingOptions.Args(
                custom_redirect_domain=custom_redirect_domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_redirect_domain: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DeliveryOptions(core.Schema):

    tls_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        tls_policy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DeliveryOptions.Args(
                tls_policy=tls_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tls_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ses_configuration_set", namespace="aws_ses")
class ConfigurationSet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delivery_options: Optional[DeliveryOptions] = core.attr(DeliveryOptions, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_fresh_start: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    reputation_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    sending_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tracking_options: Optional[TrackingOptions] = core.attr(TrackingOptions, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        delivery_options: Optional[DeliveryOptions] = None,
        reputation_metrics_enabled: Optional[Union[bool, core.BoolOut]] = None,
        sending_enabled: Optional[Union[bool, core.BoolOut]] = None,
        tracking_options: Optional[TrackingOptions] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationSet.Args(
                name=name,
                delivery_options=delivery_options,
                reputation_metrics_enabled=reputation_metrics_enabled,
                sending_enabled=sending_enabled,
                tracking_options=tracking_options,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delivery_options: Optional[DeliveryOptions] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        reputation_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sending_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tracking_options: Optional[TrackingOptions] = core.arg(default=None)
