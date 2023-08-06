from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Filters(core.Schema):

    application: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        application: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Filters.Args(
                application=application,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.data(type="aws_emr_release_labels", namespace="aws_emr")
class DsReleaseLabels(core.Data):

    filters: Optional[Filters] = core.attr(Filters, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The returned release labels.
    """
    release_labels: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filters: Optional[Filters] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsReleaseLabels.Args(
                filters=filters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filters: Optional[Filters] = core.arg(default=None)
