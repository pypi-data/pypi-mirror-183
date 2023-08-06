from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_guardduty_publishing_destination", namespace="aws_guardduty")
class PublishingDestination(core.Resource):

    destination_arn: Union[str, core.StringOut] = core.attr(str)

    destination_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    detector_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_arn: Union[str, core.StringOut],
        detector_id: Union[str, core.StringOut],
        kms_key_arn: Union[str, core.StringOut],
        destination_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PublishingDestination.Args(
                destination_arn=destination_arn,
                detector_id=detector_id,
                kms_key_arn=kms_key_arn,
                destination_type=destination_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_arn: Union[str, core.StringOut] = core.arg()

        destination_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        detector_id: Union[str, core.StringOut] = core.arg()

        kms_key_arn: Union[str, core.StringOut] = core.arg()
