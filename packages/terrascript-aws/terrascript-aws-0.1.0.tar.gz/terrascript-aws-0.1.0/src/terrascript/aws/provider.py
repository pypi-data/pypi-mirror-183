from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DefaultTags(core.Schema):

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=DefaultTags.Args(
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Endpoints(core.Schema):

    accessanalyzer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    account: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    acm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    acmpca: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    alexaforbusiness: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    amg: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    amp: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    amplify: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    amplifybackend: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    amplifyuibuilder: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    apigateway: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    apigatewaymanagementapi: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    apigatewayv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appautoscaling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appconfig: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appconfigdata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appflow: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appintegrations: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appintegrationsservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    applicationautoscaling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    applicationcostprofiler: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    applicationdiscovery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    applicationdiscoveryservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    applicationinsights: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appmesh: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appregistry: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    apprunner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appstream: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    appsync: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    athena: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    auditmanager: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    augmentedairuntime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    autoscaling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    autoscalingplans: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    backup: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    backupgateway: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    batch: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    beanstalk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    billingconductor: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    braket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    budgets: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ce: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    chime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    chimesdkidentity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    chimesdkmeetings: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    chimesdkmessaging: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloud9: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudcontrol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudcontrolapi: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    clouddirectory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudformation: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudfront: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudhsm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudhsmv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudsearch: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudsearchdomain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudtrail: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatch: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatchevents: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatchevidently: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatchlog: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatchlogs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatchrum: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codeartifact: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codebuild: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codecommit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codedeploy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codeguruprofiler: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codegurureviewer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codepipeline: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codestar: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codestarconnections: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codestarnotifications: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cognitoidentity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cognitoidentityprovider: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cognitoidp: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cognitosync: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    comprehend: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    comprehendmedical: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    computeoptimizer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    config: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    configservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connectcontactlens: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connectparticipant: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connectwisdomservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    costandusagereportservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    costexplorer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cur: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    customerprofiles: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    databasemigration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    databasemigrationservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    databrew: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dataexchange: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    datapipeline: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    datasync: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dax: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deploy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    detective: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    devicefarm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    devopsguru: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    directconnect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    directoryservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    discovery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dlm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dms: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    docdb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    drs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ds: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dynamodb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dynamodbstreams: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ec2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ec2instanceconnect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ecr: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ecrpublic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ecs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    efs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    eks: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticache: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticbeanstalk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticinference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticloadbalancing: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticloadbalancingv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticsearch: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticsearchservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elastictranscoder: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elbv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    emr: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    emrcontainers: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    emrserverless: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    es: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    eventbridge: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    events: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    evidently: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    finspace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    finspacedata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    firehose: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fis: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fms: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    forecast: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    forecastquery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    forecastqueryservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    forecastservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    frauddetector: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fsx: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gamelift: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    glacier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    globalaccelerator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    glue: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gluedatabrew: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    grafana: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    greengrass: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    greengrassv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    groundstation: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    guardduty: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    health: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    healthlake: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    honeycode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    identitystore: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    imagebuilder: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    inspector: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    inspector2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iot: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iot1clickdevices: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iot1clickdevicesservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iot1clickprojects: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotanalytics: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotdata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotdataplane: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotdeviceadvisor: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotevents: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ioteventsdata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotfleethub: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotjobsdata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotjobsdataplane: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotsecuretunneling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotsitewise: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotthingsgraph: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iottwinmaker: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iotwireless: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ivs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kafka: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kafkaconnect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kendra: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    keyspaces: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesis: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisanalytics: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisanalyticsv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisvideo: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisvideoarchivedmedia: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisvideomedia: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisvideosignaling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kinesisvideosignalingchannels: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    kms: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lakeformation: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lambda_: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, alias="lambda")

    lex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexmodelbuilding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexmodelbuildingservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexmodels: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexmodelsv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexruntime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexruntimeservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexruntimev2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexv2models: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lexv2runtime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    licensemanager: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lightsail: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    locationservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    logs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lookoutequipment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lookoutforvision: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lookoutmetrics: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lookoutvision: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    machinelearning: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    macie: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    macie2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    managedblockchain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    managedgrafana: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    marketplacecatalog: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    marketplacecommerceanalytics: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    marketplaceentitlement: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    marketplaceentitlementservice: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    marketplacemetering: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediaconnect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediaconvert: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    medialive: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediapackage: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediapackagevod: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediastore: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediastoredata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mediatailor: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    memorydb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    meteringmarketplace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mgh: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mgn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    migrationhub: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    migrationhubconfig: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    migrationhubrefactorspaces: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    migrationhubstrategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    migrationhubstrategyrecommendations: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    mobile: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mq: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    msk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mturk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mwaa: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    neptune: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    networkfirewall: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    networkmanager: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    nimble: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    nimblestudio: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    opensearch: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    opensearchservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    opsworks: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    opsworkscm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    organizations: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outposts: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    panorama: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    personalize: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    personalizeevents: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    personalizeruntime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pi: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pinpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pinpointemail: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pinpointsmsvoice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    polly: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pricing: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prometheus: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prometheusservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    proton: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    qldb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    qldbsession: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    quicksight: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ram: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rbin: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rds: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rdsdata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rdsdataservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    recyclebin: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redshift: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redshiftdata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redshiftdataapiservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redshiftserverless: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rekognition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resiliencehub: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resourcegroups: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resourcegroupstagging: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resourcegroupstaggingapi: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    robomaker: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rolesanywhere: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    route53: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    route53domains: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    route53recoverycluster: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    route53recoverycontrolconfig: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    route53recoveryreadiness: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    route53resolver: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rum: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3api: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3control: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3outposts: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemaker: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemakera2iruntime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemakeredge: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemakeredgemanager: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemakerfeaturestoreruntime: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    sagemakerruntime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    savingsplans: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schemas: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sdb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secretsmanager: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    securityhub: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    serverlessapplicationrepository: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    serverlessapprepo: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    serverlessrepo: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    servicecatalog: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    servicecatalogappregistry: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    servicediscovery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    servicequotas: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ses: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sesv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sfn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    shield: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    signer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    simpledb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sms: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snowball: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snowdevicemanagement: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sns: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sqs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssmcontacts: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssmincidents: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sso: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssoadmin: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssooidc: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stepfunctions: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    storagegateway: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sts: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    support: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    swf: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    synthetics: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    textract: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timestreamquery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timestreamwrite: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transcribe: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transcribeservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transcribestreaming: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transcribestreamingservice: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transfer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    translate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    voiceid: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    waf: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wafregional: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wafv2: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wellarchitected: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wisdom: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workdocs: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    worklink: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workmail: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workmailmessageflow: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workspaces: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workspacesweb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    xray: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        accessanalyzer: Optional[Union[str, core.StringOut]] = None,
        account: Optional[Union[str, core.StringOut]] = None,
        acm: Optional[Union[str, core.StringOut]] = None,
        acmpca: Optional[Union[str, core.StringOut]] = None,
        alexaforbusiness: Optional[Union[str, core.StringOut]] = None,
        amg: Optional[Union[str, core.StringOut]] = None,
        amp: Optional[Union[str, core.StringOut]] = None,
        amplify: Optional[Union[str, core.StringOut]] = None,
        amplifybackend: Optional[Union[str, core.StringOut]] = None,
        amplifyuibuilder: Optional[Union[str, core.StringOut]] = None,
        apigateway: Optional[Union[str, core.StringOut]] = None,
        apigatewaymanagementapi: Optional[Union[str, core.StringOut]] = None,
        apigatewayv2: Optional[Union[str, core.StringOut]] = None,
        appautoscaling: Optional[Union[str, core.StringOut]] = None,
        appconfig: Optional[Union[str, core.StringOut]] = None,
        appconfigdata: Optional[Union[str, core.StringOut]] = None,
        appflow: Optional[Union[str, core.StringOut]] = None,
        appintegrations: Optional[Union[str, core.StringOut]] = None,
        appintegrationsservice: Optional[Union[str, core.StringOut]] = None,
        applicationautoscaling: Optional[Union[str, core.StringOut]] = None,
        applicationcostprofiler: Optional[Union[str, core.StringOut]] = None,
        applicationdiscovery: Optional[Union[str, core.StringOut]] = None,
        applicationdiscoveryservice: Optional[Union[str, core.StringOut]] = None,
        applicationinsights: Optional[Union[str, core.StringOut]] = None,
        appmesh: Optional[Union[str, core.StringOut]] = None,
        appregistry: Optional[Union[str, core.StringOut]] = None,
        apprunner: Optional[Union[str, core.StringOut]] = None,
        appstream: Optional[Union[str, core.StringOut]] = None,
        appsync: Optional[Union[str, core.StringOut]] = None,
        athena: Optional[Union[str, core.StringOut]] = None,
        auditmanager: Optional[Union[str, core.StringOut]] = None,
        augmentedairuntime: Optional[Union[str, core.StringOut]] = None,
        autoscaling: Optional[Union[str, core.StringOut]] = None,
        autoscalingplans: Optional[Union[str, core.StringOut]] = None,
        backup: Optional[Union[str, core.StringOut]] = None,
        backupgateway: Optional[Union[str, core.StringOut]] = None,
        batch: Optional[Union[str, core.StringOut]] = None,
        beanstalk: Optional[Union[str, core.StringOut]] = None,
        billingconductor: Optional[Union[str, core.StringOut]] = None,
        braket: Optional[Union[str, core.StringOut]] = None,
        budgets: Optional[Union[str, core.StringOut]] = None,
        ce: Optional[Union[str, core.StringOut]] = None,
        chime: Optional[Union[str, core.StringOut]] = None,
        chimesdkidentity: Optional[Union[str, core.StringOut]] = None,
        chimesdkmeetings: Optional[Union[str, core.StringOut]] = None,
        chimesdkmessaging: Optional[Union[str, core.StringOut]] = None,
        cloud9: Optional[Union[str, core.StringOut]] = None,
        cloudcontrol: Optional[Union[str, core.StringOut]] = None,
        cloudcontrolapi: Optional[Union[str, core.StringOut]] = None,
        clouddirectory: Optional[Union[str, core.StringOut]] = None,
        cloudformation: Optional[Union[str, core.StringOut]] = None,
        cloudfront: Optional[Union[str, core.StringOut]] = None,
        cloudhsm: Optional[Union[str, core.StringOut]] = None,
        cloudhsmv2: Optional[Union[str, core.StringOut]] = None,
        cloudsearch: Optional[Union[str, core.StringOut]] = None,
        cloudsearchdomain: Optional[Union[str, core.StringOut]] = None,
        cloudtrail: Optional[Union[str, core.StringOut]] = None,
        cloudwatch: Optional[Union[str, core.StringOut]] = None,
        cloudwatchevents: Optional[Union[str, core.StringOut]] = None,
        cloudwatchevidently: Optional[Union[str, core.StringOut]] = None,
        cloudwatchlog: Optional[Union[str, core.StringOut]] = None,
        cloudwatchlogs: Optional[Union[str, core.StringOut]] = None,
        cloudwatchrum: Optional[Union[str, core.StringOut]] = None,
        codeartifact: Optional[Union[str, core.StringOut]] = None,
        codebuild: Optional[Union[str, core.StringOut]] = None,
        codecommit: Optional[Union[str, core.StringOut]] = None,
        codedeploy: Optional[Union[str, core.StringOut]] = None,
        codeguruprofiler: Optional[Union[str, core.StringOut]] = None,
        codegurureviewer: Optional[Union[str, core.StringOut]] = None,
        codepipeline: Optional[Union[str, core.StringOut]] = None,
        codestar: Optional[Union[str, core.StringOut]] = None,
        codestarconnections: Optional[Union[str, core.StringOut]] = None,
        codestarnotifications: Optional[Union[str, core.StringOut]] = None,
        cognitoidentity: Optional[Union[str, core.StringOut]] = None,
        cognitoidentityprovider: Optional[Union[str, core.StringOut]] = None,
        cognitoidp: Optional[Union[str, core.StringOut]] = None,
        cognitosync: Optional[Union[str, core.StringOut]] = None,
        comprehend: Optional[Union[str, core.StringOut]] = None,
        comprehendmedical: Optional[Union[str, core.StringOut]] = None,
        computeoptimizer: Optional[Union[str, core.StringOut]] = None,
        config: Optional[Union[str, core.StringOut]] = None,
        configservice: Optional[Union[str, core.StringOut]] = None,
        connect: Optional[Union[str, core.StringOut]] = None,
        connectcontactlens: Optional[Union[str, core.StringOut]] = None,
        connectparticipant: Optional[Union[str, core.StringOut]] = None,
        connectwisdomservice: Optional[Union[str, core.StringOut]] = None,
        costandusagereportservice: Optional[Union[str, core.StringOut]] = None,
        costexplorer: Optional[Union[str, core.StringOut]] = None,
        cur: Optional[Union[str, core.StringOut]] = None,
        customerprofiles: Optional[Union[str, core.StringOut]] = None,
        databasemigration: Optional[Union[str, core.StringOut]] = None,
        databasemigrationservice: Optional[Union[str, core.StringOut]] = None,
        databrew: Optional[Union[str, core.StringOut]] = None,
        dataexchange: Optional[Union[str, core.StringOut]] = None,
        datapipeline: Optional[Union[str, core.StringOut]] = None,
        datasync: Optional[Union[str, core.StringOut]] = None,
        dax: Optional[Union[str, core.StringOut]] = None,
        deploy: Optional[Union[str, core.StringOut]] = None,
        detective: Optional[Union[str, core.StringOut]] = None,
        devicefarm: Optional[Union[str, core.StringOut]] = None,
        devopsguru: Optional[Union[str, core.StringOut]] = None,
        directconnect: Optional[Union[str, core.StringOut]] = None,
        directoryservice: Optional[Union[str, core.StringOut]] = None,
        discovery: Optional[Union[str, core.StringOut]] = None,
        dlm: Optional[Union[str, core.StringOut]] = None,
        dms: Optional[Union[str, core.StringOut]] = None,
        docdb: Optional[Union[str, core.StringOut]] = None,
        drs: Optional[Union[str, core.StringOut]] = None,
        ds: Optional[Union[str, core.StringOut]] = None,
        dynamodb: Optional[Union[str, core.StringOut]] = None,
        dynamodbstreams: Optional[Union[str, core.StringOut]] = None,
        ebs: Optional[Union[str, core.StringOut]] = None,
        ec2: Optional[Union[str, core.StringOut]] = None,
        ec2instanceconnect: Optional[Union[str, core.StringOut]] = None,
        ecr: Optional[Union[str, core.StringOut]] = None,
        ecrpublic: Optional[Union[str, core.StringOut]] = None,
        ecs: Optional[Union[str, core.StringOut]] = None,
        efs: Optional[Union[str, core.StringOut]] = None,
        eks: Optional[Union[str, core.StringOut]] = None,
        elasticache: Optional[Union[str, core.StringOut]] = None,
        elasticbeanstalk: Optional[Union[str, core.StringOut]] = None,
        elasticinference: Optional[Union[str, core.StringOut]] = None,
        elasticloadbalancing: Optional[Union[str, core.StringOut]] = None,
        elasticloadbalancingv2: Optional[Union[str, core.StringOut]] = None,
        elasticsearch: Optional[Union[str, core.StringOut]] = None,
        elasticsearchservice: Optional[Union[str, core.StringOut]] = None,
        elastictranscoder: Optional[Union[str, core.StringOut]] = None,
        elb: Optional[Union[str, core.StringOut]] = None,
        elbv2: Optional[Union[str, core.StringOut]] = None,
        emr: Optional[Union[str, core.StringOut]] = None,
        emrcontainers: Optional[Union[str, core.StringOut]] = None,
        emrserverless: Optional[Union[str, core.StringOut]] = None,
        es: Optional[Union[str, core.StringOut]] = None,
        eventbridge: Optional[Union[str, core.StringOut]] = None,
        events: Optional[Union[str, core.StringOut]] = None,
        evidently: Optional[Union[str, core.StringOut]] = None,
        finspace: Optional[Union[str, core.StringOut]] = None,
        finspacedata: Optional[Union[str, core.StringOut]] = None,
        firehose: Optional[Union[str, core.StringOut]] = None,
        fis: Optional[Union[str, core.StringOut]] = None,
        fms: Optional[Union[str, core.StringOut]] = None,
        forecast: Optional[Union[str, core.StringOut]] = None,
        forecastquery: Optional[Union[str, core.StringOut]] = None,
        forecastqueryservice: Optional[Union[str, core.StringOut]] = None,
        forecastservice: Optional[Union[str, core.StringOut]] = None,
        frauddetector: Optional[Union[str, core.StringOut]] = None,
        fsx: Optional[Union[str, core.StringOut]] = None,
        gamelift: Optional[Union[str, core.StringOut]] = None,
        glacier: Optional[Union[str, core.StringOut]] = None,
        globalaccelerator: Optional[Union[str, core.StringOut]] = None,
        glue: Optional[Union[str, core.StringOut]] = None,
        gluedatabrew: Optional[Union[str, core.StringOut]] = None,
        grafana: Optional[Union[str, core.StringOut]] = None,
        greengrass: Optional[Union[str, core.StringOut]] = None,
        greengrassv2: Optional[Union[str, core.StringOut]] = None,
        groundstation: Optional[Union[str, core.StringOut]] = None,
        guardduty: Optional[Union[str, core.StringOut]] = None,
        health: Optional[Union[str, core.StringOut]] = None,
        healthlake: Optional[Union[str, core.StringOut]] = None,
        honeycode: Optional[Union[str, core.StringOut]] = None,
        iam: Optional[Union[str, core.StringOut]] = None,
        identitystore: Optional[Union[str, core.StringOut]] = None,
        imagebuilder: Optional[Union[str, core.StringOut]] = None,
        inspector: Optional[Union[str, core.StringOut]] = None,
        inspector2: Optional[Union[str, core.StringOut]] = None,
        iot: Optional[Union[str, core.StringOut]] = None,
        iot1clickdevices: Optional[Union[str, core.StringOut]] = None,
        iot1clickdevicesservice: Optional[Union[str, core.StringOut]] = None,
        iot1clickprojects: Optional[Union[str, core.StringOut]] = None,
        iotanalytics: Optional[Union[str, core.StringOut]] = None,
        iotdata: Optional[Union[str, core.StringOut]] = None,
        iotdataplane: Optional[Union[str, core.StringOut]] = None,
        iotdeviceadvisor: Optional[Union[str, core.StringOut]] = None,
        iotevents: Optional[Union[str, core.StringOut]] = None,
        ioteventsdata: Optional[Union[str, core.StringOut]] = None,
        iotfleethub: Optional[Union[str, core.StringOut]] = None,
        iotjobsdata: Optional[Union[str, core.StringOut]] = None,
        iotjobsdataplane: Optional[Union[str, core.StringOut]] = None,
        iotsecuretunneling: Optional[Union[str, core.StringOut]] = None,
        iotsitewise: Optional[Union[str, core.StringOut]] = None,
        iotthingsgraph: Optional[Union[str, core.StringOut]] = None,
        iottwinmaker: Optional[Union[str, core.StringOut]] = None,
        iotwireless: Optional[Union[str, core.StringOut]] = None,
        ivs: Optional[Union[str, core.StringOut]] = None,
        kafka: Optional[Union[str, core.StringOut]] = None,
        kafkaconnect: Optional[Union[str, core.StringOut]] = None,
        kendra: Optional[Union[str, core.StringOut]] = None,
        keyspaces: Optional[Union[str, core.StringOut]] = None,
        kinesis: Optional[Union[str, core.StringOut]] = None,
        kinesisanalytics: Optional[Union[str, core.StringOut]] = None,
        kinesisanalyticsv2: Optional[Union[str, core.StringOut]] = None,
        kinesisvideo: Optional[Union[str, core.StringOut]] = None,
        kinesisvideoarchivedmedia: Optional[Union[str, core.StringOut]] = None,
        kinesisvideomedia: Optional[Union[str, core.StringOut]] = None,
        kinesisvideosignaling: Optional[Union[str, core.StringOut]] = None,
        kinesisvideosignalingchannels: Optional[Union[str, core.StringOut]] = None,
        kms: Optional[Union[str, core.StringOut]] = None,
        lakeformation: Optional[Union[str, core.StringOut]] = None,
        lambda_: Optional[Union[str, core.StringOut]] = None,
        lex: Optional[Union[str, core.StringOut]] = None,
        lexmodelbuilding: Optional[Union[str, core.StringOut]] = None,
        lexmodelbuildingservice: Optional[Union[str, core.StringOut]] = None,
        lexmodels: Optional[Union[str, core.StringOut]] = None,
        lexmodelsv2: Optional[Union[str, core.StringOut]] = None,
        lexruntime: Optional[Union[str, core.StringOut]] = None,
        lexruntimeservice: Optional[Union[str, core.StringOut]] = None,
        lexruntimev2: Optional[Union[str, core.StringOut]] = None,
        lexv2models: Optional[Union[str, core.StringOut]] = None,
        lexv2runtime: Optional[Union[str, core.StringOut]] = None,
        licensemanager: Optional[Union[str, core.StringOut]] = None,
        lightsail: Optional[Union[str, core.StringOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        locationservice: Optional[Union[str, core.StringOut]] = None,
        logs: Optional[Union[str, core.StringOut]] = None,
        lookoutequipment: Optional[Union[str, core.StringOut]] = None,
        lookoutforvision: Optional[Union[str, core.StringOut]] = None,
        lookoutmetrics: Optional[Union[str, core.StringOut]] = None,
        lookoutvision: Optional[Union[str, core.StringOut]] = None,
        machinelearning: Optional[Union[str, core.StringOut]] = None,
        macie: Optional[Union[str, core.StringOut]] = None,
        macie2: Optional[Union[str, core.StringOut]] = None,
        managedblockchain: Optional[Union[str, core.StringOut]] = None,
        managedgrafana: Optional[Union[str, core.StringOut]] = None,
        marketplacecatalog: Optional[Union[str, core.StringOut]] = None,
        marketplacecommerceanalytics: Optional[Union[str, core.StringOut]] = None,
        marketplaceentitlement: Optional[Union[str, core.StringOut]] = None,
        marketplaceentitlementservice: Optional[Union[str, core.StringOut]] = None,
        marketplacemetering: Optional[Union[str, core.StringOut]] = None,
        mediaconnect: Optional[Union[str, core.StringOut]] = None,
        mediaconvert: Optional[Union[str, core.StringOut]] = None,
        medialive: Optional[Union[str, core.StringOut]] = None,
        mediapackage: Optional[Union[str, core.StringOut]] = None,
        mediapackagevod: Optional[Union[str, core.StringOut]] = None,
        mediastore: Optional[Union[str, core.StringOut]] = None,
        mediastoredata: Optional[Union[str, core.StringOut]] = None,
        mediatailor: Optional[Union[str, core.StringOut]] = None,
        memorydb: Optional[Union[str, core.StringOut]] = None,
        meteringmarketplace: Optional[Union[str, core.StringOut]] = None,
        mgh: Optional[Union[str, core.StringOut]] = None,
        mgn: Optional[Union[str, core.StringOut]] = None,
        migrationhub: Optional[Union[str, core.StringOut]] = None,
        migrationhubconfig: Optional[Union[str, core.StringOut]] = None,
        migrationhubrefactorspaces: Optional[Union[str, core.StringOut]] = None,
        migrationhubstrategy: Optional[Union[str, core.StringOut]] = None,
        migrationhubstrategyrecommendations: Optional[Union[str, core.StringOut]] = None,
        mobile: Optional[Union[str, core.StringOut]] = None,
        mq: Optional[Union[str, core.StringOut]] = None,
        msk: Optional[Union[str, core.StringOut]] = None,
        mturk: Optional[Union[str, core.StringOut]] = None,
        mwaa: Optional[Union[str, core.StringOut]] = None,
        neptune: Optional[Union[str, core.StringOut]] = None,
        networkfirewall: Optional[Union[str, core.StringOut]] = None,
        networkmanager: Optional[Union[str, core.StringOut]] = None,
        nimble: Optional[Union[str, core.StringOut]] = None,
        nimblestudio: Optional[Union[str, core.StringOut]] = None,
        opensearch: Optional[Union[str, core.StringOut]] = None,
        opensearchservice: Optional[Union[str, core.StringOut]] = None,
        opsworks: Optional[Union[str, core.StringOut]] = None,
        opsworkscm: Optional[Union[str, core.StringOut]] = None,
        organizations: Optional[Union[str, core.StringOut]] = None,
        outposts: Optional[Union[str, core.StringOut]] = None,
        panorama: Optional[Union[str, core.StringOut]] = None,
        personalize: Optional[Union[str, core.StringOut]] = None,
        personalizeevents: Optional[Union[str, core.StringOut]] = None,
        personalizeruntime: Optional[Union[str, core.StringOut]] = None,
        pi: Optional[Union[str, core.StringOut]] = None,
        pinpoint: Optional[Union[str, core.StringOut]] = None,
        pinpointemail: Optional[Union[str, core.StringOut]] = None,
        pinpointsmsvoice: Optional[Union[str, core.StringOut]] = None,
        polly: Optional[Union[str, core.StringOut]] = None,
        pricing: Optional[Union[str, core.StringOut]] = None,
        prometheus: Optional[Union[str, core.StringOut]] = None,
        prometheusservice: Optional[Union[str, core.StringOut]] = None,
        proton: Optional[Union[str, core.StringOut]] = None,
        qldb: Optional[Union[str, core.StringOut]] = None,
        qldbsession: Optional[Union[str, core.StringOut]] = None,
        quicksight: Optional[Union[str, core.StringOut]] = None,
        ram: Optional[Union[str, core.StringOut]] = None,
        rbin: Optional[Union[str, core.StringOut]] = None,
        rds: Optional[Union[str, core.StringOut]] = None,
        rdsdata: Optional[Union[str, core.StringOut]] = None,
        rdsdataservice: Optional[Union[str, core.StringOut]] = None,
        recyclebin: Optional[Union[str, core.StringOut]] = None,
        redshift: Optional[Union[str, core.StringOut]] = None,
        redshiftdata: Optional[Union[str, core.StringOut]] = None,
        redshiftdataapiservice: Optional[Union[str, core.StringOut]] = None,
        redshiftserverless: Optional[Union[str, core.StringOut]] = None,
        rekognition: Optional[Union[str, core.StringOut]] = None,
        resiliencehub: Optional[Union[str, core.StringOut]] = None,
        resourcegroups: Optional[Union[str, core.StringOut]] = None,
        resourcegroupstagging: Optional[Union[str, core.StringOut]] = None,
        resourcegroupstaggingapi: Optional[Union[str, core.StringOut]] = None,
        robomaker: Optional[Union[str, core.StringOut]] = None,
        rolesanywhere: Optional[Union[str, core.StringOut]] = None,
        route53: Optional[Union[str, core.StringOut]] = None,
        route53domains: Optional[Union[str, core.StringOut]] = None,
        route53recoverycluster: Optional[Union[str, core.StringOut]] = None,
        route53recoverycontrolconfig: Optional[Union[str, core.StringOut]] = None,
        route53recoveryreadiness: Optional[Union[str, core.StringOut]] = None,
        route53resolver: Optional[Union[str, core.StringOut]] = None,
        rum: Optional[Union[str, core.StringOut]] = None,
        s3: Optional[Union[str, core.StringOut]] = None,
        s3api: Optional[Union[str, core.StringOut]] = None,
        s3control: Optional[Union[str, core.StringOut]] = None,
        s3outposts: Optional[Union[str, core.StringOut]] = None,
        sagemaker: Optional[Union[str, core.StringOut]] = None,
        sagemakera2iruntime: Optional[Union[str, core.StringOut]] = None,
        sagemakeredge: Optional[Union[str, core.StringOut]] = None,
        sagemakeredgemanager: Optional[Union[str, core.StringOut]] = None,
        sagemakerfeaturestoreruntime: Optional[Union[str, core.StringOut]] = None,
        sagemakerruntime: Optional[Union[str, core.StringOut]] = None,
        savingsplans: Optional[Union[str, core.StringOut]] = None,
        schemas: Optional[Union[str, core.StringOut]] = None,
        sdb: Optional[Union[str, core.StringOut]] = None,
        secretsmanager: Optional[Union[str, core.StringOut]] = None,
        securityhub: Optional[Union[str, core.StringOut]] = None,
        serverlessapplicationrepository: Optional[Union[str, core.StringOut]] = None,
        serverlessapprepo: Optional[Union[str, core.StringOut]] = None,
        serverlessrepo: Optional[Union[str, core.StringOut]] = None,
        servicecatalog: Optional[Union[str, core.StringOut]] = None,
        servicecatalogappregistry: Optional[Union[str, core.StringOut]] = None,
        servicediscovery: Optional[Union[str, core.StringOut]] = None,
        servicequotas: Optional[Union[str, core.StringOut]] = None,
        ses: Optional[Union[str, core.StringOut]] = None,
        sesv2: Optional[Union[str, core.StringOut]] = None,
        sfn: Optional[Union[str, core.StringOut]] = None,
        shield: Optional[Union[str, core.StringOut]] = None,
        signer: Optional[Union[str, core.StringOut]] = None,
        simpledb: Optional[Union[str, core.StringOut]] = None,
        sms: Optional[Union[str, core.StringOut]] = None,
        snowball: Optional[Union[str, core.StringOut]] = None,
        snowdevicemanagement: Optional[Union[str, core.StringOut]] = None,
        sns: Optional[Union[str, core.StringOut]] = None,
        sqs: Optional[Union[str, core.StringOut]] = None,
        ssm: Optional[Union[str, core.StringOut]] = None,
        ssmcontacts: Optional[Union[str, core.StringOut]] = None,
        ssmincidents: Optional[Union[str, core.StringOut]] = None,
        sso: Optional[Union[str, core.StringOut]] = None,
        ssoadmin: Optional[Union[str, core.StringOut]] = None,
        ssooidc: Optional[Union[str, core.StringOut]] = None,
        stepfunctions: Optional[Union[str, core.StringOut]] = None,
        storagegateway: Optional[Union[str, core.StringOut]] = None,
        sts: Optional[Union[str, core.StringOut]] = None,
        support: Optional[Union[str, core.StringOut]] = None,
        swf: Optional[Union[str, core.StringOut]] = None,
        synthetics: Optional[Union[str, core.StringOut]] = None,
        textract: Optional[Union[str, core.StringOut]] = None,
        timestreamquery: Optional[Union[str, core.StringOut]] = None,
        timestreamwrite: Optional[Union[str, core.StringOut]] = None,
        transcribe: Optional[Union[str, core.StringOut]] = None,
        transcribeservice: Optional[Union[str, core.StringOut]] = None,
        transcribestreaming: Optional[Union[str, core.StringOut]] = None,
        transcribestreamingservice: Optional[Union[str, core.StringOut]] = None,
        transfer: Optional[Union[str, core.StringOut]] = None,
        translate: Optional[Union[str, core.StringOut]] = None,
        voiceid: Optional[Union[str, core.StringOut]] = None,
        waf: Optional[Union[str, core.StringOut]] = None,
        wafregional: Optional[Union[str, core.StringOut]] = None,
        wafv2: Optional[Union[str, core.StringOut]] = None,
        wellarchitected: Optional[Union[str, core.StringOut]] = None,
        wisdom: Optional[Union[str, core.StringOut]] = None,
        workdocs: Optional[Union[str, core.StringOut]] = None,
        worklink: Optional[Union[str, core.StringOut]] = None,
        workmail: Optional[Union[str, core.StringOut]] = None,
        workmailmessageflow: Optional[Union[str, core.StringOut]] = None,
        workspaces: Optional[Union[str, core.StringOut]] = None,
        workspacesweb: Optional[Union[str, core.StringOut]] = None,
        xray: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Endpoints.Args(
                accessanalyzer=accessanalyzer,
                account=account,
                acm=acm,
                acmpca=acmpca,
                alexaforbusiness=alexaforbusiness,
                amg=amg,
                amp=amp,
                amplify=amplify,
                amplifybackend=amplifybackend,
                amplifyuibuilder=amplifyuibuilder,
                apigateway=apigateway,
                apigatewaymanagementapi=apigatewaymanagementapi,
                apigatewayv2=apigatewayv2,
                appautoscaling=appautoscaling,
                appconfig=appconfig,
                appconfigdata=appconfigdata,
                appflow=appflow,
                appintegrations=appintegrations,
                appintegrationsservice=appintegrationsservice,
                applicationautoscaling=applicationautoscaling,
                applicationcostprofiler=applicationcostprofiler,
                applicationdiscovery=applicationdiscovery,
                applicationdiscoveryservice=applicationdiscoveryservice,
                applicationinsights=applicationinsights,
                appmesh=appmesh,
                appregistry=appregistry,
                apprunner=apprunner,
                appstream=appstream,
                appsync=appsync,
                athena=athena,
                auditmanager=auditmanager,
                augmentedairuntime=augmentedairuntime,
                autoscaling=autoscaling,
                autoscalingplans=autoscalingplans,
                backup=backup,
                backupgateway=backupgateway,
                batch=batch,
                beanstalk=beanstalk,
                billingconductor=billingconductor,
                braket=braket,
                budgets=budgets,
                ce=ce,
                chime=chime,
                chimesdkidentity=chimesdkidentity,
                chimesdkmeetings=chimesdkmeetings,
                chimesdkmessaging=chimesdkmessaging,
                cloud9=cloud9,
                cloudcontrol=cloudcontrol,
                cloudcontrolapi=cloudcontrolapi,
                clouddirectory=clouddirectory,
                cloudformation=cloudformation,
                cloudfront=cloudfront,
                cloudhsm=cloudhsm,
                cloudhsmv2=cloudhsmv2,
                cloudsearch=cloudsearch,
                cloudsearchdomain=cloudsearchdomain,
                cloudtrail=cloudtrail,
                cloudwatch=cloudwatch,
                cloudwatchevents=cloudwatchevents,
                cloudwatchevidently=cloudwatchevidently,
                cloudwatchlog=cloudwatchlog,
                cloudwatchlogs=cloudwatchlogs,
                cloudwatchrum=cloudwatchrum,
                codeartifact=codeartifact,
                codebuild=codebuild,
                codecommit=codecommit,
                codedeploy=codedeploy,
                codeguruprofiler=codeguruprofiler,
                codegurureviewer=codegurureviewer,
                codepipeline=codepipeline,
                codestar=codestar,
                codestarconnections=codestarconnections,
                codestarnotifications=codestarnotifications,
                cognitoidentity=cognitoidentity,
                cognitoidentityprovider=cognitoidentityprovider,
                cognitoidp=cognitoidp,
                cognitosync=cognitosync,
                comprehend=comprehend,
                comprehendmedical=comprehendmedical,
                computeoptimizer=computeoptimizer,
                config=config,
                configservice=configservice,
                connect=connect,
                connectcontactlens=connectcontactlens,
                connectparticipant=connectparticipant,
                connectwisdomservice=connectwisdomservice,
                costandusagereportservice=costandusagereportservice,
                costexplorer=costexplorer,
                cur=cur,
                customerprofiles=customerprofiles,
                databasemigration=databasemigration,
                databasemigrationservice=databasemigrationservice,
                databrew=databrew,
                dataexchange=dataexchange,
                datapipeline=datapipeline,
                datasync=datasync,
                dax=dax,
                deploy=deploy,
                detective=detective,
                devicefarm=devicefarm,
                devopsguru=devopsguru,
                directconnect=directconnect,
                directoryservice=directoryservice,
                discovery=discovery,
                dlm=dlm,
                dms=dms,
                docdb=docdb,
                drs=drs,
                ds=ds,
                dynamodb=dynamodb,
                dynamodbstreams=dynamodbstreams,
                ebs=ebs,
                ec2=ec2,
                ec2instanceconnect=ec2instanceconnect,
                ecr=ecr,
                ecrpublic=ecrpublic,
                ecs=ecs,
                efs=efs,
                eks=eks,
                elasticache=elasticache,
                elasticbeanstalk=elasticbeanstalk,
                elasticinference=elasticinference,
                elasticloadbalancing=elasticloadbalancing,
                elasticloadbalancingv2=elasticloadbalancingv2,
                elasticsearch=elasticsearch,
                elasticsearchservice=elasticsearchservice,
                elastictranscoder=elastictranscoder,
                elb=elb,
                elbv2=elbv2,
                emr=emr,
                emrcontainers=emrcontainers,
                emrserverless=emrserverless,
                es=es,
                eventbridge=eventbridge,
                events=events,
                evidently=evidently,
                finspace=finspace,
                finspacedata=finspacedata,
                firehose=firehose,
                fis=fis,
                fms=fms,
                forecast=forecast,
                forecastquery=forecastquery,
                forecastqueryservice=forecastqueryservice,
                forecastservice=forecastservice,
                frauddetector=frauddetector,
                fsx=fsx,
                gamelift=gamelift,
                glacier=glacier,
                globalaccelerator=globalaccelerator,
                glue=glue,
                gluedatabrew=gluedatabrew,
                grafana=grafana,
                greengrass=greengrass,
                greengrassv2=greengrassv2,
                groundstation=groundstation,
                guardduty=guardduty,
                health=health,
                healthlake=healthlake,
                honeycode=honeycode,
                iam=iam,
                identitystore=identitystore,
                imagebuilder=imagebuilder,
                inspector=inspector,
                inspector2=inspector2,
                iot=iot,
                iot1clickdevices=iot1clickdevices,
                iot1clickdevicesservice=iot1clickdevicesservice,
                iot1clickprojects=iot1clickprojects,
                iotanalytics=iotanalytics,
                iotdata=iotdata,
                iotdataplane=iotdataplane,
                iotdeviceadvisor=iotdeviceadvisor,
                iotevents=iotevents,
                ioteventsdata=ioteventsdata,
                iotfleethub=iotfleethub,
                iotjobsdata=iotjobsdata,
                iotjobsdataplane=iotjobsdataplane,
                iotsecuretunneling=iotsecuretunneling,
                iotsitewise=iotsitewise,
                iotthingsgraph=iotthingsgraph,
                iottwinmaker=iottwinmaker,
                iotwireless=iotwireless,
                ivs=ivs,
                kafka=kafka,
                kafkaconnect=kafkaconnect,
                kendra=kendra,
                keyspaces=keyspaces,
                kinesis=kinesis,
                kinesisanalytics=kinesisanalytics,
                kinesisanalyticsv2=kinesisanalyticsv2,
                kinesisvideo=kinesisvideo,
                kinesisvideoarchivedmedia=kinesisvideoarchivedmedia,
                kinesisvideomedia=kinesisvideomedia,
                kinesisvideosignaling=kinesisvideosignaling,
                kinesisvideosignalingchannels=kinesisvideosignalingchannels,
                kms=kms,
                lakeformation=lakeformation,
                lambda_=lambda_,
                lex=lex,
                lexmodelbuilding=lexmodelbuilding,
                lexmodelbuildingservice=lexmodelbuildingservice,
                lexmodels=lexmodels,
                lexmodelsv2=lexmodelsv2,
                lexruntime=lexruntime,
                lexruntimeservice=lexruntimeservice,
                lexruntimev2=lexruntimev2,
                lexv2models=lexv2models,
                lexv2runtime=lexv2runtime,
                licensemanager=licensemanager,
                lightsail=lightsail,
                location=location,
                locationservice=locationservice,
                logs=logs,
                lookoutequipment=lookoutequipment,
                lookoutforvision=lookoutforvision,
                lookoutmetrics=lookoutmetrics,
                lookoutvision=lookoutvision,
                machinelearning=machinelearning,
                macie=macie,
                macie2=macie2,
                managedblockchain=managedblockchain,
                managedgrafana=managedgrafana,
                marketplacecatalog=marketplacecatalog,
                marketplacecommerceanalytics=marketplacecommerceanalytics,
                marketplaceentitlement=marketplaceentitlement,
                marketplaceentitlementservice=marketplaceentitlementservice,
                marketplacemetering=marketplacemetering,
                mediaconnect=mediaconnect,
                mediaconvert=mediaconvert,
                medialive=medialive,
                mediapackage=mediapackage,
                mediapackagevod=mediapackagevod,
                mediastore=mediastore,
                mediastoredata=mediastoredata,
                mediatailor=mediatailor,
                memorydb=memorydb,
                meteringmarketplace=meteringmarketplace,
                mgh=mgh,
                mgn=mgn,
                migrationhub=migrationhub,
                migrationhubconfig=migrationhubconfig,
                migrationhubrefactorspaces=migrationhubrefactorspaces,
                migrationhubstrategy=migrationhubstrategy,
                migrationhubstrategyrecommendations=migrationhubstrategyrecommendations,
                mobile=mobile,
                mq=mq,
                msk=msk,
                mturk=mturk,
                mwaa=mwaa,
                neptune=neptune,
                networkfirewall=networkfirewall,
                networkmanager=networkmanager,
                nimble=nimble,
                nimblestudio=nimblestudio,
                opensearch=opensearch,
                opensearchservice=opensearchservice,
                opsworks=opsworks,
                opsworkscm=opsworkscm,
                organizations=organizations,
                outposts=outposts,
                panorama=panorama,
                personalize=personalize,
                personalizeevents=personalizeevents,
                personalizeruntime=personalizeruntime,
                pi=pi,
                pinpoint=pinpoint,
                pinpointemail=pinpointemail,
                pinpointsmsvoice=pinpointsmsvoice,
                polly=polly,
                pricing=pricing,
                prometheus=prometheus,
                prometheusservice=prometheusservice,
                proton=proton,
                qldb=qldb,
                qldbsession=qldbsession,
                quicksight=quicksight,
                ram=ram,
                rbin=rbin,
                rds=rds,
                rdsdata=rdsdata,
                rdsdataservice=rdsdataservice,
                recyclebin=recyclebin,
                redshift=redshift,
                redshiftdata=redshiftdata,
                redshiftdataapiservice=redshiftdataapiservice,
                redshiftserverless=redshiftserverless,
                rekognition=rekognition,
                resiliencehub=resiliencehub,
                resourcegroups=resourcegroups,
                resourcegroupstagging=resourcegroupstagging,
                resourcegroupstaggingapi=resourcegroupstaggingapi,
                robomaker=robomaker,
                rolesanywhere=rolesanywhere,
                route53=route53,
                route53domains=route53domains,
                route53recoverycluster=route53recoverycluster,
                route53recoverycontrolconfig=route53recoverycontrolconfig,
                route53recoveryreadiness=route53recoveryreadiness,
                route53resolver=route53resolver,
                rum=rum,
                s3=s3,
                s3api=s3api,
                s3control=s3control,
                s3outposts=s3outposts,
                sagemaker=sagemaker,
                sagemakera2iruntime=sagemakera2iruntime,
                sagemakeredge=sagemakeredge,
                sagemakeredgemanager=sagemakeredgemanager,
                sagemakerfeaturestoreruntime=sagemakerfeaturestoreruntime,
                sagemakerruntime=sagemakerruntime,
                savingsplans=savingsplans,
                schemas=schemas,
                sdb=sdb,
                secretsmanager=secretsmanager,
                securityhub=securityhub,
                serverlessapplicationrepository=serverlessapplicationrepository,
                serverlessapprepo=serverlessapprepo,
                serverlessrepo=serverlessrepo,
                servicecatalog=servicecatalog,
                servicecatalogappregistry=servicecatalogappregistry,
                servicediscovery=servicediscovery,
                servicequotas=servicequotas,
                ses=ses,
                sesv2=sesv2,
                sfn=sfn,
                shield=shield,
                signer=signer,
                simpledb=simpledb,
                sms=sms,
                snowball=snowball,
                snowdevicemanagement=snowdevicemanagement,
                sns=sns,
                sqs=sqs,
                ssm=ssm,
                ssmcontacts=ssmcontacts,
                ssmincidents=ssmincidents,
                sso=sso,
                ssoadmin=ssoadmin,
                ssooidc=ssooidc,
                stepfunctions=stepfunctions,
                storagegateway=storagegateway,
                sts=sts,
                support=support,
                swf=swf,
                synthetics=synthetics,
                textract=textract,
                timestreamquery=timestreamquery,
                timestreamwrite=timestreamwrite,
                transcribe=transcribe,
                transcribeservice=transcribeservice,
                transcribestreaming=transcribestreaming,
                transcribestreamingservice=transcribestreamingservice,
                transfer=transfer,
                translate=translate,
                voiceid=voiceid,
                waf=waf,
                wafregional=wafregional,
                wafv2=wafv2,
                wellarchitected=wellarchitected,
                wisdom=wisdom,
                workdocs=workdocs,
                worklink=worklink,
                workmail=workmail,
                workmailmessageflow=workmailmessageflow,
                workspaces=workspaces,
                workspacesweb=workspacesweb,
                xray=xray,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accessanalyzer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        account: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        acm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        acmpca: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        alexaforbusiness: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        amg: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        amp: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        amplify: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        amplifybackend: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        amplifyuibuilder: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        apigateway: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        apigatewaymanagementapi: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        apigatewayv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appautoscaling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appconfig: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appconfigdata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appflow: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appintegrations: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appintegrationsservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        applicationautoscaling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        applicationcostprofiler: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        applicationdiscovery: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        applicationdiscoveryservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        applicationinsights: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appmesh: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appregistry: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        apprunner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appstream: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        appsync: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        athena: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auditmanager: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        augmentedairuntime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        autoscaling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        autoscalingplans: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        backup: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        backupgateway: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        batch: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        beanstalk: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        billingconductor: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        braket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        budgets: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ce: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        chime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        chimesdkidentity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        chimesdkmeetings: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        chimesdkmessaging: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloud9: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudcontrol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudcontrolapi: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        clouddirectory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudformation: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudfront: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudhsm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudhsmv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudsearch: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudsearchdomain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudtrail: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatch: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatchevents: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatchevidently: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatchlog: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatchlogs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatchrum: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codeartifact: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codebuild: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codecommit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codedeploy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codeguruprofiler: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codegurureviewer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codepipeline: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codestar: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codestarconnections: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codestarnotifications: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cognitoidentity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cognitoidentityprovider: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cognitoidp: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cognitosync: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        comprehend: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        comprehendmedical: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        computeoptimizer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        config: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        configservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connect: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connectcontactlens: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connectparticipant: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connectwisdomservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        costandusagereportservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        costexplorer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cur: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        customerprofiles: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        databasemigration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        databasemigrationservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        databrew: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dataexchange: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        datapipeline: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        datasync: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dax: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deploy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        detective: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        devicefarm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        devopsguru: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        directconnect: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        directoryservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        discovery: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dlm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dms: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        docdb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        drs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ds: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dynamodb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dynamodbstreams: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ec2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ec2instanceconnect: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ecr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ecrpublic: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ecs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        efs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        eks: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticache: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticbeanstalk: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticinference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticloadbalancing: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticloadbalancingv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticsearch: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticsearchservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elastictranscoder: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elbv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        emr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        emrcontainers: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        emrserverless: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        es: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        eventbridge: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        events: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        evidently: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        finspace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        finspacedata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        firehose: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fis: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fms: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        forecast: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        forecastquery: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        forecastqueryservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        forecastservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        frauddetector: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fsx: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gamelift: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        glacier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        globalaccelerator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        glue: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gluedatabrew: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        grafana: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        greengrass: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        greengrassv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        groundstation: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        guardduty: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        health: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        healthlake: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        honeycode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identitystore: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        imagebuilder: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        inspector: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        inspector2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iot: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iot1clickdevices: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iot1clickdevicesservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iot1clickprojects: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotanalytics: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotdata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotdataplane: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotdeviceadvisor: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotevents: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ioteventsdata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotfleethub: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotjobsdata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotjobsdataplane: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotsecuretunneling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotsitewise: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotthingsgraph: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iottwinmaker: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iotwireless: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ivs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kafka: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kafkaconnect: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kendra: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        keyspaces: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesis: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisanalytics: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisanalyticsv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisvideo: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisvideoarchivedmedia: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisvideomedia: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisvideosignaling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kinesisvideosignalingchannels: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lakeformation: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexmodelbuilding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexmodelbuildingservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexmodels: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexmodelsv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexruntime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexruntimeservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexruntimev2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexv2models: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lexv2runtime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        licensemanager: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lightsail: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        locationservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lookoutequipment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lookoutforvision: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lookoutmetrics: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lookoutvision: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        machinelearning: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        macie: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        macie2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        managedblockchain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        managedgrafana: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        marketplacecatalog: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        marketplacecommerceanalytics: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        marketplaceentitlement: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        marketplaceentitlementservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        marketplacemetering: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediaconnect: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediaconvert: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        medialive: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediapackage: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediapackagevod: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediastore: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediastoredata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mediatailor: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        memorydb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        meteringmarketplace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mgh: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mgn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        migrationhub: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        migrationhubconfig: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        migrationhubrefactorspaces: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        migrationhubstrategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        migrationhubstrategyrecommendations: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        mobile: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mq: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        msk: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mturk: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mwaa: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        neptune: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        networkfirewall: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        networkmanager: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        nimble: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        nimblestudio: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        opensearch: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        opensearchservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        opsworks: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        opsworkscm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organizations: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outposts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        panorama: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        personalize: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        personalizeevents: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        personalizeruntime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pi: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pinpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pinpointemail: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pinpointsmsvoice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        polly: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pricing: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prometheus: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prometheusservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        proton: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        qldb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        qldbsession: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        quicksight: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ram: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rbin: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rds: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rdsdata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rdsdataservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        recyclebin: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redshift: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redshiftdata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redshiftdataapiservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redshiftserverless: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rekognition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resiliencehub: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resourcegroups: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resourcegroupstagging: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resourcegroupstaggingapi: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        robomaker: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rolesanywhere: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route53: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route53domains: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route53recoverycluster: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route53recoverycontrolconfig: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route53recoveryreadiness: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route53resolver: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rum: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3api: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3control: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3outposts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemaker: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemakera2iruntime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemakeredge: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemakeredgemanager: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemakerfeaturestoreruntime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemakerruntime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        savingsplans: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schemas: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sdb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        secretsmanager: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        securityhub: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        serverlessapplicationrepository: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        serverlessapprepo: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        serverlessrepo: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        servicecatalog: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        servicecatalogappregistry: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        servicediscovery: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        servicequotas: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ses: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sesv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sfn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        shield: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        signer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        simpledb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sms: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snowball: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snowdevicemanagement: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sns: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sqs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssmcontacts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssmincidents: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sso: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssoadmin: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssooidc: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stepfunctions: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storagegateway: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        support: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        swf: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        synthetics: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        textract: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timestreamquery: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timestreamwrite: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transcribe: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transcribeservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transcribestreaming: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transcribestreamingservice: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transfer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        translate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        voiceid: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        waf: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wafregional: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wafv2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wellarchitected: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wisdom: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workdocs: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        worklink: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workmail: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workmailmessageflow: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workspaces: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workspacesweb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        xray: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class IgnoreTags(core.Schema):

    key_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=IgnoreTags.Args(
                key_prefixes=key_prefixes,
                keys=keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class AssumeRoleWithWebIdentity(core.Schema):

    duration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    web_identity_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    web_identity_token_file: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        duration: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        session_name: Optional[Union[str, core.StringOut]] = None,
        web_identity_token: Optional[Union[str, core.StringOut]] = None,
        web_identity_token_file: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AssumeRoleWithWebIdentity.Args(
                duration=duration,
                policy=policy,
                policy_arns=policy_arns,
                role_arn=role_arn,
                session_name=session_name,
                web_identity_token=web_identity_token,
                web_identity_token_file=web_identity_token_file,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        web_identity_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        web_identity_token_file: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AssumeRole(core.Schema):

    duration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    duration_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    external_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    transitive_tag_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        duration: Optional[Union[str, core.StringOut]] = None,
        duration_seconds: Optional[Union[int, core.IntOut]] = None,
        external_id: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        session_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transitive_tag_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AssumeRole.Args(
                duration=duration,
                duration_seconds=duration_seconds,
                external_id=external_id,
                policy=policy,
                policy_arns=policy_arns,
                role_arn=role_arn,
                session_name=session_name,
                tags=tags,
                transitive_tag_keys=transitive_tag_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        duration_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        external_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        transitive_tag_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.provider(name="aws")
class Provider(core.Provider):

    access_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    allowed_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    assume_role: Optional[AssumeRole] = core.attr(AssumeRole, default=None)

    assume_role_with_web_identity: Optional[AssumeRoleWithWebIdentity] = core.attr(
        AssumeRoleWithWebIdentity, default=None
    )

    custom_ca_bundle: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_tags: Optional[DefaultTags] = core.attr(DefaultTags, default=None)

    ec2_metadata_service_endpoint: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    ec2_metadata_service_endpoint_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    endpoints: Optional[Union[List[Endpoints], core.ArrayOut[Endpoints]]] = core.attr(
        Endpoints, default=None, kind=core.Kind.array
    )

    forbidden_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    http_proxy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ignore_tags: Optional[IgnoreTags] = core.attr(IgnoreTags, default=None)

    insecure: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    max_retries: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    profile: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_force_path_style: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    s3_use_path_style: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    secret_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    shared_config_files: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    shared_credentials_file: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    shared_credentials_files: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skip_credentials_validation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    skip_get_ec2_platforms: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    skip_metadata_api_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    skip_region_validation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    skip_requesting_account_id: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    sts_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    use_dualstack_endpoint: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    use_fips_endpoint: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        access_key: Optional[Union[str, core.StringOut]] = None,
        allowed_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        assume_role: Optional[AssumeRole] = None,
        assume_role_with_web_identity: Optional[AssumeRoleWithWebIdentity] = None,
        custom_ca_bundle: Optional[Union[str, core.StringOut]] = None,
        default_tags: Optional[DefaultTags] = None,
        ec2_metadata_service_endpoint: Optional[Union[str, core.StringOut]] = None,
        ec2_metadata_service_endpoint_mode: Optional[Union[str, core.StringOut]] = None,
        endpoints: Optional[Union[List[Endpoints], core.ArrayOut[Endpoints]]] = None,
        forbidden_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        http_proxy: Optional[Union[str, core.StringOut]] = None,
        ignore_tags: Optional[IgnoreTags] = None,
        insecure: Optional[Union[bool, core.BoolOut]] = None,
        max_retries: Optional[Union[int, core.IntOut]] = None,
        profile: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        s3_force_path_style: Optional[Union[bool, core.BoolOut]] = None,
        s3_use_path_style: Optional[Union[bool, core.BoolOut]] = None,
        secret_key: Optional[Union[str, core.StringOut]] = None,
        shared_config_files: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        shared_credentials_file: Optional[Union[str, core.StringOut]] = None,
        shared_credentials_files: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        skip_credentials_validation: Optional[Union[bool, core.BoolOut]] = None,
        skip_get_ec2_platforms: Optional[Union[bool, core.BoolOut]] = None,
        skip_metadata_api_check: Optional[Union[str, core.StringOut]] = None,
        skip_region_validation: Optional[Union[bool, core.BoolOut]] = None,
        skip_requesting_account_id: Optional[Union[bool, core.BoolOut]] = None,
        sts_region: Optional[Union[str, core.StringOut]] = None,
        token: Optional[Union[str, core.StringOut]] = None,
        use_dualstack_endpoint: Optional[Union[bool, core.BoolOut]] = None,
        use_fips_endpoint: Optional[Union[bool, core.BoolOut]] = None,
        alias: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Provider.Args(
                access_key=access_key,
                allowed_account_ids=allowed_account_ids,
                assume_role=assume_role,
                assume_role_with_web_identity=assume_role_with_web_identity,
                custom_ca_bundle=custom_ca_bundle,
                default_tags=default_tags,
                ec2_metadata_service_endpoint=ec2_metadata_service_endpoint,
                ec2_metadata_service_endpoint_mode=ec2_metadata_service_endpoint_mode,
                endpoints=endpoints,
                forbidden_account_ids=forbidden_account_ids,
                http_proxy=http_proxy,
                ignore_tags=ignore_tags,
                insecure=insecure,
                max_retries=max_retries,
                profile=profile,
                region=region,
                s3_force_path_style=s3_force_path_style,
                s3_use_path_style=s3_use_path_style,
                secret_key=secret_key,
                shared_config_files=shared_config_files,
                shared_credentials_file=shared_credentials_file,
                shared_credentials_files=shared_credentials_files,
                skip_credentials_validation=skip_credentials_validation,
                skip_get_ec2_platforms=skip_get_ec2_platforms,
                skip_metadata_api_check=skip_metadata_api_check,
                skip_region_validation=skip_region_validation,
                skip_requesting_account_id=skip_requesting_account_id,
                sts_region=sts_region,
                token=token,
                use_dualstack_endpoint=use_dualstack_endpoint,
                use_fips_endpoint=use_fips_endpoint,
                alias=alias,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.Provider.Args):
        access_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        allowed_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        assume_role: Optional[AssumeRole] = core.arg(default=None)

        assume_role_with_web_identity: Optional[AssumeRoleWithWebIdentity] = core.arg(default=None)

        custom_ca_bundle: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_tags: Optional[DefaultTags] = core.arg(default=None)

        ec2_metadata_service_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ec2_metadata_service_endpoint_mode: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        endpoints: Optional[Union[List[Endpoints], core.ArrayOut[Endpoints]]] = core.arg(
            default=None
        )

        forbidden_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        http_proxy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ignore_tags: Optional[IgnoreTags] = core.arg(default=None)

        insecure: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_retries: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        profile: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_force_path_style: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        s3_use_path_style: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        secret_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        shared_config_files: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        shared_credentials_file: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        shared_credentials_files: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        skip_credentials_validation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        skip_get_ec2_platforms: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        skip_metadata_api_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        skip_region_validation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        skip_requesting_account_id: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sts_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        use_dualstack_endpoint: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        use_fips_endpoint: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
