from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_volume_attachment", namespace="aws_ebs")
class VolumeAttachment(core.Resource):

    device_name: Union[str, core.StringOut] = core.attr(str)

    force_detach: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    skip_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    stop_instance_before_detaching: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    volume_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        device_name: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
        volume_id: Union[str, core.StringOut],
        force_detach: Optional[Union[bool, core.BoolOut]] = None,
        skip_destroy: Optional[Union[bool, core.BoolOut]] = None,
        stop_instance_before_detaching: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VolumeAttachment.Args(
                device_name=device_name,
                instance_id=instance_id,
                volume_id=volume_id,
                force_detach=force_detach,
                skip_destroy=skip_destroy,
                stop_instance_before_detaching=stop_instance_before_detaching,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_name: Union[str, core.StringOut] = core.arg()

        force_detach: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        skip_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        stop_instance_before_detaching: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        volume_id: Union[str, core.StringOut] = core.arg()
