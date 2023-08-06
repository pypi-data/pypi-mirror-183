from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class GlobalFilter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=GlobalFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class PatchFilter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=PatchFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class ApprovalRule(core.Schema):

    approve_after_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    approve_until_date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compliance_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_non_security: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    patch_filter: Union[List[PatchFilter], core.ArrayOut[PatchFilter]] = core.attr(
        PatchFilter, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        patch_filter: Union[List[PatchFilter], core.ArrayOut[PatchFilter]],
        approve_after_days: Optional[Union[int, core.IntOut]] = None,
        approve_until_date: Optional[Union[str, core.StringOut]] = None,
        compliance_level: Optional[Union[str, core.StringOut]] = None,
        enable_non_security: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ApprovalRule.Args(
                patch_filter=patch_filter,
                approve_after_days=approve_after_days,
                approve_until_date=approve_until_date,
                compliance_level=compliance_level,
                enable_non_security=enable_non_security,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        approve_after_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        approve_until_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compliance_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_non_security: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        patch_filter: Union[List[PatchFilter], core.ArrayOut[PatchFilter]] = core.arg()


@core.schema
class Source(core.Schema):

    configuration: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    products: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        configuration: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        products: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Source.Args(
                configuration=configuration,
                name=name,
                products=products,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configuration: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        products: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_ssm_patch_baseline", namespace="aws_ssm")
class PatchBaseline(core.Resource):

    approval_rule: Optional[Union[List[ApprovalRule], core.ArrayOut[ApprovalRule]]] = core.attr(
        ApprovalRule, default=None, kind=core.Kind.array
    )

    approved_patches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    approved_patches_compliance_level: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    approved_patches_enable_non_security: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_filter: Optional[Union[List[GlobalFilter], core.ArrayOut[GlobalFilter]]] = core.attr(
        GlobalFilter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    operating_system: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rejected_patches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    rejected_patches_action: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source: Optional[Union[List[Source], core.ArrayOut[Source]]] = core.attr(
        Source, default=None, kind=core.Kind.array
    )

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
        name: Union[str, core.StringOut],
        approval_rule: Optional[Union[List[ApprovalRule], core.ArrayOut[ApprovalRule]]] = None,
        approved_patches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        approved_patches_compliance_level: Optional[Union[str, core.StringOut]] = None,
        approved_patches_enable_non_security: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        global_filter: Optional[Union[List[GlobalFilter], core.ArrayOut[GlobalFilter]]] = None,
        operating_system: Optional[Union[str, core.StringOut]] = None,
        rejected_patches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        rejected_patches_action: Optional[Union[str, core.StringOut]] = None,
        source: Optional[Union[List[Source], core.ArrayOut[Source]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PatchBaseline.Args(
                name=name,
                approval_rule=approval_rule,
                approved_patches=approved_patches,
                approved_patches_compliance_level=approved_patches_compliance_level,
                approved_patches_enable_non_security=approved_patches_enable_non_security,
                description=description,
                global_filter=global_filter,
                operating_system=operating_system,
                rejected_patches=rejected_patches,
                rejected_patches_action=rejected_patches_action,
                source=source,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        approval_rule: Optional[Union[List[ApprovalRule], core.ArrayOut[ApprovalRule]]] = core.arg(
            default=None
        )

        approved_patches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        approved_patches_compliance_level: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        approved_patches_enable_non_security: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_filter: Optional[Union[List[GlobalFilter], core.ArrayOut[GlobalFilter]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        operating_system: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rejected_patches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        rejected_patches_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source: Optional[Union[List[Source], core.ArrayOut[Source]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
