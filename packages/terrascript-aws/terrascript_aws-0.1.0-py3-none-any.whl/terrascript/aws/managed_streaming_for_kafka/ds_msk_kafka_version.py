from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_msk_kafka_version", namespace="aws_managed_streaming_for_kafka")
class DsMskKafkaVersion(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    preferred_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        preferred_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMskKafkaVersion.Args(
                preferred_versions=preferred_versions,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        preferred_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
