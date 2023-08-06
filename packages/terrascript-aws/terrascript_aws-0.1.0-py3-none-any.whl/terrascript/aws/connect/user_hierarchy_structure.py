from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class LevelFour(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LevelFour.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LevelFive(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LevelFive.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LevelOne(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LevelOne.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LevelTwo(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LevelTwo.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LevelThree(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LevelThree.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class HierarchyStructure(core.Schema):

    level_five: Optional[LevelFive] = core.attr(LevelFive, default=None, computed=True)

    level_four: Optional[LevelFour] = core.attr(LevelFour, default=None, computed=True)

    level_one: Optional[LevelOne] = core.attr(LevelOne, default=None, computed=True)

    level_three: Optional[LevelThree] = core.attr(LevelThree, default=None, computed=True)

    level_two: Optional[LevelTwo] = core.attr(LevelTwo, default=None, computed=True)

    def __init__(
        self,
        *,
        level_five: Optional[LevelFive] = None,
        level_four: Optional[LevelFour] = None,
        level_one: Optional[LevelOne] = None,
        level_three: Optional[LevelThree] = None,
        level_two: Optional[LevelTwo] = None,
    ):
        super().__init__(
            args=HierarchyStructure.Args(
                level_five=level_five,
                level_four=level_four,
                level_one=level_one,
                level_three=level_three,
                level_two=level_two,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        level_five: Optional[LevelFive] = core.arg(default=None)

        level_four: Optional[LevelFour] = core.arg(default=None)

        level_one: Optional[LevelOne] = core.arg(default=None)

        level_three: Optional[LevelThree] = core.arg(default=None)

        level_two: Optional[LevelTwo] = core.arg(default=None)


@core.resource(type="aws_connect_user_hierarchy_structure", namespace="aws_connect")
class UserHierarchyStructure(core.Resource):

    hierarchy_structure: HierarchyStructure = core.attr(HierarchyStructure)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        hierarchy_structure: HierarchyStructure,
        instance_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserHierarchyStructure.Args(
                hierarchy_structure=hierarchy_structure,
                instance_id=instance_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hierarchy_structure: HierarchyStructure = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()
