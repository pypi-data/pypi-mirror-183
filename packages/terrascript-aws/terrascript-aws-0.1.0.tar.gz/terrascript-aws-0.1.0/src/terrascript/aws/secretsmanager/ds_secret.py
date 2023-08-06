from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RotationRules(core.Schema):

    automatically_after_days: Union[int, core.IntOut] = core.attr(int, computed=True)

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


@core.data(type="aws_secretsmanager_secret", namespace="aws_secretsmanager")
class DsSecret(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    rotation_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    rotation_lambda_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    rotation_rules: Union[List[RotationRules], core.ArrayOut[RotationRules]] = core.attr(
        RotationRules, computed=True, kind=core.Kind.array
    )

    tags: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSecret.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
