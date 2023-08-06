from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class S3(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    file_key: Union[str, core.StringOut] = core.attr(str)

    object_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        file_key: Union[str, core.StringOut],
        object_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
                object_version=object_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        file_key: Union[str, core.StringOut] = core.arg()

        object_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Location(core.Schema):

    s3: S3 = core.attr(S3)

    def __init__(
        self,
        *,
        s3: S3,
    ):
        super().__init__(
            args=Location.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: S3 = core.arg()


@core.resource(
    type="aws_mskconnect_custom_plugin", namespace="aws_managed_streaming_for_kafka_connect"
)
class MskconnectCustomPlugin(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_type: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    location: Location = core.attr(Location)

    name: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        content_type: Union[str, core.StringOut],
        location: Location,
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskconnectCustomPlugin.Args(
                content_type=content_type,
                location=location,
                name=name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location: Location = core.arg()

        name: Union[str, core.StringOut] = core.arg()
