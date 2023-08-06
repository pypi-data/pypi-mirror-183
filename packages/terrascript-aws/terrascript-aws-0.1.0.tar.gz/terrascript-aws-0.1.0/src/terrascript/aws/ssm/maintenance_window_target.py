from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Targets(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Targets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_ssm_maintenance_window_target", namespace="aws_ssm")
class MaintenanceWindowTarget(core.Resource):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_information: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_type: Union[str, core.StringOut] = core.attr(str)

    targets: Union[List[Targets], core.ArrayOut[Targets]] = core.attr(Targets, kind=core.Kind.array)

    window_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_type: Union[str, core.StringOut],
        targets: Union[List[Targets], core.ArrayOut[Targets]],
        window_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        owner_information: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MaintenanceWindowTarget.Args(
                resource_type=resource_type,
                targets=targets,
                window_id=window_id,
                description=description,
                name=name,
                owner_information=owner_information,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner_information: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_type: Union[str, core.StringOut] = core.arg()

        targets: Union[List[Targets], core.ArrayOut[Targets]] = core.arg()

        window_id: Union[str, core.StringOut] = core.arg()
