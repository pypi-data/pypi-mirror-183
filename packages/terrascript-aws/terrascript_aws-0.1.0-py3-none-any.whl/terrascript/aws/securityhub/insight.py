from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ThreatIntelIndicatorSourceUrl(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ThreatIntelIndicatorSourceUrl.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceRegion(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceRegion.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkSourceDomain(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkSourceDomain.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class DateRange(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=DateRange.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceLaunchedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceLaunchedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceAwsEc2InstanceSubnetId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceSubnetId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ComplianceStatus(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ComplianceStatus.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourcePartition(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourcePartition.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceTags(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceTags.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class MalwareType(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MalwareType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceType(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProductArn(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProductArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NoteUpdatedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NoteUpdatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ThreatIntelIndicatorType(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ThreatIntelIndicatorType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceImageId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceImageId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class MalwarePath(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MalwarePath.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProcessParentPid(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProcessParentPid.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FindingProviderFieldsTypes(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FindingProviderFieldsTypes.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Criticality(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Criticality.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceAwsEc2InstanceIpv4Addresses(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceIpv4Addresses.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class NoteText(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NoteText.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class RecordState(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RecordState.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class LastObservedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LastObservedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NetworkProtocol(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkProtocol.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceIamInstanceProfileArn(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceIamInstanceProfileArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceContainerImageId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceContainerImageId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Description(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Description.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceUrl(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceUrl.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class FindingProviderFieldsSeverityLabel(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FindingProviderFieldsSeverityLabel.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class RelatedFindingsProductArn(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RelatedFindingsProductArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Id(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Id.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class FindingProviderFieldsSeverityOriginal(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FindingProviderFieldsSeverityOriginal.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsIamAccessKeyUserName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsIamAccessKeyUserName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class MalwareName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MalwareName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class UpdatedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=UpdatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MalwareState(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MalwareState.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceIpv6Addresses(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceIpv6Addresses.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceKeyName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceKeyName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProductFields(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProductFields.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class RelatedFindingsId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RelatedFindingsId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkSourcePort(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NetworkSourcePort.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FindingProviderFieldsCriticality(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FindingProviderFieldsCriticality.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FindingProviderFieldsRelatedFindingsId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FindingProviderFieldsRelatedFindingsId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class FirstObservedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FirstObservedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceAwsS3BucketOwnerName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsS3BucketOwnerName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsIamAccessKeyStatus(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsIamAccessKeyStatus.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Confidence(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Confidence.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceAwsIamAccessKeyCreatedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ResourceAwsIamAccessKeyCreatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ProcessPid(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProcessPid.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class VerificationState(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VerificationState.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class FindingProviderFieldsConfidence(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FindingProviderFieldsConfidence.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WorkflowStatus(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=WorkflowStatus.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class CreatedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CreatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceAwsS3BucketOwnerId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsS3BucketOwnerId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Keyword(core.Schema):

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Keyword.Args(
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceContainerLaunchedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ResourceContainerLaunchedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkDestinationPort(core.Schema):

    eq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NetworkDestinationPort.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceDetailsOther(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceDetailsOther.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ThreatIntelIndicatorValue(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ThreatIntelIndicatorValue.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Type(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Type.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class GeneratorId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=GeneratorId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkSourceMac(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkSourceMac.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ThreatIntelIndicatorLastObservedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ThreatIntelIndicatorLastObservedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NetworkDirection(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkDirection.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class FindingProviderFieldsRelatedFindingsProductArn(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FindingProviderFieldsRelatedFindingsProductArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkDestinationIpv6(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkDestinationIpv6.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class ThreatIntelIndicatorCategory(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ThreatIntelIndicatorCategory.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkDestinationIpv4(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkDestinationIpv4.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class CompanyName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CompanyName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProcessPath(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProcessPath.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class AwsAccountId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AwsAccountId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ThreatIntelIndicatorSource(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ThreatIntelIndicatorSource.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkSourceIpv4(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkSourceIpv4.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkSourceIpv6(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkSourceIpv6.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceType(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Title(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Title.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkDestinationDomain(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkDestinationDomain.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class UserDefinedValues(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserDefinedValues.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class NoteUpdatedBy(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NoteUpdatedBy.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProcessName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProcessName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProcessTerminatedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProcessTerminatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RecommendationText(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RecommendationText.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceContainerImageName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceContainerImageName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceContainerName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceContainerName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ResourceAwsEc2InstanceVpcId(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceVpcId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProductName(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProductName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ProcessLaunchedAt(core.Schema):

    date_range: Optional[DateRange] = core.attr(DateRange, default=None)

    end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: Optional[DateRange] = None,
        end: Optional[Union[str, core.StringOut]] = None,
        start: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProcessLaunchedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: Optional[DateRange] = core.arg(default=None)

        end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SeverityLabel(core.Schema):

    comparison: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SeverityLabel.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Filters(core.Schema):

    aws_account_id: Optional[Union[List[AwsAccountId], core.ArrayOut[AwsAccountId]]] = core.attr(
        AwsAccountId, default=None, kind=core.Kind.array
    )

    company_name: Optional[Union[List[CompanyName], core.ArrayOut[CompanyName]]] = core.attr(
        CompanyName, default=None, kind=core.Kind.array
    )

    compliance_status: Optional[
        Union[List[ComplianceStatus], core.ArrayOut[ComplianceStatus]]
    ] = core.attr(ComplianceStatus, default=None, kind=core.Kind.array)

    confidence: Optional[Union[List[Confidence], core.ArrayOut[Confidence]]] = core.attr(
        Confidence, default=None, kind=core.Kind.array
    )

    created_at: Optional[Union[List[CreatedAt], core.ArrayOut[CreatedAt]]] = core.attr(
        CreatedAt, default=None, kind=core.Kind.array
    )

    criticality: Optional[Union[List[Criticality], core.ArrayOut[Criticality]]] = core.attr(
        Criticality, default=None, kind=core.Kind.array
    )

    description: Optional[Union[List[Description], core.ArrayOut[Description]]] = core.attr(
        Description, default=None, kind=core.Kind.array
    )

    finding_provider_fields_confidence: Optional[
        Union[List[FindingProviderFieldsConfidence], core.ArrayOut[FindingProviderFieldsConfidence]]
    ] = core.attr(FindingProviderFieldsConfidence, default=None, kind=core.Kind.array)

    finding_provider_fields_criticality: Optional[
        Union[
            List[FindingProviderFieldsCriticality], core.ArrayOut[FindingProviderFieldsCriticality]
        ]
    ] = core.attr(FindingProviderFieldsCriticality, default=None, kind=core.Kind.array)

    finding_provider_fields_related_findings_id: Optional[
        Union[
            List[FindingProviderFieldsRelatedFindingsId],
            core.ArrayOut[FindingProviderFieldsRelatedFindingsId],
        ]
    ] = core.attr(FindingProviderFieldsRelatedFindingsId, default=None, kind=core.Kind.array)

    finding_provider_fields_related_findings_product_arn: Optional[
        Union[
            List[FindingProviderFieldsRelatedFindingsProductArn],
            core.ArrayOut[FindingProviderFieldsRelatedFindingsProductArn],
        ]
    ] = core.attr(
        FindingProviderFieldsRelatedFindingsProductArn, default=None, kind=core.Kind.array
    )

    finding_provider_fields_severity_label: Optional[
        Union[
            List[FindingProviderFieldsSeverityLabel],
            core.ArrayOut[FindingProviderFieldsSeverityLabel],
        ]
    ] = core.attr(FindingProviderFieldsSeverityLabel, default=None, kind=core.Kind.array)

    finding_provider_fields_severity_original: Optional[
        Union[
            List[FindingProviderFieldsSeverityOriginal],
            core.ArrayOut[FindingProviderFieldsSeverityOriginal],
        ]
    ] = core.attr(FindingProviderFieldsSeverityOriginal, default=None, kind=core.Kind.array)

    finding_provider_fields_types: Optional[
        Union[List[FindingProviderFieldsTypes], core.ArrayOut[FindingProviderFieldsTypes]]
    ] = core.attr(FindingProviderFieldsTypes, default=None, kind=core.Kind.array)

    first_observed_at: Optional[
        Union[List[FirstObservedAt], core.ArrayOut[FirstObservedAt]]
    ] = core.attr(FirstObservedAt, default=None, kind=core.Kind.array)

    generator_id: Optional[Union[List[GeneratorId], core.ArrayOut[GeneratorId]]] = core.attr(
        GeneratorId, default=None, kind=core.Kind.array
    )

    id: Optional[Union[List[Id], core.ArrayOut[Id]]] = core.attr(
        Id, default=None, kind=core.Kind.array
    )

    keyword: Optional[Union[List[Keyword], core.ArrayOut[Keyword]]] = core.attr(
        Keyword, default=None, kind=core.Kind.array
    )

    last_observed_at: Optional[
        Union[List[LastObservedAt], core.ArrayOut[LastObservedAt]]
    ] = core.attr(LastObservedAt, default=None, kind=core.Kind.array)

    malware_name: Optional[Union[List[MalwareName], core.ArrayOut[MalwareName]]] = core.attr(
        MalwareName, default=None, kind=core.Kind.array
    )

    malware_path: Optional[Union[List[MalwarePath], core.ArrayOut[MalwarePath]]] = core.attr(
        MalwarePath, default=None, kind=core.Kind.array
    )

    malware_state: Optional[Union[List[MalwareState], core.ArrayOut[MalwareState]]] = core.attr(
        MalwareState, default=None, kind=core.Kind.array
    )

    malware_type: Optional[Union[List[MalwareType], core.ArrayOut[MalwareType]]] = core.attr(
        MalwareType, default=None, kind=core.Kind.array
    )

    network_destination_domain: Optional[
        Union[List[NetworkDestinationDomain], core.ArrayOut[NetworkDestinationDomain]]
    ] = core.attr(NetworkDestinationDomain, default=None, kind=core.Kind.array)

    network_destination_ipv4: Optional[
        Union[List[NetworkDestinationIpv4], core.ArrayOut[NetworkDestinationIpv4]]
    ] = core.attr(NetworkDestinationIpv4, default=None, kind=core.Kind.array)

    network_destination_ipv6: Optional[
        Union[List[NetworkDestinationIpv6], core.ArrayOut[NetworkDestinationIpv6]]
    ] = core.attr(NetworkDestinationIpv6, default=None, kind=core.Kind.array)

    network_destination_port: Optional[
        Union[List[NetworkDestinationPort], core.ArrayOut[NetworkDestinationPort]]
    ] = core.attr(NetworkDestinationPort, default=None, kind=core.Kind.array)

    network_direction: Optional[
        Union[List[NetworkDirection], core.ArrayOut[NetworkDirection]]
    ] = core.attr(NetworkDirection, default=None, kind=core.Kind.array)

    network_protocol: Optional[
        Union[List[NetworkProtocol], core.ArrayOut[NetworkProtocol]]
    ] = core.attr(NetworkProtocol, default=None, kind=core.Kind.array)

    network_source_domain: Optional[
        Union[List[NetworkSourceDomain], core.ArrayOut[NetworkSourceDomain]]
    ] = core.attr(NetworkSourceDomain, default=None, kind=core.Kind.array)

    network_source_ipv4: Optional[
        Union[List[NetworkSourceIpv4], core.ArrayOut[NetworkSourceIpv4]]
    ] = core.attr(NetworkSourceIpv4, default=None, kind=core.Kind.array)

    network_source_ipv6: Optional[
        Union[List[NetworkSourceIpv6], core.ArrayOut[NetworkSourceIpv6]]
    ] = core.attr(NetworkSourceIpv6, default=None, kind=core.Kind.array)

    network_source_mac: Optional[
        Union[List[NetworkSourceMac], core.ArrayOut[NetworkSourceMac]]
    ] = core.attr(NetworkSourceMac, default=None, kind=core.Kind.array)

    network_source_port: Optional[
        Union[List[NetworkSourcePort], core.ArrayOut[NetworkSourcePort]]
    ] = core.attr(NetworkSourcePort, default=None, kind=core.Kind.array)

    note_text: Optional[Union[List[NoteText], core.ArrayOut[NoteText]]] = core.attr(
        NoteText, default=None, kind=core.Kind.array
    )

    note_updated_at: Optional[Union[List[NoteUpdatedAt], core.ArrayOut[NoteUpdatedAt]]] = core.attr(
        NoteUpdatedAt, default=None, kind=core.Kind.array
    )

    note_updated_by: Optional[Union[List[NoteUpdatedBy], core.ArrayOut[NoteUpdatedBy]]] = core.attr(
        NoteUpdatedBy, default=None, kind=core.Kind.array
    )

    process_launched_at: Optional[
        Union[List[ProcessLaunchedAt], core.ArrayOut[ProcessLaunchedAt]]
    ] = core.attr(ProcessLaunchedAt, default=None, kind=core.Kind.array)

    process_name: Optional[Union[List[ProcessName], core.ArrayOut[ProcessName]]] = core.attr(
        ProcessName, default=None, kind=core.Kind.array
    )

    process_parent_pid: Optional[
        Union[List[ProcessParentPid], core.ArrayOut[ProcessParentPid]]
    ] = core.attr(ProcessParentPid, default=None, kind=core.Kind.array)

    process_path: Optional[Union[List[ProcessPath], core.ArrayOut[ProcessPath]]] = core.attr(
        ProcessPath, default=None, kind=core.Kind.array
    )

    process_pid: Optional[Union[List[ProcessPid], core.ArrayOut[ProcessPid]]] = core.attr(
        ProcessPid, default=None, kind=core.Kind.array
    )

    process_terminated_at: Optional[
        Union[List[ProcessTerminatedAt], core.ArrayOut[ProcessTerminatedAt]]
    ] = core.attr(ProcessTerminatedAt, default=None, kind=core.Kind.array)

    product_arn: Optional[Union[List[ProductArn], core.ArrayOut[ProductArn]]] = core.attr(
        ProductArn, default=None, kind=core.Kind.array
    )

    product_fields: Optional[Union[List[ProductFields], core.ArrayOut[ProductFields]]] = core.attr(
        ProductFields, default=None, kind=core.Kind.array
    )

    product_name: Optional[Union[List[ProductName], core.ArrayOut[ProductName]]] = core.attr(
        ProductName, default=None, kind=core.Kind.array
    )

    recommendation_text: Optional[
        Union[List[RecommendationText], core.ArrayOut[RecommendationText]]
    ] = core.attr(RecommendationText, default=None, kind=core.Kind.array)

    record_state: Optional[Union[List[RecordState], core.ArrayOut[RecordState]]] = core.attr(
        RecordState, default=None, kind=core.Kind.array
    )

    related_findings_id: Optional[
        Union[List[RelatedFindingsId], core.ArrayOut[RelatedFindingsId]]
    ] = core.attr(RelatedFindingsId, default=None, kind=core.Kind.array)

    related_findings_product_arn: Optional[
        Union[List[RelatedFindingsProductArn], core.ArrayOut[RelatedFindingsProductArn]]
    ] = core.attr(RelatedFindingsProductArn, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_iam_instance_profile_arn: Optional[
        Union[
            List[ResourceAwsEc2InstanceIamInstanceProfileArn],
            core.ArrayOut[ResourceAwsEc2InstanceIamInstanceProfileArn],
        ]
    ] = core.attr(ResourceAwsEc2InstanceIamInstanceProfileArn, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_image_id: Optional[
        Union[List[ResourceAwsEc2InstanceImageId], core.ArrayOut[ResourceAwsEc2InstanceImageId]]
    ] = core.attr(ResourceAwsEc2InstanceImageId, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_ipv4_addresses: Optional[
        Union[
            List[ResourceAwsEc2InstanceIpv4Addresses],
            core.ArrayOut[ResourceAwsEc2InstanceIpv4Addresses],
        ]
    ] = core.attr(ResourceAwsEc2InstanceIpv4Addresses, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_ipv6_addresses: Optional[
        Union[
            List[ResourceAwsEc2InstanceIpv6Addresses],
            core.ArrayOut[ResourceAwsEc2InstanceIpv6Addresses],
        ]
    ] = core.attr(ResourceAwsEc2InstanceIpv6Addresses, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_key_name: Optional[
        Union[List[ResourceAwsEc2InstanceKeyName], core.ArrayOut[ResourceAwsEc2InstanceKeyName]]
    ] = core.attr(ResourceAwsEc2InstanceKeyName, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_launched_at: Optional[
        Union[
            List[ResourceAwsEc2InstanceLaunchedAt], core.ArrayOut[ResourceAwsEc2InstanceLaunchedAt]
        ]
    ] = core.attr(ResourceAwsEc2InstanceLaunchedAt, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_subnet_id: Optional[
        Union[List[ResourceAwsEc2InstanceSubnetId], core.ArrayOut[ResourceAwsEc2InstanceSubnetId]]
    ] = core.attr(ResourceAwsEc2InstanceSubnetId, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_type: Optional[
        Union[List[ResourceAwsEc2InstanceType], core.ArrayOut[ResourceAwsEc2InstanceType]]
    ] = core.attr(ResourceAwsEc2InstanceType, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_vpc_id: Optional[
        Union[List[ResourceAwsEc2InstanceVpcId], core.ArrayOut[ResourceAwsEc2InstanceVpcId]]
    ] = core.attr(ResourceAwsEc2InstanceVpcId, default=None, kind=core.Kind.array)

    resource_aws_iam_access_key_created_at: Optional[
        Union[
            List[ResourceAwsIamAccessKeyCreatedAt], core.ArrayOut[ResourceAwsIamAccessKeyCreatedAt]
        ]
    ] = core.attr(ResourceAwsIamAccessKeyCreatedAt, default=None, kind=core.Kind.array)

    resource_aws_iam_access_key_status: Optional[
        Union[List[ResourceAwsIamAccessKeyStatus], core.ArrayOut[ResourceAwsIamAccessKeyStatus]]
    ] = core.attr(ResourceAwsIamAccessKeyStatus, default=None, kind=core.Kind.array)

    resource_aws_iam_access_key_user_name: Optional[
        Union[List[ResourceAwsIamAccessKeyUserName], core.ArrayOut[ResourceAwsIamAccessKeyUserName]]
    ] = core.attr(ResourceAwsIamAccessKeyUserName, default=None, kind=core.Kind.array)

    resource_aws_s3_bucket_owner_id: Optional[
        Union[List[ResourceAwsS3BucketOwnerId], core.ArrayOut[ResourceAwsS3BucketOwnerId]]
    ] = core.attr(ResourceAwsS3BucketOwnerId, default=None, kind=core.Kind.array)

    resource_aws_s3_bucket_owner_name: Optional[
        Union[List[ResourceAwsS3BucketOwnerName], core.ArrayOut[ResourceAwsS3BucketOwnerName]]
    ] = core.attr(ResourceAwsS3BucketOwnerName, default=None, kind=core.Kind.array)

    resource_container_image_id: Optional[
        Union[List[ResourceContainerImageId], core.ArrayOut[ResourceContainerImageId]]
    ] = core.attr(ResourceContainerImageId, default=None, kind=core.Kind.array)

    resource_container_image_name: Optional[
        Union[List[ResourceContainerImageName], core.ArrayOut[ResourceContainerImageName]]
    ] = core.attr(ResourceContainerImageName, default=None, kind=core.Kind.array)

    resource_container_launched_at: Optional[
        Union[List[ResourceContainerLaunchedAt], core.ArrayOut[ResourceContainerLaunchedAt]]
    ] = core.attr(ResourceContainerLaunchedAt, default=None, kind=core.Kind.array)

    resource_container_name: Optional[
        Union[List[ResourceContainerName], core.ArrayOut[ResourceContainerName]]
    ] = core.attr(ResourceContainerName, default=None, kind=core.Kind.array)

    resource_details_other: Optional[
        Union[List[ResourceDetailsOther], core.ArrayOut[ResourceDetailsOther]]
    ] = core.attr(ResourceDetailsOther, default=None, kind=core.Kind.array)

    resource_id: Optional[Union[List[ResourceId], core.ArrayOut[ResourceId]]] = core.attr(
        ResourceId, default=None, kind=core.Kind.array
    )

    resource_partition: Optional[
        Union[List[ResourcePartition], core.ArrayOut[ResourcePartition]]
    ] = core.attr(ResourcePartition, default=None, kind=core.Kind.array)

    resource_region: Optional[
        Union[List[ResourceRegion], core.ArrayOut[ResourceRegion]]
    ] = core.attr(ResourceRegion, default=None, kind=core.Kind.array)

    resource_tags: Optional[Union[List[ResourceTags], core.ArrayOut[ResourceTags]]] = core.attr(
        ResourceTags, default=None, kind=core.Kind.array
    )

    resource_type: Optional[Union[List[ResourceType], core.ArrayOut[ResourceType]]] = core.attr(
        ResourceType, default=None, kind=core.Kind.array
    )

    severity_label: Optional[Union[List[SeverityLabel], core.ArrayOut[SeverityLabel]]] = core.attr(
        SeverityLabel, default=None, kind=core.Kind.array
    )

    source_url: Optional[Union[List[SourceUrl], core.ArrayOut[SourceUrl]]] = core.attr(
        SourceUrl, default=None, kind=core.Kind.array
    )

    threat_intel_indicator_category: Optional[
        Union[List[ThreatIntelIndicatorCategory], core.ArrayOut[ThreatIntelIndicatorCategory]]
    ] = core.attr(ThreatIntelIndicatorCategory, default=None, kind=core.Kind.array)

    threat_intel_indicator_last_observed_at: Optional[
        Union[
            List[ThreatIntelIndicatorLastObservedAt],
            core.ArrayOut[ThreatIntelIndicatorLastObservedAt],
        ]
    ] = core.attr(ThreatIntelIndicatorLastObservedAt, default=None, kind=core.Kind.array)

    threat_intel_indicator_source: Optional[
        Union[List[ThreatIntelIndicatorSource], core.ArrayOut[ThreatIntelIndicatorSource]]
    ] = core.attr(ThreatIntelIndicatorSource, default=None, kind=core.Kind.array)

    threat_intel_indicator_source_url: Optional[
        Union[List[ThreatIntelIndicatorSourceUrl], core.ArrayOut[ThreatIntelIndicatorSourceUrl]]
    ] = core.attr(ThreatIntelIndicatorSourceUrl, default=None, kind=core.Kind.array)

    threat_intel_indicator_type: Optional[
        Union[List[ThreatIntelIndicatorType], core.ArrayOut[ThreatIntelIndicatorType]]
    ] = core.attr(ThreatIntelIndicatorType, default=None, kind=core.Kind.array)

    threat_intel_indicator_value: Optional[
        Union[List[ThreatIntelIndicatorValue], core.ArrayOut[ThreatIntelIndicatorValue]]
    ] = core.attr(ThreatIntelIndicatorValue, default=None, kind=core.Kind.array)

    title: Optional[Union[List[Title], core.ArrayOut[Title]]] = core.attr(
        Title, default=None, kind=core.Kind.array
    )

    type: Optional[Union[List[Type], core.ArrayOut[Type]]] = core.attr(
        Type, default=None, kind=core.Kind.array
    )

    updated_at: Optional[Union[List[UpdatedAt], core.ArrayOut[UpdatedAt]]] = core.attr(
        UpdatedAt, default=None, kind=core.Kind.array
    )

    user_defined_values: Optional[
        Union[List[UserDefinedValues], core.ArrayOut[UserDefinedValues]]
    ] = core.attr(UserDefinedValues, default=None, kind=core.Kind.array)

    verification_state: Optional[
        Union[List[VerificationState], core.ArrayOut[VerificationState]]
    ] = core.attr(VerificationState, default=None, kind=core.Kind.array)

    workflow_status: Optional[
        Union[List[WorkflowStatus], core.ArrayOut[WorkflowStatus]]
    ] = core.attr(WorkflowStatus, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        aws_account_id: Optional[Union[List[AwsAccountId], core.ArrayOut[AwsAccountId]]] = None,
        company_name: Optional[Union[List[CompanyName], core.ArrayOut[CompanyName]]] = None,
        compliance_status: Optional[
            Union[List[ComplianceStatus], core.ArrayOut[ComplianceStatus]]
        ] = None,
        confidence: Optional[Union[List[Confidence], core.ArrayOut[Confidence]]] = None,
        created_at: Optional[Union[List[CreatedAt], core.ArrayOut[CreatedAt]]] = None,
        criticality: Optional[Union[List[Criticality], core.ArrayOut[Criticality]]] = None,
        description: Optional[Union[List[Description], core.ArrayOut[Description]]] = None,
        finding_provider_fields_confidence: Optional[
            Union[
                List[FindingProviderFieldsConfidence],
                core.ArrayOut[FindingProviderFieldsConfidence],
            ]
        ] = None,
        finding_provider_fields_criticality: Optional[
            Union[
                List[FindingProviderFieldsCriticality],
                core.ArrayOut[FindingProviderFieldsCriticality],
            ]
        ] = None,
        finding_provider_fields_related_findings_id: Optional[
            Union[
                List[FindingProviderFieldsRelatedFindingsId],
                core.ArrayOut[FindingProviderFieldsRelatedFindingsId],
            ]
        ] = None,
        finding_provider_fields_related_findings_product_arn: Optional[
            Union[
                List[FindingProviderFieldsRelatedFindingsProductArn],
                core.ArrayOut[FindingProviderFieldsRelatedFindingsProductArn],
            ]
        ] = None,
        finding_provider_fields_severity_label: Optional[
            Union[
                List[FindingProviderFieldsSeverityLabel],
                core.ArrayOut[FindingProviderFieldsSeverityLabel],
            ]
        ] = None,
        finding_provider_fields_severity_original: Optional[
            Union[
                List[FindingProviderFieldsSeverityOriginal],
                core.ArrayOut[FindingProviderFieldsSeverityOriginal],
            ]
        ] = None,
        finding_provider_fields_types: Optional[
            Union[List[FindingProviderFieldsTypes], core.ArrayOut[FindingProviderFieldsTypes]]
        ] = None,
        first_observed_at: Optional[
            Union[List[FirstObservedAt], core.ArrayOut[FirstObservedAt]]
        ] = None,
        generator_id: Optional[Union[List[GeneratorId], core.ArrayOut[GeneratorId]]] = None,
        id: Optional[Union[List[Id], core.ArrayOut[Id]]] = None,
        keyword: Optional[Union[List[Keyword], core.ArrayOut[Keyword]]] = None,
        last_observed_at: Optional[
            Union[List[LastObservedAt], core.ArrayOut[LastObservedAt]]
        ] = None,
        malware_name: Optional[Union[List[MalwareName], core.ArrayOut[MalwareName]]] = None,
        malware_path: Optional[Union[List[MalwarePath], core.ArrayOut[MalwarePath]]] = None,
        malware_state: Optional[Union[List[MalwareState], core.ArrayOut[MalwareState]]] = None,
        malware_type: Optional[Union[List[MalwareType], core.ArrayOut[MalwareType]]] = None,
        network_destination_domain: Optional[
            Union[List[NetworkDestinationDomain], core.ArrayOut[NetworkDestinationDomain]]
        ] = None,
        network_destination_ipv4: Optional[
            Union[List[NetworkDestinationIpv4], core.ArrayOut[NetworkDestinationIpv4]]
        ] = None,
        network_destination_ipv6: Optional[
            Union[List[NetworkDestinationIpv6], core.ArrayOut[NetworkDestinationIpv6]]
        ] = None,
        network_destination_port: Optional[
            Union[List[NetworkDestinationPort], core.ArrayOut[NetworkDestinationPort]]
        ] = None,
        network_direction: Optional[
            Union[List[NetworkDirection], core.ArrayOut[NetworkDirection]]
        ] = None,
        network_protocol: Optional[
            Union[List[NetworkProtocol], core.ArrayOut[NetworkProtocol]]
        ] = None,
        network_source_domain: Optional[
            Union[List[NetworkSourceDomain], core.ArrayOut[NetworkSourceDomain]]
        ] = None,
        network_source_ipv4: Optional[
            Union[List[NetworkSourceIpv4], core.ArrayOut[NetworkSourceIpv4]]
        ] = None,
        network_source_ipv6: Optional[
            Union[List[NetworkSourceIpv6], core.ArrayOut[NetworkSourceIpv6]]
        ] = None,
        network_source_mac: Optional[
            Union[List[NetworkSourceMac], core.ArrayOut[NetworkSourceMac]]
        ] = None,
        network_source_port: Optional[
            Union[List[NetworkSourcePort], core.ArrayOut[NetworkSourcePort]]
        ] = None,
        note_text: Optional[Union[List[NoteText], core.ArrayOut[NoteText]]] = None,
        note_updated_at: Optional[Union[List[NoteUpdatedAt], core.ArrayOut[NoteUpdatedAt]]] = None,
        note_updated_by: Optional[Union[List[NoteUpdatedBy], core.ArrayOut[NoteUpdatedBy]]] = None,
        process_launched_at: Optional[
            Union[List[ProcessLaunchedAt], core.ArrayOut[ProcessLaunchedAt]]
        ] = None,
        process_name: Optional[Union[List[ProcessName], core.ArrayOut[ProcessName]]] = None,
        process_parent_pid: Optional[
            Union[List[ProcessParentPid], core.ArrayOut[ProcessParentPid]]
        ] = None,
        process_path: Optional[Union[List[ProcessPath], core.ArrayOut[ProcessPath]]] = None,
        process_pid: Optional[Union[List[ProcessPid], core.ArrayOut[ProcessPid]]] = None,
        process_terminated_at: Optional[
            Union[List[ProcessTerminatedAt], core.ArrayOut[ProcessTerminatedAt]]
        ] = None,
        product_arn: Optional[Union[List[ProductArn], core.ArrayOut[ProductArn]]] = None,
        product_fields: Optional[Union[List[ProductFields], core.ArrayOut[ProductFields]]] = None,
        product_name: Optional[Union[List[ProductName], core.ArrayOut[ProductName]]] = None,
        recommendation_text: Optional[
            Union[List[RecommendationText], core.ArrayOut[RecommendationText]]
        ] = None,
        record_state: Optional[Union[List[RecordState], core.ArrayOut[RecordState]]] = None,
        related_findings_id: Optional[
            Union[List[RelatedFindingsId], core.ArrayOut[RelatedFindingsId]]
        ] = None,
        related_findings_product_arn: Optional[
            Union[List[RelatedFindingsProductArn], core.ArrayOut[RelatedFindingsProductArn]]
        ] = None,
        resource_aws_ec2_instance_iam_instance_profile_arn: Optional[
            Union[
                List[ResourceAwsEc2InstanceIamInstanceProfileArn],
                core.ArrayOut[ResourceAwsEc2InstanceIamInstanceProfileArn],
            ]
        ] = None,
        resource_aws_ec2_instance_image_id: Optional[
            Union[List[ResourceAwsEc2InstanceImageId], core.ArrayOut[ResourceAwsEc2InstanceImageId]]
        ] = None,
        resource_aws_ec2_instance_ipv4_addresses: Optional[
            Union[
                List[ResourceAwsEc2InstanceIpv4Addresses],
                core.ArrayOut[ResourceAwsEc2InstanceIpv4Addresses],
            ]
        ] = None,
        resource_aws_ec2_instance_ipv6_addresses: Optional[
            Union[
                List[ResourceAwsEc2InstanceIpv6Addresses],
                core.ArrayOut[ResourceAwsEc2InstanceIpv6Addresses],
            ]
        ] = None,
        resource_aws_ec2_instance_key_name: Optional[
            Union[List[ResourceAwsEc2InstanceKeyName], core.ArrayOut[ResourceAwsEc2InstanceKeyName]]
        ] = None,
        resource_aws_ec2_instance_launched_at: Optional[
            Union[
                List[ResourceAwsEc2InstanceLaunchedAt],
                core.ArrayOut[ResourceAwsEc2InstanceLaunchedAt],
            ]
        ] = None,
        resource_aws_ec2_instance_subnet_id: Optional[
            Union[
                List[ResourceAwsEc2InstanceSubnetId], core.ArrayOut[ResourceAwsEc2InstanceSubnetId]
            ]
        ] = None,
        resource_aws_ec2_instance_type: Optional[
            Union[List[ResourceAwsEc2InstanceType], core.ArrayOut[ResourceAwsEc2InstanceType]]
        ] = None,
        resource_aws_ec2_instance_vpc_id: Optional[
            Union[List[ResourceAwsEc2InstanceVpcId], core.ArrayOut[ResourceAwsEc2InstanceVpcId]]
        ] = None,
        resource_aws_iam_access_key_created_at: Optional[
            Union[
                List[ResourceAwsIamAccessKeyCreatedAt],
                core.ArrayOut[ResourceAwsIamAccessKeyCreatedAt],
            ]
        ] = None,
        resource_aws_iam_access_key_status: Optional[
            Union[List[ResourceAwsIamAccessKeyStatus], core.ArrayOut[ResourceAwsIamAccessKeyStatus]]
        ] = None,
        resource_aws_iam_access_key_user_name: Optional[
            Union[
                List[ResourceAwsIamAccessKeyUserName],
                core.ArrayOut[ResourceAwsIamAccessKeyUserName],
            ]
        ] = None,
        resource_aws_s3_bucket_owner_id: Optional[
            Union[List[ResourceAwsS3BucketOwnerId], core.ArrayOut[ResourceAwsS3BucketOwnerId]]
        ] = None,
        resource_aws_s3_bucket_owner_name: Optional[
            Union[List[ResourceAwsS3BucketOwnerName], core.ArrayOut[ResourceAwsS3BucketOwnerName]]
        ] = None,
        resource_container_image_id: Optional[
            Union[List[ResourceContainerImageId], core.ArrayOut[ResourceContainerImageId]]
        ] = None,
        resource_container_image_name: Optional[
            Union[List[ResourceContainerImageName], core.ArrayOut[ResourceContainerImageName]]
        ] = None,
        resource_container_launched_at: Optional[
            Union[List[ResourceContainerLaunchedAt], core.ArrayOut[ResourceContainerLaunchedAt]]
        ] = None,
        resource_container_name: Optional[
            Union[List[ResourceContainerName], core.ArrayOut[ResourceContainerName]]
        ] = None,
        resource_details_other: Optional[
            Union[List[ResourceDetailsOther], core.ArrayOut[ResourceDetailsOther]]
        ] = None,
        resource_id: Optional[Union[List[ResourceId], core.ArrayOut[ResourceId]]] = None,
        resource_partition: Optional[
            Union[List[ResourcePartition], core.ArrayOut[ResourcePartition]]
        ] = None,
        resource_region: Optional[
            Union[List[ResourceRegion], core.ArrayOut[ResourceRegion]]
        ] = None,
        resource_tags: Optional[Union[List[ResourceTags], core.ArrayOut[ResourceTags]]] = None,
        resource_type: Optional[Union[List[ResourceType], core.ArrayOut[ResourceType]]] = None,
        severity_label: Optional[Union[List[SeverityLabel], core.ArrayOut[SeverityLabel]]] = None,
        source_url: Optional[Union[List[SourceUrl], core.ArrayOut[SourceUrl]]] = None,
        threat_intel_indicator_category: Optional[
            Union[List[ThreatIntelIndicatorCategory], core.ArrayOut[ThreatIntelIndicatorCategory]]
        ] = None,
        threat_intel_indicator_last_observed_at: Optional[
            Union[
                List[ThreatIntelIndicatorLastObservedAt],
                core.ArrayOut[ThreatIntelIndicatorLastObservedAt],
            ]
        ] = None,
        threat_intel_indicator_source: Optional[
            Union[List[ThreatIntelIndicatorSource], core.ArrayOut[ThreatIntelIndicatorSource]]
        ] = None,
        threat_intel_indicator_source_url: Optional[
            Union[List[ThreatIntelIndicatorSourceUrl], core.ArrayOut[ThreatIntelIndicatorSourceUrl]]
        ] = None,
        threat_intel_indicator_type: Optional[
            Union[List[ThreatIntelIndicatorType], core.ArrayOut[ThreatIntelIndicatorType]]
        ] = None,
        threat_intel_indicator_value: Optional[
            Union[List[ThreatIntelIndicatorValue], core.ArrayOut[ThreatIntelIndicatorValue]]
        ] = None,
        title: Optional[Union[List[Title], core.ArrayOut[Title]]] = None,
        type: Optional[Union[List[Type], core.ArrayOut[Type]]] = None,
        updated_at: Optional[Union[List[UpdatedAt], core.ArrayOut[UpdatedAt]]] = None,
        user_defined_values: Optional[
            Union[List[UserDefinedValues], core.ArrayOut[UserDefinedValues]]
        ] = None,
        verification_state: Optional[
            Union[List[VerificationState], core.ArrayOut[VerificationState]]
        ] = None,
        workflow_status: Optional[
            Union[List[WorkflowStatus], core.ArrayOut[WorkflowStatus]]
        ] = None,
    ):
        super().__init__(
            args=Filters.Args(
                aws_account_id=aws_account_id,
                company_name=company_name,
                compliance_status=compliance_status,
                confidence=confidence,
                created_at=created_at,
                criticality=criticality,
                description=description,
                finding_provider_fields_confidence=finding_provider_fields_confidence,
                finding_provider_fields_criticality=finding_provider_fields_criticality,
                finding_provider_fields_related_findings_id=finding_provider_fields_related_findings_id,
                finding_provider_fields_related_findings_product_arn=finding_provider_fields_related_findings_product_arn,
                finding_provider_fields_severity_label=finding_provider_fields_severity_label,
                finding_provider_fields_severity_original=finding_provider_fields_severity_original,
                finding_provider_fields_types=finding_provider_fields_types,
                first_observed_at=first_observed_at,
                generator_id=generator_id,
                id=id,
                keyword=keyword,
                last_observed_at=last_observed_at,
                malware_name=malware_name,
                malware_path=malware_path,
                malware_state=malware_state,
                malware_type=malware_type,
                network_destination_domain=network_destination_domain,
                network_destination_ipv4=network_destination_ipv4,
                network_destination_ipv6=network_destination_ipv6,
                network_destination_port=network_destination_port,
                network_direction=network_direction,
                network_protocol=network_protocol,
                network_source_domain=network_source_domain,
                network_source_ipv4=network_source_ipv4,
                network_source_ipv6=network_source_ipv6,
                network_source_mac=network_source_mac,
                network_source_port=network_source_port,
                note_text=note_text,
                note_updated_at=note_updated_at,
                note_updated_by=note_updated_by,
                process_launched_at=process_launched_at,
                process_name=process_name,
                process_parent_pid=process_parent_pid,
                process_path=process_path,
                process_pid=process_pid,
                process_terminated_at=process_terminated_at,
                product_arn=product_arn,
                product_fields=product_fields,
                product_name=product_name,
                recommendation_text=recommendation_text,
                record_state=record_state,
                related_findings_id=related_findings_id,
                related_findings_product_arn=related_findings_product_arn,
                resource_aws_ec2_instance_iam_instance_profile_arn=resource_aws_ec2_instance_iam_instance_profile_arn,
                resource_aws_ec2_instance_image_id=resource_aws_ec2_instance_image_id,
                resource_aws_ec2_instance_ipv4_addresses=resource_aws_ec2_instance_ipv4_addresses,
                resource_aws_ec2_instance_ipv6_addresses=resource_aws_ec2_instance_ipv6_addresses,
                resource_aws_ec2_instance_key_name=resource_aws_ec2_instance_key_name,
                resource_aws_ec2_instance_launched_at=resource_aws_ec2_instance_launched_at,
                resource_aws_ec2_instance_subnet_id=resource_aws_ec2_instance_subnet_id,
                resource_aws_ec2_instance_type=resource_aws_ec2_instance_type,
                resource_aws_ec2_instance_vpc_id=resource_aws_ec2_instance_vpc_id,
                resource_aws_iam_access_key_created_at=resource_aws_iam_access_key_created_at,
                resource_aws_iam_access_key_status=resource_aws_iam_access_key_status,
                resource_aws_iam_access_key_user_name=resource_aws_iam_access_key_user_name,
                resource_aws_s3_bucket_owner_id=resource_aws_s3_bucket_owner_id,
                resource_aws_s3_bucket_owner_name=resource_aws_s3_bucket_owner_name,
                resource_container_image_id=resource_container_image_id,
                resource_container_image_name=resource_container_image_name,
                resource_container_launched_at=resource_container_launched_at,
                resource_container_name=resource_container_name,
                resource_details_other=resource_details_other,
                resource_id=resource_id,
                resource_partition=resource_partition,
                resource_region=resource_region,
                resource_tags=resource_tags,
                resource_type=resource_type,
                severity_label=severity_label,
                source_url=source_url,
                threat_intel_indicator_category=threat_intel_indicator_category,
                threat_intel_indicator_last_observed_at=threat_intel_indicator_last_observed_at,
                threat_intel_indicator_source=threat_intel_indicator_source,
                threat_intel_indicator_source_url=threat_intel_indicator_source_url,
                threat_intel_indicator_type=threat_intel_indicator_type,
                threat_intel_indicator_value=threat_intel_indicator_value,
                title=title,
                type=type,
                updated_at=updated_at,
                user_defined_values=user_defined_values,
                verification_state=verification_state,
                workflow_status=workflow_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_account_id: Optional[Union[List[AwsAccountId], core.ArrayOut[AwsAccountId]]] = core.arg(
            default=None
        )

        company_name: Optional[Union[List[CompanyName], core.ArrayOut[CompanyName]]] = core.arg(
            default=None
        )

        compliance_status: Optional[
            Union[List[ComplianceStatus], core.ArrayOut[ComplianceStatus]]
        ] = core.arg(default=None)

        confidence: Optional[Union[List[Confidence], core.ArrayOut[Confidence]]] = core.arg(
            default=None
        )

        created_at: Optional[Union[List[CreatedAt], core.ArrayOut[CreatedAt]]] = core.arg(
            default=None
        )

        criticality: Optional[Union[List[Criticality], core.ArrayOut[Criticality]]] = core.arg(
            default=None
        )

        description: Optional[Union[List[Description], core.ArrayOut[Description]]] = core.arg(
            default=None
        )

        finding_provider_fields_confidence: Optional[
            Union[
                List[FindingProviderFieldsConfidence],
                core.ArrayOut[FindingProviderFieldsConfidence],
            ]
        ] = core.arg(default=None)

        finding_provider_fields_criticality: Optional[
            Union[
                List[FindingProviderFieldsCriticality],
                core.ArrayOut[FindingProviderFieldsCriticality],
            ]
        ] = core.arg(default=None)

        finding_provider_fields_related_findings_id: Optional[
            Union[
                List[FindingProviderFieldsRelatedFindingsId],
                core.ArrayOut[FindingProviderFieldsRelatedFindingsId],
            ]
        ] = core.arg(default=None)

        finding_provider_fields_related_findings_product_arn: Optional[
            Union[
                List[FindingProviderFieldsRelatedFindingsProductArn],
                core.ArrayOut[FindingProviderFieldsRelatedFindingsProductArn],
            ]
        ] = core.arg(default=None)

        finding_provider_fields_severity_label: Optional[
            Union[
                List[FindingProviderFieldsSeverityLabel],
                core.ArrayOut[FindingProviderFieldsSeverityLabel],
            ]
        ] = core.arg(default=None)

        finding_provider_fields_severity_original: Optional[
            Union[
                List[FindingProviderFieldsSeverityOriginal],
                core.ArrayOut[FindingProviderFieldsSeverityOriginal],
            ]
        ] = core.arg(default=None)

        finding_provider_fields_types: Optional[
            Union[List[FindingProviderFieldsTypes], core.ArrayOut[FindingProviderFieldsTypes]]
        ] = core.arg(default=None)

        first_observed_at: Optional[
            Union[List[FirstObservedAt], core.ArrayOut[FirstObservedAt]]
        ] = core.arg(default=None)

        generator_id: Optional[Union[List[GeneratorId], core.ArrayOut[GeneratorId]]] = core.arg(
            default=None
        )

        id: Optional[Union[List[Id], core.ArrayOut[Id]]] = core.arg(default=None)

        keyword: Optional[Union[List[Keyword], core.ArrayOut[Keyword]]] = core.arg(default=None)

        last_observed_at: Optional[
            Union[List[LastObservedAt], core.ArrayOut[LastObservedAt]]
        ] = core.arg(default=None)

        malware_name: Optional[Union[List[MalwareName], core.ArrayOut[MalwareName]]] = core.arg(
            default=None
        )

        malware_path: Optional[Union[List[MalwarePath], core.ArrayOut[MalwarePath]]] = core.arg(
            default=None
        )

        malware_state: Optional[Union[List[MalwareState], core.ArrayOut[MalwareState]]] = core.arg(
            default=None
        )

        malware_type: Optional[Union[List[MalwareType], core.ArrayOut[MalwareType]]] = core.arg(
            default=None
        )

        network_destination_domain: Optional[
            Union[List[NetworkDestinationDomain], core.ArrayOut[NetworkDestinationDomain]]
        ] = core.arg(default=None)

        network_destination_ipv4: Optional[
            Union[List[NetworkDestinationIpv4], core.ArrayOut[NetworkDestinationIpv4]]
        ] = core.arg(default=None)

        network_destination_ipv6: Optional[
            Union[List[NetworkDestinationIpv6], core.ArrayOut[NetworkDestinationIpv6]]
        ] = core.arg(default=None)

        network_destination_port: Optional[
            Union[List[NetworkDestinationPort], core.ArrayOut[NetworkDestinationPort]]
        ] = core.arg(default=None)

        network_direction: Optional[
            Union[List[NetworkDirection], core.ArrayOut[NetworkDirection]]
        ] = core.arg(default=None)

        network_protocol: Optional[
            Union[List[NetworkProtocol], core.ArrayOut[NetworkProtocol]]
        ] = core.arg(default=None)

        network_source_domain: Optional[
            Union[List[NetworkSourceDomain], core.ArrayOut[NetworkSourceDomain]]
        ] = core.arg(default=None)

        network_source_ipv4: Optional[
            Union[List[NetworkSourceIpv4], core.ArrayOut[NetworkSourceIpv4]]
        ] = core.arg(default=None)

        network_source_ipv6: Optional[
            Union[List[NetworkSourceIpv6], core.ArrayOut[NetworkSourceIpv6]]
        ] = core.arg(default=None)

        network_source_mac: Optional[
            Union[List[NetworkSourceMac], core.ArrayOut[NetworkSourceMac]]
        ] = core.arg(default=None)

        network_source_port: Optional[
            Union[List[NetworkSourcePort], core.ArrayOut[NetworkSourcePort]]
        ] = core.arg(default=None)

        note_text: Optional[Union[List[NoteText], core.ArrayOut[NoteText]]] = core.arg(default=None)

        note_updated_at: Optional[
            Union[List[NoteUpdatedAt], core.ArrayOut[NoteUpdatedAt]]
        ] = core.arg(default=None)

        note_updated_by: Optional[
            Union[List[NoteUpdatedBy], core.ArrayOut[NoteUpdatedBy]]
        ] = core.arg(default=None)

        process_launched_at: Optional[
            Union[List[ProcessLaunchedAt], core.ArrayOut[ProcessLaunchedAt]]
        ] = core.arg(default=None)

        process_name: Optional[Union[List[ProcessName], core.ArrayOut[ProcessName]]] = core.arg(
            default=None
        )

        process_parent_pid: Optional[
            Union[List[ProcessParentPid], core.ArrayOut[ProcessParentPid]]
        ] = core.arg(default=None)

        process_path: Optional[Union[List[ProcessPath], core.ArrayOut[ProcessPath]]] = core.arg(
            default=None
        )

        process_pid: Optional[Union[List[ProcessPid], core.ArrayOut[ProcessPid]]] = core.arg(
            default=None
        )

        process_terminated_at: Optional[
            Union[List[ProcessTerminatedAt], core.ArrayOut[ProcessTerminatedAt]]
        ] = core.arg(default=None)

        product_arn: Optional[Union[List[ProductArn], core.ArrayOut[ProductArn]]] = core.arg(
            default=None
        )

        product_fields: Optional[
            Union[List[ProductFields], core.ArrayOut[ProductFields]]
        ] = core.arg(default=None)

        product_name: Optional[Union[List[ProductName], core.ArrayOut[ProductName]]] = core.arg(
            default=None
        )

        recommendation_text: Optional[
            Union[List[RecommendationText], core.ArrayOut[RecommendationText]]
        ] = core.arg(default=None)

        record_state: Optional[Union[List[RecordState], core.ArrayOut[RecordState]]] = core.arg(
            default=None
        )

        related_findings_id: Optional[
            Union[List[RelatedFindingsId], core.ArrayOut[RelatedFindingsId]]
        ] = core.arg(default=None)

        related_findings_product_arn: Optional[
            Union[List[RelatedFindingsProductArn], core.ArrayOut[RelatedFindingsProductArn]]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_iam_instance_profile_arn: Optional[
            Union[
                List[ResourceAwsEc2InstanceIamInstanceProfileArn],
                core.ArrayOut[ResourceAwsEc2InstanceIamInstanceProfileArn],
            ]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_image_id: Optional[
            Union[List[ResourceAwsEc2InstanceImageId], core.ArrayOut[ResourceAwsEc2InstanceImageId]]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_ipv4_addresses: Optional[
            Union[
                List[ResourceAwsEc2InstanceIpv4Addresses],
                core.ArrayOut[ResourceAwsEc2InstanceIpv4Addresses],
            ]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_ipv6_addresses: Optional[
            Union[
                List[ResourceAwsEc2InstanceIpv6Addresses],
                core.ArrayOut[ResourceAwsEc2InstanceIpv6Addresses],
            ]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_key_name: Optional[
            Union[List[ResourceAwsEc2InstanceKeyName], core.ArrayOut[ResourceAwsEc2InstanceKeyName]]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_launched_at: Optional[
            Union[
                List[ResourceAwsEc2InstanceLaunchedAt],
                core.ArrayOut[ResourceAwsEc2InstanceLaunchedAt],
            ]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_subnet_id: Optional[
            Union[
                List[ResourceAwsEc2InstanceSubnetId], core.ArrayOut[ResourceAwsEc2InstanceSubnetId]
            ]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_type: Optional[
            Union[List[ResourceAwsEc2InstanceType], core.ArrayOut[ResourceAwsEc2InstanceType]]
        ] = core.arg(default=None)

        resource_aws_ec2_instance_vpc_id: Optional[
            Union[List[ResourceAwsEc2InstanceVpcId], core.ArrayOut[ResourceAwsEc2InstanceVpcId]]
        ] = core.arg(default=None)

        resource_aws_iam_access_key_created_at: Optional[
            Union[
                List[ResourceAwsIamAccessKeyCreatedAt],
                core.ArrayOut[ResourceAwsIamAccessKeyCreatedAt],
            ]
        ] = core.arg(default=None)

        resource_aws_iam_access_key_status: Optional[
            Union[List[ResourceAwsIamAccessKeyStatus], core.ArrayOut[ResourceAwsIamAccessKeyStatus]]
        ] = core.arg(default=None)

        resource_aws_iam_access_key_user_name: Optional[
            Union[
                List[ResourceAwsIamAccessKeyUserName],
                core.ArrayOut[ResourceAwsIamAccessKeyUserName],
            ]
        ] = core.arg(default=None)

        resource_aws_s3_bucket_owner_id: Optional[
            Union[List[ResourceAwsS3BucketOwnerId], core.ArrayOut[ResourceAwsS3BucketOwnerId]]
        ] = core.arg(default=None)

        resource_aws_s3_bucket_owner_name: Optional[
            Union[List[ResourceAwsS3BucketOwnerName], core.ArrayOut[ResourceAwsS3BucketOwnerName]]
        ] = core.arg(default=None)

        resource_container_image_id: Optional[
            Union[List[ResourceContainerImageId], core.ArrayOut[ResourceContainerImageId]]
        ] = core.arg(default=None)

        resource_container_image_name: Optional[
            Union[List[ResourceContainerImageName], core.ArrayOut[ResourceContainerImageName]]
        ] = core.arg(default=None)

        resource_container_launched_at: Optional[
            Union[List[ResourceContainerLaunchedAt], core.ArrayOut[ResourceContainerLaunchedAt]]
        ] = core.arg(default=None)

        resource_container_name: Optional[
            Union[List[ResourceContainerName], core.ArrayOut[ResourceContainerName]]
        ] = core.arg(default=None)

        resource_details_other: Optional[
            Union[List[ResourceDetailsOther], core.ArrayOut[ResourceDetailsOther]]
        ] = core.arg(default=None)

        resource_id: Optional[Union[List[ResourceId], core.ArrayOut[ResourceId]]] = core.arg(
            default=None
        )

        resource_partition: Optional[
            Union[List[ResourcePartition], core.ArrayOut[ResourcePartition]]
        ] = core.arg(default=None)

        resource_region: Optional[
            Union[List[ResourceRegion], core.ArrayOut[ResourceRegion]]
        ] = core.arg(default=None)

        resource_tags: Optional[Union[List[ResourceTags], core.ArrayOut[ResourceTags]]] = core.arg(
            default=None
        )

        resource_type: Optional[Union[List[ResourceType], core.ArrayOut[ResourceType]]] = core.arg(
            default=None
        )

        severity_label: Optional[
            Union[List[SeverityLabel], core.ArrayOut[SeverityLabel]]
        ] = core.arg(default=None)

        source_url: Optional[Union[List[SourceUrl], core.ArrayOut[SourceUrl]]] = core.arg(
            default=None
        )

        threat_intel_indicator_category: Optional[
            Union[List[ThreatIntelIndicatorCategory], core.ArrayOut[ThreatIntelIndicatorCategory]]
        ] = core.arg(default=None)

        threat_intel_indicator_last_observed_at: Optional[
            Union[
                List[ThreatIntelIndicatorLastObservedAt],
                core.ArrayOut[ThreatIntelIndicatorLastObservedAt],
            ]
        ] = core.arg(default=None)

        threat_intel_indicator_source: Optional[
            Union[List[ThreatIntelIndicatorSource], core.ArrayOut[ThreatIntelIndicatorSource]]
        ] = core.arg(default=None)

        threat_intel_indicator_source_url: Optional[
            Union[List[ThreatIntelIndicatorSourceUrl], core.ArrayOut[ThreatIntelIndicatorSourceUrl]]
        ] = core.arg(default=None)

        threat_intel_indicator_type: Optional[
            Union[List[ThreatIntelIndicatorType], core.ArrayOut[ThreatIntelIndicatorType]]
        ] = core.arg(default=None)

        threat_intel_indicator_value: Optional[
            Union[List[ThreatIntelIndicatorValue], core.ArrayOut[ThreatIntelIndicatorValue]]
        ] = core.arg(default=None)

        title: Optional[Union[List[Title], core.ArrayOut[Title]]] = core.arg(default=None)

        type: Optional[Union[List[Type], core.ArrayOut[Type]]] = core.arg(default=None)

        updated_at: Optional[Union[List[UpdatedAt], core.ArrayOut[UpdatedAt]]] = core.arg(
            default=None
        )

        user_defined_values: Optional[
            Union[List[UserDefinedValues], core.ArrayOut[UserDefinedValues]]
        ] = core.arg(default=None)

        verification_state: Optional[
            Union[List[VerificationState], core.ArrayOut[VerificationState]]
        ] = core.arg(default=None)

        workflow_status: Optional[
            Union[List[WorkflowStatus], core.ArrayOut[WorkflowStatus]]
        ] = core.arg(default=None)


@core.resource(type="aws_securityhub_insight", namespace="aws_securityhub")
class Insight(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    filters: Filters = core.attr(Filters)

    group_by_attribute: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        filters: Filters,
        group_by_attribute: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Insight.Args(
                filters=filters,
                group_by_attribute=group_by_attribute,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        filters: Filters = core.arg()

        group_by_attribute: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
