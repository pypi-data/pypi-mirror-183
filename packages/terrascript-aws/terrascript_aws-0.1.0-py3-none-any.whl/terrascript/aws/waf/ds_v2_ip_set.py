from typing import List, Union

import terrascript.core as core


@core.data(type="aws_wafv2_ip_set", namespace="aws_waf")
class DsV2IpSet(core.Data):

    addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    scope: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsV2IpSet.Args(
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()
