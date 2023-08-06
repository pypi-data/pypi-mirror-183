from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class InputParameter(core.Schema):

    parameter_name: Union[str, core.StringOut] = core.attr(str)

    parameter_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        parameter_name: Union[str, core.StringOut],
        parameter_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InputParameter.Args(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_name: Union[str, core.StringOut] = core.arg()

        parameter_value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_config_organization_conformance_pack", namespace="aws_config")
class OrganizationConformancePack(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delivery_s3_bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    delivery_s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    excluded_accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_parameter: Optional[
        Union[List[InputParameter], core.ArrayOut[InputParameter]]
    ] = core.attr(InputParameter, default=None, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    template_body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    template_s3_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        delivery_s3_bucket: Optional[Union[str, core.StringOut]] = None,
        delivery_s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
        excluded_accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        input_parameter: Optional[
            Union[List[InputParameter], core.ArrayOut[InputParameter]]
        ] = None,
        template_body: Optional[Union[str, core.StringOut]] = None,
        template_s3_uri: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationConformancePack.Args(
                name=name,
                delivery_s3_bucket=delivery_s3_bucket,
                delivery_s3_key_prefix=delivery_s3_key_prefix,
                excluded_accounts=excluded_accounts,
                input_parameter=input_parameter,
                template_body=template_body,
                template_s3_uri=template_s3_uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delivery_s3_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delivery_s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        excluded_accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        input_parameter: Optional[
            Union[List[InputParameter], core.ArrayOut[InputParameter]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        template_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        template_s3_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)
