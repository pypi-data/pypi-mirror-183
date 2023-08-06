from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_redshift_hsm_configuration", namespace="aws_redshift")
class HsmConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str)

    hsm_configuration_identifier: Union[str, core.StringOut] = core.attr(str)

    hsm_ip_address: Union[str, core.StringOut] = core.attr(str)

    hsm_partition_name: Union[str, core.StringOut] = core.attr(str)

    hsm_partition_password: Union[str, core.StringOut] = core.attr(str)

    hsm_server_public_certificate: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        description: Union[str, core.StringOut],
        hsm_configuration_identifier: Union[str, core.StringOut],
        hsm_ip_address: Union[str, core.StringOut],
        hsm_partition_name: Union[str, core.StringOut],
        hsm_partition_password: Union[str, core.StringOut],
        hsm_server_public_certificate: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=HsmConfiguration.Args(
                description=description,
                hsm_configuration_identifier=hsm_configuration_identifier,
                hsm_ip_address=hsm_ip_address,
                hsm_partition_name=hsm_partition_name,
                hsm_partition_password=hsm_partition_password,
                hsm_server_public_certificate=hsm_server_public_certificate,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Union[str, core.StringOut] = core.arg()

        hsm_configuration_identifier: Union[str, core.StringOut] = core.arg()

        hsm_ip_address: Union[str, core.StringOut] = core.arg()

        hsm_partition_name: Union[str, core.StringOut] = core.arg()

        hsm_partition_password: Union[str, core.StringOut] = core.arg()

        hsm_server_public_certificate: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
