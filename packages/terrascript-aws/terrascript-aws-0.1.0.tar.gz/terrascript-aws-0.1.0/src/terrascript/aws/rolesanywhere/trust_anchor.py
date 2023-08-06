from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SourceData(core.Schema):

    acm_pca_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    x509_certificate_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        acm_pca_arn: Optional[Union[str, core.StringOut]] = None,
        x509_certificate_data: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SourceData.Args(
                acm_pca_arn=acm_pca_arn,
                x509_certificate_data=x509_certificate_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm_pca_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        x509_certificate_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Source(core.Schema):

    source_data: SourceData = core.attr(SourceData)

    source_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source_data: SourceData,
        source_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Source.Args(
                source_data=source_data,
                source_type=source_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source_data: SourceData = core.arg()

        source_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_rolesanywhere_trust_anchor", namespace="aws_rolesanywhere")
class TrustAnchor(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    source: Source = core.attr(Source)

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
        name: Union[str, core.StringOut],
        source: Source,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrustAnchor.Args(
                name=name,
                source=source,
                enabled=enabled,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        source: Source = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
