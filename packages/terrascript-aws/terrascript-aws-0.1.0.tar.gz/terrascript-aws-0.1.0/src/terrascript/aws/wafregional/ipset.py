from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class IpSetDescriptor(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IpSetDescriptor.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_ipset", namespace="aws_wafregional")
class Ipset(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_set_descriptor: Optional[
        Union[List[IpSetDescriptor], core.ArrayOut[IpSetDescriptor]]
    ] = core.attr(IpSetDescriptor, default=None, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        ip_set_descriptor: Optional[
            Union[List[IpSetDescriptor], core.ArrayOut[IpSetDescriptor]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipset.Args(
                name=name,
                ip_set_descriptor=ip_set_descriptor,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ip_set_descriptor: Optional[
            Union[List[IpSetDescriptor], core.ArrayOut[IpSetDescriptor]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
