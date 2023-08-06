from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Notifications(core.Schema):

    completed: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    progressing: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    warning: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        completed: Optional[Union[str, core.StringOut]] = None,
        error: Optional[Union[str, core.StringOut]] = None,
        progressing: Optional[Union[str, core.StringOut]] = None,
        warning: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Notifications.Args(
                completed=completed,
                error=error,
                progressing=progressing,
                warning=warning,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        completed: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        error: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        progressing: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        warning: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ContentConfig(core.Schema):

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    storage_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Optional[Union[str, core.StringOut]] = None,
        storage_class: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ContentConfig.Args(
                bucket=bucket,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ThumbnailConfig(core.Schema):

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    storage_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Optional[Union[str, core.StringOut]] = None,
        storage_class: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ThumbnailConfig.Args(
                bucket=bucket,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ThumbnailConfigPermissions(core.Schema):

    access: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    grantee: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    grantee_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        grantee: Optional[Union[str, core.StringOut]] = None,
        grantee_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ThumbnailConfigPermissions.Args(
                access=access,
                grantee=grantee,
                grantee_type=grantee_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        grantee: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        grantee_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ContentConfigPermissions(core.Schema):

    access: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    grantee: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    grantee_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        grantee: Optional[Union[str, core.StringOut]] = None,
        grantee_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ContentConfigPermissions.Args(
                access=access,
                grantee=grantee,
                grantee_type=grantee_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        grantee: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        grantee_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_elastictranscoder_pipeline", namespace="aws_elastictranscoder")
class Pipeline(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_config: Optional[ContentConfig] = core.attr(ContentConfig, default=None, computed=True)

    content_config_permissions: Optional[
        Union[List[ContentConfigPermissions], core.ArrayOut[ContentConfigPermissions]]
    ] = core.attr(ContentConfigPermissions, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_bucket: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    notifications: Optional[Notifications] = core.attr(Notifications, default=None)

    output_bucket: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    role: Union[str, core.StringOut] = core.attr(str)

    thumbnail_config: Optional[ThumbnailConfig] = core.attr(
        ThumbnailConfig, default=None, computed=True
    )

    thumbnail_config_permissions: Optional[
        Union[List[ThumbnailConfigPermissions], core.ArrayOut[ThumbnailConfigPermissions]]
    ] = core.attr(ThumbnailConfigPermissions, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        input_bucket: Union[str, core.StringOut],
        role: Union[str, core.StringOut],
        aws_kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        content_config: Optional[ContentConfig] = None,
        content_config_permissions: Optional[
            Union[List[ContentConfigPermissions], core.ArrayOut[ContentConfigPermissions]]
        ] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        notifications: Optional[Notifications] = None,
        output_bucket: Optional[Union[str, core.StringOut]] = None,
        thumbnail_config: Optional[ThumbnailConfig] = None,
        thumbnail_config_permissions: Optional[
            Union[List[ThumbnailConfigPermissions], core.ArrayOut[ThumbnailConfigPermissions]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Pipeline.Args(
                input_bucket=input_bucket,
                role=role,
                aws_kms_key_arn=aws_kms_key_arn,
                content_config=content_config,
                content_config_permissions=content_config_permissions,
                name=name,
                notifications=notifications,
                output_bucket=output_bucket,
                thumbnail_config=thumbnail_config,
                thumbnail_config_permissions=thumbnail_config_permissions,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_config: Optional[ContentConfig] = core.arg(default=None)

        content_config_permissions: Optional[
            Union[List[ContentConfigPermissions], core.ArrayOut[ContentConfigPermissions]]
        ] = core.arg(default=None)

        input_bucket: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notifications: Optional[Notifications] = core.arg(default=None)

        output_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role: Union[str, core.StringOut] = core.arg()

        thumbnail_config: Optional[ThumbnailConfig] = core.arg(default=None)

        thumbnail_config_permissions: Optional[
            Union[List[ThumbnailConfigPermissions], core.ArrayOut[ThumbnailConfigPermissions]]
        ] = core.arg(default=None)
