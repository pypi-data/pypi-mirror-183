from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Replica(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    last_accessed_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        last_accessed_date: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        status_message: Union[str, core.StringOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Replica.Args(
                last_accessed_date=last_accessed_date,
                region=region,
                status=status,
                status_message=status_message,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        last_accessed_date: Union[str, core.StringOut] = core.arg()

        region: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        status_message: Union[str, core.StringOut] = core.arg()


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


@core.resource(type="aws_secretsmanager_secret", namespace="aws_secretsmanager")
class Secret(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_overwrite_replica_secret: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    recovery_window_in_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    replica: Optional[Union[List[Replica], core.ArrayOut[Replica]]] = core.attr(
        Replica, default=None, computed=True, kind=core.Kind.array
    )

    rotation_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    rotation_lambda_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    rotation_rules: Optional[RotationRules] = core.attr(RotationRules, default=None, computed=True)

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
        description: Optional[Union[str, core.StringOut]] = None,
        force_overwrite_replica_secret: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        recovery_window_in_days: Optional[Union[int, core.IntOut]] = None,
        replica: Optional[Union[List[Replica], core.ArrayOut[Replica]]] = None,
        rotation_lambda_arn: Optional[Union[str, core.StringOut]] = None,
        rotation_rules: Optional[RotationRules] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Secret.Args(
                description=description,
                force_overwrite_replica_secret=force_overwrite_replica_secret,
                kms_key_id=kms_key_id,
                name=name,
                name_prefix=name_prefix,
                policy=policy,
                recovery_window_in_days=recovery_window_in_days,
                replica=replica,
                rotation_lambda_arn=rotation_lambda_arn,
                rotation_rules=rotation_rules,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_overwrite_replica_secret: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        recovery_window_in_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        replica: Optional[Union[List[Replica], core.ArrayOut[Replica]]] = core.arg(default=None)

        rotation_lambda_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rotation_rules: Optional[RotationRules] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
