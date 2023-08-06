from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_cloudcontrolapi_resource", namespace="aws_cloudcontrolapi")
class DsResource(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identifier: Union[str, core.StringOut] = core.attr(str)

    properties: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type_name: Union[str, core.StringOut] = core.attr(str)

    type_version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        identifier: Union[str, core.StringOut],
        type_name: Union[str, core.StringOut],
        role_arn: Optional[Union[str, core.StringOut]] = None,
        type_version_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResource.Args(
                identifier=identifier,
                type_name=type_name,
                role_arn=role_arn,
                type_version_id=type_version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifier: Union[str, core.StringOut] = core.arg()

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type_name: Union[str, core.StringOut] = core.arg()

        type_version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
