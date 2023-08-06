from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_api_gateway_domain_name", namespace="aws_api_gateway")
class DsDomainName(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_upload_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudfront_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudfront_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    endpoint_configuration: Union[
        List[EndpointConfiguration], core.ArrayOut[EndpointConfiguration]
    ] = core.attr(EndpointConfiguration, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    regional_certificate_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    regional_certificate_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    regional_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    regional_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDomainName.Args(
                domain_name=domain_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
