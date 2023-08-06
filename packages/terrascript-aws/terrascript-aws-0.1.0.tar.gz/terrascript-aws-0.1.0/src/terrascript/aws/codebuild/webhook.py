from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    exclude_matched_pattern: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    pattern: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        pattern: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        exclude_matched_pattern: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                pattern=pattern,
                type=type,
                exclude_matched_pattern=exclude_matched_pattern,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_matched_pattern: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        pattern: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class FilterGroup(core.Schema):

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
    ):
        super().__init__(
            args=FilterGroup.Args(
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)


@core.resource(type="aws_codebuild_webhook", namespace="aws_codebuild")
class Webhook(core.Resource):

    branch_filter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    build_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter_group: Optional[Union[List[FilterGroup], core.ArrayOut[FilterGroup]]] = core.attr(
        FilterGroup, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    payload_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    project_name: Union[str, core.StringOut] = core.attr(str)

    secret: Union[str, core.StringOut] = core.attr(str, computed=True)

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        project_name: Union[str, core.StringOut],
        branch_filter: Optional[Union[str, core.StringOut]] = None,
        build_type: Optional[Union[str, core.StringOut]] = None,
        filter_group: Optional[Union[List[FilterGroup], core.ArrayOut[FilterGroup]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Webhook.Args(
                project_name=project_name,
                branch_filter=branch_filter,
                build_type=build_type,
                filter_group=filter_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        branch_filter: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        build_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter_group: Optional[Union[List[FilterGroup], core.ArrayOut[FilterGroup]]] = core.arg(
            default=None
        )

        project_name: Union[str, core.StringOut] = core.arg()
