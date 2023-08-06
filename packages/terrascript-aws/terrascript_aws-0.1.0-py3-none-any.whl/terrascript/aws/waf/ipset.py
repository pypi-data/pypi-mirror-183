from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class IpSetDescriptors(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IpSetDescriptors.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_waf_ipset", namespace="aws_waf")
class Ipset(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_set_descriptors: Optional[
        Union[List[IpSetDescriptors], core.ArrayOut[IpSetDescriptors]]
    ] = core.attr(IpSetDescriptors, default=None, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        ip_set_descriptors: Optional[
            Union[List[IpSetDescriptors], core.ArrayOut[IpSetDescriptors]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipset.Args(
                name=name,
                ip_set_descriptors=ip_set_descriptors,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ip_set_descriptors: Optional[
            Union[List[IpSetDescriptors], core.ArrayOut[IpSetDescriptors]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
