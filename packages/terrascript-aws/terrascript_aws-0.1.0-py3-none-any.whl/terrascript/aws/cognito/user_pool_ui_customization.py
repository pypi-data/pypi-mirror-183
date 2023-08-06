from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cognito_user_pool_ui_customization", namespace="aws_cognito")
class UserPoolUiCustomization(core.Resource):

    client_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    css: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    css_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_file: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    image_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_pool_id: Union[str, core.StringOut],
        client_id: Optional[Union[str, core.StringOut]] = None,
        css: Optional[Union[str, core.StringOut]] = None,
        image_file: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPoolUiCustomization.Args(
                user_pool_id=user_pool_id,
                client_id=client_id,
                css=css,
                image_file=image_file,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        css: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_file: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_pool_id: Union[str, core.StringOut] = core.arg()
