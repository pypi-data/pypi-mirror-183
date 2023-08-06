from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_default_tags", namespace="aws_meta_data_sources")
class DsDefaultTags(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Blocks of default tags set on the provider. See details below.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDefaultTags.Args(
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
