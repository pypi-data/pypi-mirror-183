from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_location_geofence_collection", namespace="aws_location")
class DsGeofenceCollection(core.Data):

    collection_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    collection_name: Union[str, core.StringOut] = core.attr(str)

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        collection_name: Union[str, core.StringOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGeofenceCollection.Args(
                collection_name=collection_name,
                kms_key_id=kms_key_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        collection_name: Union[str, core.StringOut] = core.arg()

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
