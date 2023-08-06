from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Destination(core.Schema):

    availability_zone_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    file_system_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        file_system_id: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        availability_zone_name: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Destination.Args(
                file_system_id=file_system_id,
                status=status,
                availability_zone_name=availability_zone_name,
                kms_key_id=kms_key_id,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_system_id: Union[str, core.StringOut] = core.arg()

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_efs_replication_configuration", namespace="aws_efs")
class ReplicationConfiguration(core.Resource):

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination: Destination = core.attr(Destination)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    original_source_file_system_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_file_system_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_file_system_id: Union[str, core.StringOut] = core.attr(str)

    source_file_system_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination: Destination,
        source_file_system_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationConfiguration.Args(
                destination=destination,
                source_file_system_id=source_file_system_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: Destination = core.arg()

        source_file_system_id: Union[str, core.StringOut] = core.arg()
