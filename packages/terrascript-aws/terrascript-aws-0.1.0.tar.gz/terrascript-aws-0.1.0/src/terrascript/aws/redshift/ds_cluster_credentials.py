from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_redshift_cluster_credentials", namespace="aws_redshift")
class DsClusterCredentials(core.Data):

    auto_create: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    db_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    db_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_password: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_user: Union[str, core.StringOut] = core.attr(str)

    duration_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    expiration: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        db_user: Union[str, core.StringOut],
        auto_create: Optional[Union[bool, core.BoolOut]] = None,
        db_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        db_name: Optional[Union[str, core.StringOut]] = None,
        duration_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsClusterCredentials.Args(
                cluster_identifier=cluster_identifier,
                db_user=db_user,
                auto_create=auto_create,
                db_groups=db_groups,
                db_name=db_name,
                duration_seconds=duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_create: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        db_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        db_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_user: Union[str, core.StringOut] = core.arg()

        duration_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)
