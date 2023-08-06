from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_acm_certificate", namespace="aws_acm")
class DsCertificate(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_chain: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    statuses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain: Union[str, core.StringOut],
        key_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
        statuses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificate.Args(
                domain=domain,
                key_types=key_types,
                most_recent=most_recent,
                statuses=statuses,
                tags=tags,
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: Union[str, core.StringOut] = core.arg()

        key_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        statuses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)
