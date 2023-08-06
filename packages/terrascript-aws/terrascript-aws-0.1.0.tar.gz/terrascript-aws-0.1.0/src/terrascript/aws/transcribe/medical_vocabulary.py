from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_transcribe_medical_vocabulary", namespace="aws_transcribe")
class MedicalVocabulary(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    download_uri: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    language_code: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vocabulary_file_uri: Union[str, core.StringOut] = core.attr(str)

    vocabulary_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        language_code: Union[str, core.StringOut],
        vocabulary_file_uri: Union[str, core.StringOut],
        vocabulary_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MedicalVocabulary.Args(
                language_code=language_code,
                vocabulary_file_uri=vocabulary_file_uri,
                vocabulary_name=vocabulary_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        language_code: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vocabulary_file_uri: Union[str, core.StringOut] = core.arg()

        vocabulary_name: Union[str, core.StringOut] = core.arg()
