from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Source(core.Schema):

    configuration: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    products: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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


@core.schema
class PatchFilter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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

    approve_after_days: Union[int, core.IntOut] = core.attr(int, computed=True)

    approve_until_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    compliance_level: Union[str, core.StringOut] = core.attr(str, computed=True)

    enable_non_security: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    patch_filter: Union[List[PatchFilter], core.ArrayOut[PatchFilter]] = core.attr(
        PatchFilter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        approve_after_days: Union[int, core.IntOut],
        approve_until_date: Union[str, core.StringOut],
        compliance_level: Union[str, core.StringOut],
        enable_non_security: Union[bool, core.BoolOut],
        patch_filter: Union[List[PatchFilter], core.ArrayOut[PatchFilter]],
    ):
        super().__init__(
            args=ApprovalRule.Args(
                approve_after_days=approve_after_days,
                approve_until_date=approve_until_date,
                compliance_level=compliance_level,
                enable_non_security=enable_non_security,
                patch_filter=patch_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        approve_after_days: Union[int, core.IntOut] = core.arg()

        approve_until_date: Union[str, core.StringOut] = core.arg()

        compliance_level: Union[str, core.StringOut] = core.arg()

        enable_non_security: Union[bool, core.BoolOut] = core.arg()

        patch_filter: Union[List[PatchFilter], core.ArrayOut[PatchFilter]] = core.arg()


@core.schema
class GlobalFilter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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


@core.data(type="aws_ssm_patch_baseline", namespace="aws_ssm")
class DsPatchBaseline(core.Data):

    approval_rule: Union[List[ApprovalRule], core.ArrayOut[ApprovalRule]] = core.attr(
        ApprovalRule, computed=True, kind=core.Kind.array
    )

    approved_patches: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    approved_patches_compliance_level: Union[str, core.StringOut] = core.attr(str, computed=True)

    approved_patches_enable_non_security: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    default_baseline: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_filter: Union[List[GlobalFilter], core.ArrayOut[GlobalFilter]] = core.attr(
        GlobalFilter, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    operating_system: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner: Union[str, core.StringOut] = core.attr(str)

    rejected_patches: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    rejected_patches_action: Union[str, core.StringOut] = core.attr(str, computed=True)

    source: Union[List[Source], core.ArrayOut[Source]] = core.attr(
        Source, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        owner: Union[str, core.StringOut],
        default_baseline: Optional[Union[bool, core.BoolOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        operating_system: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPatchBaseline.Args(
                owner=owner,
                default_baseline=default_baseline,
                name_prefix=name_prefix,
                operating_system=operating_system,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_baseline: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operating_system: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner: Union[str, core.StringOut] = core.arg()
