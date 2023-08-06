from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_service_specific_credential", namespace="aws_iam")
class ServiceSpecificCredential(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_name: Union[str, core.StringOut] = core.attr(str)

    service_password: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_specific_credential_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_user_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        service_name: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceSpecificCredential.Args(
                service_name=service_name,
                user_name=user_name,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        service_name: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_name: Union[str, core.StringOut] = core.arg()
