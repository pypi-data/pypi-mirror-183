from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_neptune_engine_version", namespace="aws_neptune")
class DsEngineVersion(core.Data):
    """
    (Optional) DB engine. (Default: `neptune`)
    """

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    The description of the database engine.
    """
    engine_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Set of log types that the database engine has available for export to CloudWatch Logs.
    """
    exportable_log_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) The name of a specific DB parameter group family. An example parameter group family is `n
    eptune1`.
    """
    parameter_group_family: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Ordered list of preferred engine versions. The first match in this list will be returned.
    If no preferred matches are found and the original search returned more than one result, an error i
    s returned. If both the `version` and `preferred_versions` arguments are not configured, the data so
    urce will return the default version for the engine.
    """
    preferred_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Set of the time zones supported by this engine.
    """
    supported_timezones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Indicates whether the engine version supports exporting the log types specified by `exportable_log_t
    ypes` to CloudWatch Logs.
    """
    supports_log_exports_to_cloudwatch: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    """
    Indicates whether the database engine version supports read replicas.
    """
    supports_read_replica: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    """
    Set of engine versions that this database engine version can be upgraded to.
    """
    valid_upgrade_targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Version of the DB engine. For example, `1.0.1.0`, `1.0.2.2`, and `1.0.3.0`. If both the `
    version` and `preferred_versions` arguments are not configured, the data source will return the defa
    ult version for the engine.
    """
    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    The description of the database engine version.
    """
    version_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        engine: Optional[Union[str, core.StringOut]] = None,
        parameter_group_family: Optional[Union[str, core.StringOut]] = None,
        preferred_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEngineVersion.Args(
                engine=engine,
                parameter_group_family=parameter_group_family,
                preferred_versions=preferred_versions,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter_group_family: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
