from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AutoExportPolicy(core.Schema):

    events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AutoExportPolicy.Args(
                events=events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class AutoImportPolicy(core.Schema):

    events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AutoImportPolicy.Args(
                events=events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class S3(core.Schema):

    auto_export_policy: Optional[AutoExportPolicy] = core.attr(
        AutoExportPolicy, default=None, computed=True
    )

    auto_import_policy: Optional[AutoImportPolicy] = core.attr(
        AutoImportPolicy, default=None, computed=True
    )

    def __init__(
        self,
        *,
        auto_export_policy: Optional[AutoExportPolicy] = None,
        auto_import_policy: Optional[AutoImportPolicy] = None,
    ):
        super().__init__(
            args=S3.Args(
                auto_export_policy=auto_export_policy,
                auto_import_policy=auto_import_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_export_policy: Optional[AutoExportPolicy] = core.arg(default=None)

        auto_import_policy: Optional[AutoImportPolicy] = core.arg(default=None)


@core.resource(type="aws_fsx_data_repository_association", namespace="aws_fsx")
class DataRepositoryAssociation(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    batch_import_meta_data_on_create: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    data_repository_path: Union[str, core.StringOut] = core.attr(str)

    delete_data_in_filesystem: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    file_system_path: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    imported_file_chunk_size: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    s3: Optional[S3] = core.attr(S3, default=None, computed=True)

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
        data_repository_path: Union[str, core.StringOut],
        file_system_id: Union[str, core.StringOut],
        file_system_path: Union[str, core.StringOut],
        batch_import_meta_data_on_create: Optional[Union[bool, core.BoolOut]] = None,
        delete_data_in_filesystem: Optional[Union[bool, core.BoolOut]] = None,
        imported_file_chunk_size: Optional[Union[int, core.IntOut]] = None,
        s3: Optional[S3] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataRepositoryAssociation.Args(
                data_repository_path=data_repository_path,
                file_system_id=file_system_id,
                file_system_path=file_system_path,
                batch_import_meta_data_on_create=batch_import_meta_data_on_create,
                delete_data_in_filesystem=delete_data_in_filesystem,
                imported_file_chunk_size=imported_file_chunk_size,
                s3=s3,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        batch_import_meta_data_on_create: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        data_repository_path: Union[str, core.StringOut] = core.arg()

        delete_data_in_filesystem: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        file_system_id: Union[str, core.StringOut] = core.arg()

        file_system_path: Union[str, core.StringOut] = core.arg()

        imported_file_chunk_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        s3: Optional[S3] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
