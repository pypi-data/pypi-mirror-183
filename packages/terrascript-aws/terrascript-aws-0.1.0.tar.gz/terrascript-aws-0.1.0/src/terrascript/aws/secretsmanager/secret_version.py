from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_secretsmanager_secret_version", namespace="aws_secretsmanager")
class SecretVersion(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    secret_binary: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secret_id: Union[str, core.StringOut] = core.attr(str)

    secret_string: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    version_stages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        secret_id: Union[str, core.StringOut],
        secret_binary: Optional[Union[str, core.StringOut]] = None,
        secret_string: Optional[Union[str, core.StringOut]] = None,
        version_stages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretVersion.Args(
                secret_id=secret_id,
                secret_binary=secret_binary,
                secret_string=secret_string,
                version_stages=version_stages,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        secret_binary: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        secret_id: Union[str, core.StringOut] = core.arg()

        secret_string: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version_stages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
