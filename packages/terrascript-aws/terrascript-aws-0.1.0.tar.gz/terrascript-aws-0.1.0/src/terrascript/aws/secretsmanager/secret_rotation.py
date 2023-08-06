from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RotationRules(core.Schema):

    automatically_after_days: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        automatically_after_days: Union[int, core.IntOut],
    ):
        super().__init__(
            args=RotationRules.Args(
                automatically_after_days=automatically_after_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        automatically_after_days: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_secretsmanager_secret_rotation", namespace="aws_secretsmanager")
class SecretRotation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rotation_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    rotation_lambda_arn: Union[str, core.StringOut] = core.attr(str)

    rotation_rules: RotationRules = core.attr(RotationRules)

    secret_id: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        rotation_lambda_arn: Union[str, core.StringOut],
        rotation_rules: RotationRules,
        secret_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretRotation.Args(
                rotation_lambda_arn=rotation_lambda_arn,
                rotation_rules=rotation_rules,
                secret_id=secret_id,
                tags=tags,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        rotation_lambda_arn: Union[str, core.StringOut] = core.arg()

        rotation_rules: RotationRules = core.arg()

        secret_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
