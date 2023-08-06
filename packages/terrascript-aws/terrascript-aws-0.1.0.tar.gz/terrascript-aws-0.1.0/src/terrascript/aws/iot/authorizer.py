from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_authorizer", namespace="aws_iot")
class Authorizer(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authorizer_function_arn: Union[str, core.StringOut] = core.attr(str)

    enable_caching_for_http: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    signing_disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    token_key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    token_signing_public_keys: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    def __init__(
        self,
        resource_name: str,
        *,
        authorizer_function_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        enable_caching_for_http: Optional[Union[bool, core.BoolOut]] = None,
        signing_disabled: Optional[Union[bool, core.BoolOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        token_key_name: Optional[Union[str, core.StringOut]] = None,
        token_signing_public_keys: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Authorizer.Args(
                authorizer_function_arn=authorizer_function_arn,
                name=name,
                enable_caching_for_http=enable_caching_for_http,
                signing_disabled=signing_disabled,
                status=status,
                token_key_name=token_key_name,
                token_signing_public_keys=token_signing_public_keys,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authorizer_function_arn: Union[str, core.StringOut] = core.arg()

        enable_caching_for_http: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        signing_disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        token_key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        token_signing_public_keys: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)
