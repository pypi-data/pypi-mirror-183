from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_rds_cluster_activity_stream", namespace="aws_rds")
class ClusterActivityStream(core.Resource):

    engine_native_audit_fields_included: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kinesis_stream_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str)

    mode: Union[str, core.StringOut] = core.attr(str)

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        kms_key_id: Union[str, core.StringOut],
        mode: Union[str, core.StringOut],
        resource_arn: Union[str, core.StringOut],
        engine_native_audit_fields_included: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterActivityStream.Args(
                kms_key_id=kms_key_id,
                mode=mode,
                resource_arn=resource_arn,
                engine_native_audit_fields_included=engine_native_audit_fields_included,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        engine_native_audit_fields_included: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        kms_key_id: Union[str, core.StringOut] = core.arg()

        mode: Union[str, core.StringOut] = core.arg()

        resource_arn: Union[str, core.StringOut] = core.arg()
