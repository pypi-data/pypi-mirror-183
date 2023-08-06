from typing import List, Union

import terrascript.core as core


@core.schema
class LevelThree(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

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
class LevelFour(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

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
class HierarchyStructure(core.Schema):

    level_five: Union[List[LevelFive], core.ArrayOut[LevelFive]] = core.attr(
        LevelFive, computed=True, kind=core.Kind.array
    )

    level_four: Union[List[LevelFour], core.ArrayOut[LevelFour]] = core.attr(
        LevelFour, computed=True, kind=core.Kind.array
    )

    level_one: Union[List[LevelOne], core.ArrayOut[LevelOne]] = core.attr(
        LevelOne, computed=True, kind=core.Kind.array
    )

    level_three: Union[List[LevelThree], core.ArrayOut[LevelThree]] = core.attr(
        LevelThree, computed=True, kind=core.Kind.array
    )

    level_two: Union[List[LevelTwo], core.ArrayOut[LevelTwo]] = core.attr(
        LevelTwo, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        level_five: Union[List[LevelFive], core.ArrayOut[LevelFive]],
        level_four: Union[List[LevelFour], core.ArrayOut[LevelFour]],
        level_one: Union[List[LevelOne], core.ArrayOut[LevelOne]],
        level_three: Union[List[LevelThree], core.ArrayOut[LevelThree]],
        level_two: Union[List[LevelTwo], core.ArrayOut[LevelTwo]],
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
        level_five: Union[List[LevelFive], core.ArrayOut[LevelFive]] = core.arg()

        level_four: Union[List[LevelFour], core.ArrayOut[LevelFour]] = core.arg()

        level_one: Union[List[LevelOne], core.ArrayOut[LevelOne]] = core.arg()

        level_three: Union[List[LevelThree], core.ArrayOut[LevelThree]] = core.arg()

        level_two: Union[List[LevelTwo], core.ArrayOut[LevelTwo]] = core.arg()


@core.data(type="aws_connect_user_hierarchy_structure", namespace="aws_connect")
class DsUserHierarchyStructure(core.Data):

    hierarchy_structure: Union[
        List[HierarchyStructure], core.ArrayOut[HierarchyStructure]
    ] = core.attr(HierarchyStructure, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsUserHierarchyStructure.Args(
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: Union[str, core.StringOut] = core.arg()
