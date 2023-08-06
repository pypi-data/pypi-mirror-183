from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AppMonitorConfiguration(core.Schema):

    allow_cookies: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_xray: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    excluded_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    favorite_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    guest_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    identity_pool_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    included_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    session_sample_rate: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    telemetries: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        allow_cookies: Optional[Union[bool, core.BoolOut]] = None,
        enable_xray: Optional[Union[bool, core.BoolOut]] = None,
        excluded_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        favorite_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        guest_role_arn: Optional[Union[str, core.StringOut]] = None,
        identity_pool_id: Optional[Union[str, core.StringOut]] = None,
        included_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        session_sample_rate: Optional[Union[float, core.FloatOut]] = None,
        telemetries: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AppMonitorConfiguration.Args(
                allow_cookies=allow_cookies,
                enable_xray=enable_xray,
                excluded_pages=excluded_pages,
                favorite_pages=favorite_pages,
                guest_role_arn=guest_role_arn,
                identity_pool_id=identity_pool_id,
                included_pages=included_pages,
                session_sample_rate=session_sample_rate,
                telemetries=telemetries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_cookies: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_xray: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        excluded_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        favorite_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        guest_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_pool_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        included_pages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        session_sample_rate: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        telemetries: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.resource(type="aws_rum_app_monitor", namespace="aws_rum")
class AppMonitor(core.Resource):

    app_monitor_configuration: Optional[AppMonitorConfiguration] = core.attr(
        AppMonitorConfiguration, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cw_log_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cw_log_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

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
        domain: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        app_monitor_configuration: Optional[AppMonitorConfiguration] = None,
        cw_log_enabled: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppMonitor.Args(
                domain=domain,
                name=name,
                app_monitor_configuration=app_monitor_configuration,
                cw_log_enabled=cw_log_enabled,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_monitor_configuration: Optional[AppMonitorConfiguration] = core.arg(default=None)

        cw_log_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        domain: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
