from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_xray_sampling_rule", namespace="aws_x_ray")
class XraySamplingRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    fixed_rate: Union[float, core.FloatOut] = core.attr(float)

    host: Union[str, core.StringOut] = core.attr(str)

    http_method: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    priority: Union[int, core.IntOut] = core.attr(int)

    reservoir_size: Union[int, core.IntOut] = core.attr(int)

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    rule_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_name: Union[str, core.StringOut] = core.attr(str)

    service_type: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url_path: Union[str, core.StringOut] = core.attr(str)

    version: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        fixed_rate: Union[float, core.FloatOut],
        host: Union[str, core.StringOut],
        http_method: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
        reservoir_size: Union[int, core.IntOut],
        resource_arn: Union[str, core.StringOut],
        service_name: Union[str, core.StringOut],
        service_type: Union[str, core.StringOut],
        url_path: Union[str, core.StringOut],
        version: Union[int, core.IntOut],
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        rule_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=XraySamplingRule.Args(
                fixed_rate=fixed_rate,
                host=host,
                http_method=http_method,
                priority=priority,
                reservoir_size=reservoir_size,
                resource_arn=resource_arn,
                service_name=service_name,
                service_type=service_type,
                url_path=url_path,
                version=version,
                attributes=attributes,
                rule_name=rule_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        fixed_rate: Union[float, core.FloatOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        http_method: Union[str, core.StringOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()

        reservoir_size: Union[int, core.IntOut] = core.arg()

        resource_arn: Union[str, core.StringOut] = core.arg()

        rule_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_name: Union[str, core.StringOut] = core.arg()

        service_type: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        url_path: Union[str, core.StringOut] = core.arg()

        version: Union[int, core.IntOut] = core.arg()
