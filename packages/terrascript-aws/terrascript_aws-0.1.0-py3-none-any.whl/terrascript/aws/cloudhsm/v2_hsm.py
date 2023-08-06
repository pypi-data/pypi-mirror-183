from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudhsm_v2_hsm", namespace="aws_cloudhsm")
class V2Hsm(core.Resource):

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    hsm_eni_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    hsm_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    hsm_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        ip_address: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2Hsm.Args(
                cluster_id=cluster_id,
                availability_zone=availability_zone,
                ip_address=ip_address,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_id: Union[str, core.StringOut] = core.arg()

        ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
