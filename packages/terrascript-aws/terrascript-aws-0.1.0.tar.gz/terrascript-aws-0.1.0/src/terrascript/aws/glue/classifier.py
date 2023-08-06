from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CsvClassifier(core.Schema):

    allow_single_column: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    contains_header: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    delimiter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    disable_value_trimming: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    header: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    quote_symbol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        allow_single_column: Optional[Union[bool, core.BoolOut]] = None,
        contains_header: Optional[Union[str, core.StringOut]] = None,
        delimiter: Optional[Union[str, core.StringOut]] = None,
        disable_value_trimming: Optional[Union[bool, core.BoolOut]] = None,
        header: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        quote_symbol: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CsvClassifier.Args(
                allow_single_column=allow_single_column,
                contains_header=contains_header,
                delimiter=delimiter,
                disable_value_trimming=disable_value_trimming,
                header=header,
                quote_symbol=quote_symbol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_single_column: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        contains_header: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delimiter: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disable_value_trimming: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        header: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        quote_symbol: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class GrokClassifier(core.Schema):

    classification: Union[str, core.StringOut] = core.attr(str)

    custom_patterns: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    grok_pattern: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        classification: Union[str, core.StringOut],
        grok_pattern: Union[str, core.StringOut],
        custom_patterns: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=GrokClassifier.Args(
                classification=classification,
                grok_pattern=grok_pattern,
                custom_patterns=custom_patterns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: Union[str, core.StringOut] = core.arg()

        custom_patterns: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        grok_pattern: Union[str, core.StringOut] = core.arg()


@core.schema
class JsonClassifier(core.Schema):

    json_path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        json_path: Union[str, core.StringOut],
    ):
        super().__init__(
            args=JsonClassifier.Args(
                json_path=json_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_path: Union[str, core.StringOut] = core.arg()


@core.schema
class XmlClassifier(core.Schema):

    classification: Union[str, core.StringOut] = core.attr(str)

    row_tag: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        classification: Union[str, core.StringOut],
        row_tag: Union[str, core.StringOut],
    ):
        super().__init__(
            args=XmlClassifier.Args(
                classification=classification,
                row_tag=row_tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: Union[str, core.StringOut] = core.arg()

        row_tag: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_glue_classifier", namespace="aws_glue")
class Classifier(core.Resource):

    csv_classifier: Optional[CsvClassifier] = core.attr(CsvClassifier, default=None)

    grok_classifier: Optional[GrokClassifier] = core.attr(GrokClassifier, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    json_classifier: Optional[JsonClassifier] = core.attr(JsonClassifier, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    xml_classifier: Optional[XmlClassifier] = core.attr(XmlClassifier, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        csv_classifier: Optional[CsvClassifier] = None,
        grok_classifier: Optional[GrokClassifier] = None,
        json_classifier: Optional[JsonClassifier] = None,
        xml_classifier: Optional[XmlClassifier] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Classifier.Args(
                name=name,
                csv_classifier=csv_classifier,
                grok_classifier=grok_classifier,
                json_classifier=json_classifier,
                xml_classifier=xml_classifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        csv_classifier: Optional[CsvClassifier] = core.arg(default=None)

        grok_classifier: Optional[GrokClassifier] = core.arg(default=None)

        json_classifier: Optional[JsonClassifier] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        xml_classifier: Optional[XmlClassifier] = core.arg(default=None)
