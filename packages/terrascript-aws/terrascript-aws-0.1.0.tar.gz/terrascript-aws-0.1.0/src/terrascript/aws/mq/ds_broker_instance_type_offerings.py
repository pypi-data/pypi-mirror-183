from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class AvailabilityZones(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AvailabilityZones.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class BrokerInstanceOptions(core.Schema):

    availability_zones: Union[
        List[AvailabilityZones], core.ArrayOut[AvailabilityZones]
    ] = core.attr(AvailabilityZones, computed=True, kind=core.Kind.array)

    engine_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    host_instance_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    supported_deployment_modes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_engine_versions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        availability_zones: Union[List[AvailabilityZones], core.ArrayOut[AvailabilityZones]],
        engine_type: Union[str, core.StringOut],
        host_instance_type: Union[str, core.StringOut],
        storage_type: Union[str, core.StringOut],
        supported_deployment_modes: Union[List[str], core.ArrayOut[core.StringOut]],
        supported_engine_versions: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=BrokerInstanceOptions.Args(
                availability_zones=availability_zones,
                engine_type=engine_type,
                host_instance_type=host_instance_type,
                storage_type=storage_type,
                supported_deployment_modes=supported_deployment_modes,
                supported_engine_versions=supported_engine_versions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: Union[
            List[AvailabilityZones], core.ArrayOut[AvailabilityZones]
        ] = core.arg()

        engine_type: Union[str, core.StringOut] = core.arg()

        host_instance_type: Union[str, core.StringOut] = core.arg()

        storage_type: Union[str, core.StringOut] = core.arg()

        supported_deployment_modes: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        supported_engine_versions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_mq_broker_instance_type_offerings", namespace="aws_mq")
class DsBrokerInstanceTypeOfferings(core.Data):
    """
    Option for host instance type. See Broker Instance Options below.
    """

    broker_instance_options: Union[
        List[BrokerInstanceOptions], core.ArrayOut[BrokerInstanceOptions]
    ] = core.attr(BrokerInstanceOptions, computed=True, kind=core.Kind.array)

    """
    (Optional) Filter response by engine type.
    """
    engine_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) Filter response by host instance type.
    """
    host_instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Filter response by storage type.
    """
    storage_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        engine_type: Optional[Union[str, core.StringOut]] = None,
        host_instance_type: Optional[Union[str, core.StringOut]] = None,
        storage_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBrokerInstanceTypeOfferings.Args(
                engine_type=engine_type,
                host_instance_type=host_instance_type,
                storage_type=storage_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        engine_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        host_instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
