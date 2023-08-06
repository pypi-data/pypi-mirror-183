from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_service", namespace="aws_meta_data_sources")
class DsService(core.Data):

    dns_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    partition: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    reverse_dns_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    reverse_dns_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    service_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        dns_name: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        reverse_dns_name: Optional[Union[str, core.StringOut]] = None,
        reverse_dns_prefix: Optional[Union[str, core.StringOut]] = None,
        service_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsService.Args(
                dns_name=dns_name,
                region=region,
                reverse_dns_name=reverse_dns_name,
                reverse_dns_prefix=reverse_dns_prefix,
                service_id=service_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        reverse_dns_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        reverse_dns_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
