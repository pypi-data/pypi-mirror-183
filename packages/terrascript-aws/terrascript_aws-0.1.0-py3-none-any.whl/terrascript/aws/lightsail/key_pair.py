from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lightsail_key_pair", namespace="aws_lightsail")
class KeyPair(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted_fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted_private_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pgp_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    private_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        pgp_key: Optional[Union[str, core.StringOut]] = None,
        public_key: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeyPair.Args(
                name=name,
                name_prefix=name_prefix,
                pgp_key=pgp_key,
                public_key=public_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pgp_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        public_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)
