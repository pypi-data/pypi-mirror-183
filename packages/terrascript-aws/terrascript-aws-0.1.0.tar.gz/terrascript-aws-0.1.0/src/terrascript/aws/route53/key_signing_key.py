from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_key_signing_key", namespace="aws_route53")
class KeySigningKey(core.Resource):

    digest_algorithm_mnemonic: Union[str, core.StringOut] = core.attr(str, computed=True)

    digest_algorithm_type: Union[int, core.IntOut] = core.attr(int, computed=True)

    digest_value: Union[str, core.StringOut] = core.attr(str, computed=True)

    dnskey_record: Union[str, core.StringOut] = core.attr(str, computed=True)

    ds_record: Union[str, core.StringOut] = core.attr(str, computed=True)

    flag: Union[int, core.IntOut] = core.attr(int, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_management_service_arn: Union[str, core.StringOut] = core.attr(str)

    key_tag: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    public_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_algorithm_mnemonic: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_algorithm_type: Union[int, core.IntOut] = core.attr(int, computed=True)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        hosted_zone_id: Union[str, core.StringOut],
        key_management_service_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeySigningKey.Args(
                hosted_zone_id=hosted_zone_id,
                key_management_service_arn=key_management_service_arn,
                name=name,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hosted_zone_id: Union[str, core.StringOut] = core.arg()

        key_management_service_arn: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)
