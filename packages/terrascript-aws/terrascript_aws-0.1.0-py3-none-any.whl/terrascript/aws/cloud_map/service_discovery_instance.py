from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_service_discovery_instance", namespace="aws_cloud_map")
class ServiceDiscoveryInstance(core.Resource):

    attributes: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    service_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        attributes: Union[Dict[str, str], core.MapOut[core.StringOut]],
        instance_id: Union[str, core.StringOut],
        service_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceDiscoveryInstance.Args(
                attributes=attributes,
                instance_id=instance_id,
                service_id=service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        service_id: Union[str, core.StringOut] = core.arg()
