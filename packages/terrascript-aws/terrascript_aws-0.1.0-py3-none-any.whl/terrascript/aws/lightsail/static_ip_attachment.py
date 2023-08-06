from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lightsail_static_ip_attachment", namespace="aws_lightsail")
class StaticIpAttachment(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_name: Union[str, core.StringOut] = core.attr(str)

    ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    static_ip_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_name: Union[str, core.StringOut],
        static_ip_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StaticIpAttachment.Args(
                instance_name=instance_name,
                static_ip_name=static_ip_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_name: Union[str, core.StringOut] = core.arg()

        static_ip_name: Union[str, core.StringOut] = core.arg()
