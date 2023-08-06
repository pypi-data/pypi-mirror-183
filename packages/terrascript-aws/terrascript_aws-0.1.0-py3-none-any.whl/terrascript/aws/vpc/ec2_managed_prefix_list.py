from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Entry(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Entry.Args(
                cidr=cidr,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ec2_managed_prefix_list", namespace="aws_vpc")
class Ec2ManagedPrefixList(core.Resource):

    address_family: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    entry: Optional[Union[List[Entry], core.ArrayOut[Entry]]] = core.attr(
        Entry, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_entries: Union[int, core.IntOut] = core.attr(int)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: Union[str, core.StringOut],
        max_entries: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
        entry: Optional[Union[List[Entry], core.ArrayOut[Entry]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ManagedPrefixList.Args(
                address_family=address_family,
                max_entries=max_entries,
                name=name,
                entry=entry,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: Union[str, core.StringOut] = core.arg()

        entry: Optional[Union[List[Entry], core.ArrayOut[Entry]]] = core.arg(default=None)

        max_entries: Union[int, core.IntOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
