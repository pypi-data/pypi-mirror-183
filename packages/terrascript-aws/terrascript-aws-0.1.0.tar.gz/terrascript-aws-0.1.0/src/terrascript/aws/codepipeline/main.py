from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionKey(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionKey.Args(
                id=id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ArtifactStore(core.Schema):

    encryption_key: Optional[EncryptionKey] = core.attr(EncryptionKey, default=None)

    location: Union[str, core.StringOut] = core.attr(str)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        location: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        encryption_key: Optional[EncryptionKey] = None,
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ArtifactStore.Args(
                location=location,
                type=type,
                encryption_key=encryption_key,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_key: Optional[EncryptionKey] = core.arg(default=None)

        location: Union[str, core.StringOut] = core.arg()

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Action(core.Schema):

    category: Union[str, core.StringOut] = core.attr(str)

    configuration: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    input_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    namespace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    output_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    owner: Union[str, core.StringOut] = core.attr(str)

    provider: Union[str, core.StringOut] = core.attr(str)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    run_order: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        category: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        owner: Union[str, core.StringOut],
        provider: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
        configuration: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        input_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        namespace: Optional[Union[str, core.StringOut]] = None,
        output_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        run_order: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Action.Args(
                category=category,
                name=name,
                owner=owner,
                provider=provider,
                version=version,
                configuration=configuration,
                input_artifacts=input_artifacts,
                namespace=namespace,
                output_artifacts=output_artifacts,
                region=region,
                role_arn=role_arn,
                run_order=run_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        category: Union[str, core.StringOut] = core.arg()

        configuration: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        input_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        output_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        owner: Union[str, core.StringOut] = core.arg()

        provider: Union[str, core.StringOut] = core.arg()

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        run_order: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        version: Union[str, core.StringOut] = core.arg()


@core.schema
class Stage(core.Schema):

    action: Union[List[Action], core.ArrayOut[Action]] = core.attr(Action, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action: Union[List[Action], core.ArrayOut[Action]],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Stage.Args(
                action=action,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[List[Action], core.ArrayOut[Action]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_codepipeline", namespace="aws_codepipeline")
class Main(core.Resource):
    """
    The codepipeline ARN.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    artifact_store: Union[List[ArtifactStore], core.ArrayOut[ArtifactStore]] = core.attr(
        ArtifactStore, kind=core.Kind.array
    )

    """
    (Required) The KMS key ARN or ID
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The name of the pipeline.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make
    calls to AWS services on your behalf.
    """
    role_arn: Union[str, core.StringOut] = core.attr(str)

    stage: Union[List[Stage], core.ArrayOut[Stage]] = core.attr(Stage, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        artifact_store: Union[List[ArtifactStore], core.ArrayOut[ArtifactStore]],
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        stage: Union[List[Stage], core.ArrayOut[Stage]],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                artifact_store=artifact_store,
                name=name,
                role_arn=role_arn,
                stage=stage,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifact_store: Union[List[ArtifactStore], core.ArrayOut[ArtifactStore]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        stage: Union[List[Stage], core.ArrayOut[Stage]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
