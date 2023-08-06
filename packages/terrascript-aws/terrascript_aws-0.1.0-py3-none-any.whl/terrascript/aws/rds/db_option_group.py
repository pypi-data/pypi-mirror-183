from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OptionSettings(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OptionSettings.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Option(core.Schema):

    db_security_group_memberships: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    option_name: Union[str, core.StringOut] = core.attr(str)

    option_settings: Optional[
        Union[List[OptionSettings], core.ArrayOut[OptionSettings]]
    ] = core.attr(OptionSettings, default=None, kind=core.Kind.array)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_security_group_memberships: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        option_name: Union[str, core.StringOut],
        db_security_group_memberships: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        option_settings: Optional[
            Union[List[OptionSettings], core.ArrayOut[OptionSettings]]
        ] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
        vpc_security_group_memberships: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
    ):
        super().__init__(
            args=Option.Args(
                option_name=option_name,
                db_security_group_memberships=db_security_group_memberships,
                option_settings=option_settings,
                port=port,
                version=version,
                vpc_security_group_memberships=vpc_security_group_memberships,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_security_group_memberships: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        option_name: Union[str, core.StringOut] = core.arg()

        option_settings: Optional[
            Union[List[OptionSettings], core.ArrayOut[OptionSettings]]
        ] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_security_group_memberships: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.resource(type="aws_db_option_group", namespace="aws_rds")
class DbOptionGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    major_engine_version: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    option: Optional[Union[List[Option], core.ArrayOut[Option]]] = core.attr(
        Option, default=None, kind=core.Kind.array
    )

    option_group_description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        engine_name: Union[str, core.StringOut],
        major_engine_version: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        option: Optional[Union[List[Option], core.ArrayOut[Option]]] = None,
        option_group_description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbOptionGroup.Args(
                engine_name=engine_name,
                major_engine_version=major_engine_version,
                name=name,
                name_prefix=name_prefix,
                option=option,
                option_group_description=option_group_description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        engine_name: Union[str, core.StringOut] = core.arg()

        major_engine_version: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        option: Optional[Union[List[Option], core.ArrayOut[Option]]] = core.arg(default=None)

        option_group_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
