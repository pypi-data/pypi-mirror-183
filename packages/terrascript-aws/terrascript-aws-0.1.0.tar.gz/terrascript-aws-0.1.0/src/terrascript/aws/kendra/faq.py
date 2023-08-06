from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Path(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=S3Path.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_kendra_faq", namespace="aws_kendra")
class Faq(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    faq_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_id: Union[str, core.StringOut] = core.attr(str)

    language_code: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    s3_path: S3Path = core.attr(S3Path)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        s3_path: S3Path,
        description: Optional[Union[str, core.StringOut]] = None,
        file_format: Optional[Union[str, core.StringOut]] = None,
        language_code: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Faq.Args(
                index_id=index_id,
                name=name,
                role_arn=role_arn,
                s3_path=s3_path,
                description=description,
                file_format=file_format,
                language_code=language_code,
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

        file_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_id: Union[str, core.StringOut] = core.arg()

        language_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        s3_path: S3Path = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
