from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_key_pair", namespace="aws_ec2")
class KeyPair(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key_name_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    key_pair_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        public_key: Union[str, core.StringOut],
        key_name: Optional[Union[str, core.StringOut]] = None,
        key_name_prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeyPair.Args(
                public_key=public_key,
                key_name=key_name,
                key_name_prefix=key_name_prefix,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key_name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        public_key: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
