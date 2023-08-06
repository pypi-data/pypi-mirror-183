from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class GeoMatchConstraint(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=GeoMatchConstraint.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_geo_match_set", namespace="aws_wafregional")
class GeoMatchSet(core.Resource):

    geo_match_constraint: Optional[
        Union[List[GeoMatchConstraint], core.ArrayOut[GeoMatchConstraint]]
    ] = core.attr(GeoMatchConstraint, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        geo_match_constraint: Optional[
            Union[List[GeoMatchConstraint], core.ArrayOut[GeoMatchConstraint]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GeoMatchSet.Args(
                name=name,
                geo_match_constraint=geo_match_constraint,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        geo_match_constraint: Optional[
            Union[List[GeoMatchConstraint], core.ArrayOut[GeoMatchConstraint]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
