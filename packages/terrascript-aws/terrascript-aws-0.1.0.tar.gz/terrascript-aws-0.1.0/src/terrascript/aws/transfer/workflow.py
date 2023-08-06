from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DeleteStepDetails(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_file_location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        source_file_location: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DeleteStepDetails.Args(
                name=name,
                source_file_location=source_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_file_location: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Tags(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Tags.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class TagStepDetails(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_file_location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[List[Tags], core.ArrayOut[Tags]]] = core.attr(
        Tags, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        source_file_location: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[List[Tags], core.ArrayOut[Tags]]] = None,
    ):
        super().__init__(
            args=TagStepDetails.Args(
                name=name,
                source_file_location=source_file_location,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_file_location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[List[Tags], core.ArrayOut[Tags]]] = core.arg(default=None)


@core.schema
class EfsFileLocation(core.Schema):

    file_system_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        file_system_id: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EfsFileLocation.Args(
                file_system_id=file_system_id,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_system_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3FileLocation(core.Schema):

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Optional[Union[str, core.StringOut]] = None,
        key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3FileLocation.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DestinationFileLocation(core.Schema):

    efs_file_location: Optional[EfsFileLocation] = core.attr(EfsFileLocation, default=None)

    s3_file_location: Optional[S3FileLocation] = core.attr(S3FileLocation, default=None)

    def __init__(
        self,
        *,
        efs_file_location: Optional[EfsFileLocation] = None,
        s3_file_location: Optional[S3FileLocation] = None,
    ):
        super().__init__(
            args=DestinationFileLocation.Args(
                efs_file_location=efs_file_location,
                s3_file_location=s3_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        efs_file_location: Optional[EfsFileLocation] = core.arg(default=None)

        s3_file_location: Optional[S3FileLocation] = core.arg(default=None)


@core.schema
class CopyStepDetails(core.Schema):

    destination_file_location: Optional[DestinationFileLocation] = core.attr(
        DestinationFileLocation, default=None
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    overwrite_existing: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_file_location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        destination_file_location: Optional[DestinationFileLocation] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        overwrite_existing: Optional[Union[str, core.StringOut]] = None,
        source_file_location: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CopyStepDetails.Args(
                destination_file_location=destination_file_location,
                name=name,
                overwrite_existing=overwrite_existing,
                source_file_location=source_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_file_location: Optional[DestinationFileLocation] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        overwrite_existing: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_file_location: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CustomStepDetails(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_file_location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        source_file_location: Optional[Union[str, core.StringOut]] = None,
        target: Optional[Union[str, core.StringOut]] = None,
        timeout_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CustomStepDetails.Args(
                name=name,
                source_file_location=source_file_location,
                target=target,
                timeout_seconds=timeout_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_file_location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class OnExceptionSteps(core.Schema):

    copy_step_details: Optional[CopyStepDetails] = core.attr(CopyStepDetails, default=None)

    custom_step_details: Optional[CustomStepDetails] = core.attr(CustomStepDetails, default=None)

    delete_step_details: Optional[DeleteStepDetails] = core.attr(DeleteStepDetails, default=None)

    tag_step_details: Optional[TagStepDetails] = core.attr(TagStepDetails, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        copy_step_details: Optional[CopyStepDetails] = None,
        custom_step_details: Optional[CustomStepDetails] = None,
        delete_step_details: Optional[DeleteStepDetails] = None,
        tag_step_details: Optional[TagStepDetails] = None,
    ):
        super().__init__(
            args=OnExceptionSteps.Args(
                type=type,
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_step_details: Optional[CopyStepDetails] = core.arg(default=None)

        custom_step_details: Optional[CustomStepDetails] = core.arg(default=None)

        delete_step_details: Optional[DeleteStepDetails] = core.arg(default=None)

        tag_step_details: Optional[TagStepDetails] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Steps(core.Schema):

    copy_step_details: Optional[CopyStepDetails] = core.attr(CopyStepDetails, default=None)

    custom_step_details: Optional[CustomStepDetails] = core.attr(CustomStepDetails, default=None)

    delete_step_details: Optional[DeleteStepDetails] = core.attr(DeleteStepDetails, default=None)

    tag_step_details: Optional[TagStepDetails] = core.attr(TagStepDetails, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        copy_step_details: Optional[CopyStepDetails] = None,
        custom_step_details: Optional[CustomStepDetails] = None,
        delete_step_details: Optional[DeleteStepDetails] = None,
        tag_step_details: Optional[TagStepDetails] = None,
    ):
        super().__init__(
            args=Steps.Args(
                type=type,
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_step_details: Optional[CopyStepDetails] = core.arg(default=None)

        custom_step_details: Optional[CustomStepDetails] = core.arg(default=None)

        delete_step_details: Optional[DeleteStepDetails] = core.arg(default=None)

        tag_step_details: Optional[TagStepDetails] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_transfer_workflow", namespace="aws_transfer")
class Workflow(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    on_exception_steps: Optional[
        Union[List[OnExceptionSteps], core.ArrayOut[OnExceptionSteps]]
    ] = core.attr(OnExceptionSteps, default=None, kind=core.Kind.array)

    steps: Union[List[Steps], core.ArrayOut[Steps]] = core.attr(Steps, kind=core.Kind.array)

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
        steps: Union[List[Steps], core.ArrayOut[Steps]],
        description: Optional[Union[str, core.StringOut]] = None,
        on_exception_steps: Optional[
            Union[List[OnExceptionSteps], core.ArrayOut[OnExceptionSteps]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workflow.Args(
                steps=steps,
                description=description,
                on_exception_steps=on_exception_steps,
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

        on_exception_steps: Optional[
            Union[List[OnExceptionSteps], core.ArrayOut[OnExceptionSteps]]
        ] = core.arg(default=None)

        steps: Union[List[Steps], core.ArrayOut[Steps]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
