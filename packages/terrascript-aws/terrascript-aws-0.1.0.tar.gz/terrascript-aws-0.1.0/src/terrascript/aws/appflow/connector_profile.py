from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ConnectorProfileCredentialsSingular(core.Schema):

    api_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        api_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSingular.Args(
                api_key=api_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: Union[str, core.StringOut] = core.arg()


@core.schema
class OauthRequest(core.Schema):

    auth_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redirect_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auth_code: Optional[Union[str, core.StringOut]] = None,
        redirect_uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OauthRequest.Args(
                auth_code=auth_code,
                redirect_uri=redirect_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redirect_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsSlack(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        access_token: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSlack.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        oauth_request: Optional[OauthRequest] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsAmplitude(core.Schema):

    api_key: Union[str, core.StringOut] = core.attr(str)

    secret_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        api_key: Union[str, core.StringOut],
        secret_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsAmplitude.Args(
                api_key=api_key,
                secret_key=secret_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: Union[str, core.StringOut] = core.arg()

        secret_key: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentialsDatadog(core.Schema):

    api_key: Union[str, core.StringOut] = core.attr(str)

    application_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        api_key: Union[str, core.StringOut],
        application_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsDatadog.Args(
                api_key=api_key,
                application_key=application_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: Union[str, core.StringOut] = core.arg()

        application_key: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentialsSnowflake(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSnowflake.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentialsHoneycode(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    refresh_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
        refresh_token: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsHoneycode.Args(
                access_token=access_token,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        oauth_request: Optional[OauthRequest] = core.arg(default=None)

        refresh_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsDynatrace(core.Schema):

    api_token: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        api_token: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsDynatrace.Args(
                api_token=api_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_token: Union[str, core.StringOut] = core.arg()


@core.schema
class BasicAuthCredentials(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=BasicAuthCredentials.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class OauthCredentials(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    refresh_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        access_token: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
        refresh_token: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OauthCredentials.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        oauth_request: Optional[OauthRequest] = core.arg(default=None)

        refresh_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsSapoData(core.Schema):

    basic_auth_credentials: Optional[BasicAuthCredentials] = core.attr(
        BasicAuthCredentials, default=None
    )

    oauth_credentials: Optional[OauthCredentials] = core.attr(OauthCredentials, default=None)

    def __init__(
        self,
        *,
        basic_auth_credentials: Optional[BasicAuthCredentials] = None,
        oauth_credentials: Optional[OauthCredentials] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSapoData.Args(
                basic_auth_credentials=basic_auth_credentials,
                oauth_credentials=oauth_credentials,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        basic_auth_credentials: Optional[BasicAuthCredentials] = core.arg(default=None)

        oauth_credentials: Optional[OauthCredentials] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsZendesk(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        access_token: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsZendesk.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        oauth_request: Optional[OauthRequest] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsGoogleAnalytics(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    refresh_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        access_token: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
        refresh_token: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsGoogleAnalytics.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        oauth_request: Optional[OauthRequest] = core.arg(default=None)

        refresh_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsRedshift(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsRedshift.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentialsMarketo(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        access_token: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsMarketo.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        oauth_request: Optional[OauthRequest] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsTrendmicro(core.Schema):

    api_secret_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        api_secret_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsTrendmicro.Args(
                api_secret_key=api_secret_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_secret_key: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentialsSalesforce(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_credentials_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    refresh_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: Optional[Union[str, core.StringOut]] = None,
        client_credentials_arn: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
        refresh_token: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSalesforce.Args(
                access_token=access_token,
                client_credentials_arn=client_credentials_arn,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_credentials_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        oauth_request: Optional[OauthRequest] = core.arg(default=None)

        refresh_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsInforNexus(core.Schema):

    access_key_id: Union[str, core.StringOut] = core.attr(str)

    datakey: Union[str, core.StringOut] = core.attr(str)

    secret_access_key: Union[str, core.StringOut] = core.attr(str)

    user_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        access_key_id: Union[str, core.StringOut],
        datakey: Union[str, core.StringOut],
        secret_access_key: Union[str, core.StringOut],
        user_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsInforNexus.Args(
                access_key_id=access_key_id,
                datakey=datakey,
                secret_access_key=secret_access_key,
                user_id=user_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_key_id: Union[str, core.StringOut] = core.arg()

        datakey: Union[str, core.StringOut] = core.arg()

        secret_access_key: Union[str, core.StringOut] = core.arg()

        user_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Basic(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Basic.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class Custom(core.Schema):

    credentials_map: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    custom_authentication_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        custom_authentication_type: Union[str, core.StringOut],
        credentials_map: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Custom.Args(
                custom_authentication_type=custom_authentication_type,
                credentials_map=credentials_map,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials_map: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        custom_authentication_type: Union[str, core.StringOut] = core.arg()


@core.schema
class Oauth2(core.Schema):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_secret: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    oauth_request: Optional[OauthRequest] = core.attr(OauthRequest, default=None)

    refresh_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: Optional[Union[str, core.StringOut]] = None,
        client_id: Optional[Union[str, core.StringOut]] = None,
        client_secret: Optional[Union[str, core.StringOut]] = None,
        oauth_request: Optional[OauthRequest] = None,
        refresh_token: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Oauth2.Args(
                access_token=access_token,
                client_id=client_id,
                client_secret=client_secret,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_secret: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        oauth_request: Optional[OauthRequest] = core.arg(default=None)

        refresh_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ApiKey(core.Schema):

    api_key: Union[str, core.StringOut] = core.attr(str)

    api_secret_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        api_key: Union[str, core.StringOut],
        api_secret_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ApiKey.Args(
                api_key=api_key,
                api_secret_key=api_secret_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: Union[str, core.StringOut] = core.arg()

        api_secret_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsCustomConnector(core.Schema):

    api_key: Optional[ApiKey] = core.attr(ApiKey, default=None)

    authentication_type: Union[str, core.StringOut] = core.attr(str)

    basic: Optional[Basic] = core.attr(Basic, default=None)

    custom: Optional[Custom] = core.attr(Custom, default=None)

    oauth2: Optional[Oauth2] = core.attr(Oauth2, default=None)

    def __init__(
        self,
        *,
        authentication_type: Union[str, core.StringOut],
        api_key: Optional[ApiKey] = None,
        basic: Optional[Basic] = None,
        custom: Optional[Custom] = None,
        oauth2: Optional[Oauth2] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsCustomConnector.Args(
                authentication_type=authentication_type,
                api_key=api_key,
                basic=basic,
                custom=custom,
                oauth2=oauth2,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: Optional[ApiKey] = core.arg(default=None)

        authentication_type: Union[str, core.StringOut] = core.arg()

        basic: Optional[Basic] = core.arg(default=None)

        custom: Optional[Custom] = core.arg(default=None)

        oauth2: Optional[Oauth2] = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsVeeva(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsVeeva.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentialsServiceNow(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfileCredentialsServiceNow.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfileCredentials(core.Schema):

    amplitude: Optional[ConnectorProfileCredentialsAmplitude] = core.attr(
        ConnectorProfileCredentialsAmplitude, default=None
    )

    custom_connector: Optional[ConnectorProfileCredentialsCustomConnector] = core.attr(
        ConnectorProfileCredentialsCustomConnector, default=None
    )

    datadog: Optional[ConnectorProfileCredentialsDatadog] = core.attr(
        ConnectorProfileCredentialsDatadog, default=None
    )

    dynatrace: Optional[ConnectorProfileCredentialsDynatrace] = core.attr(
        ConnectorProfileCredentialsDynatrace, default=None
    )

    google_analytics: Optional[ConnectorProfileCredentialsGoogleAnalytics] = core.attr(
        ConnectorProfileCredentialsGoogleAnalytics, default=None
    )

    honeycode: Optional[ConnectorProfileCredentialsHoneycode] = core.attr(
        ConnectorProfileCredentialsHoneycode, default=None
    )

    infor_nexus: Optional[ConnectorProfileCredentialsInforNexus] = core.attr(
        ConnectorProfileCredentialsInforNexus, default=None
    )

    marketo: Optional[ConnectorProfileCredentialsMarketo] = core.attr(
        ConnectorProfileCredentialsMarketo, default=None
    )

    redshift: Optional[ConnectorProfileCredentialsRedshift] = core.attr(
        ConnectorProfileCredentialsRedshift, default=None
    )

    salesforce: Optional[ConnectorProfileCredentialsSalesforce] = core.attr(
        ConnectorProfileCredentialsSalesforce, default=None
    )

    sapo_data: Optional[ConnectorProfileCredentialsSapoData] = core.attr(
        ConnectorProfileCredentialsSapoData, default=None
    )

    service_now: Optional[ConnectorProfileCredentialsServiceNow] = core.attr(
        ConnectorProfileCredentialsServiceNow, default=None
    )

    singular: Optional[ConnectorProfileCredentialsSingular] = core.attr(
        ConnectorProfileCredentialsSingular, default=None
    )

    slack: Optional[ConnectorProfileCredentialsSlack] = core.attr(
        ConnectorProfileCredentialsSlack, default=None
    )

    snowflake: Optional[ConnectorProfileCredentialsSnowflake] = core.attr(
        ConnectorProfileCredentialsSnowflake, default=None
    )

    trendmicro: Optional[ConnectorProfileCredentialsTrendmicro] = core.attr(
        ConnectorProfileCredentialsTrendmicro, default=None
    )

    veeva: Optional[ConnectorProfileCredentialsVeeva] = core.attr(
        ConnectorProfileCredentialsVeeva, default=None
    )

    zendesk: Optional[ConnectorProfileCredentialsZendesk] = core.attr(
        ConnectorProfileCredentialsZendesk, default=None
    )

    def __init__(
        self,
        *,
        amplitude: Optional[ConnectorProfileCredentialsAmplitude] = None,
        custom_connector: Optional[ConnectorProfileCredentialsCustomConnector] = None,
        datadog: Optional[ConnectorProfileCredentialsDatadog] = None,
        dynatrace: Optional[ConnectorProfileCredentialsDynatrace] = None,
        google_analytics: Optional[ConnectorProfileCredentialsGoogleAnalytics] = None,
        honeycode: Optional[ConnectorProfileCredentialsHoneycode] = None,
        infor_nexus: Optional[ConnectorProfileCredentialsInforNexus] = None,
        marketo: Optional[ConnectorProfileCredentialsMarketo] = None,
        redshift: Optional[ConnectorProfileCredentialsRedshift] = None,
        salesforce: Optional[ConnectorProfileCredentialsSalesforce] = None,
        sapo_data: Optional[ConnectorProfileCredentialsSapoData] = None,
        service_now: Optional[ConnectorProfileCredentialsServiceNow] = None,
        singular: Optional[ConnectorProfileCredentialsSingular] = None,
        slack: Optional[ConnectorProfileCredentialsSlack] = None,
        snowflake: Optional[ConnectorProfileCredentialsSnowflake] = None,
        trendmicro: Optional[ConnectorProfileCredentialsTrendmicro] = None,
        veeva: Optional[ConnectorProfileCredentialsVeeva] = None,
        zendesk: Optional[ConnectorProfileCredentialsZendesk] = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentials.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                honeycode=honeycode,
                infor_nexus=infor_nexus,
                marketo=marketo,
                redshift=redshift,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                snowflake=snowflake,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: Optional[ConnectorProfileCredentialsAmplitude] = core.arg(default=None)

        custom_connector: Optional[ConnectorProfileCredentialsCustomConnector] = core.arg(
            default=None
        )

        datadog: Optional[ConnectorProfileCredentialsDatadog] = core.arg(default=None)

        dynatrace: Optional[ConnectorProfileCredentialsDynatrace] = core.arg(default=None)

        google_analytics: Optional[ConnectorProfileCredentialsGoogleAnalytics] = core.arg(
            default=None
        )

        honeycode: Optional[ConnectorProfileCredentialsHoneycode] = core.arg(default=None)

        infor_nexus: Optional[ConnectorProfileCredentialsInforNexus] = core.arg(default=None)

        marketo: Optional[ConnectorProfileCredentialsMarketo] = core.arg(default=None)

        redshift: Optional[ConnectorProfileCredentialsRedshift] = core.arg(default=None)

        salesforce: Optional[ConnectorProfileCredentialsSalesforce] = core.arg(default=None)

        sapo_data: Optional[ConnectorProfileCredentialsSapoData] = core.arg(default=None)

        service_now: Optional[ConnectorProfileCredentialsServiceNow] = core.arg(default=None)

        singular: Optional[ConnectorProfileCredentialsSingular] = core.arg(default=None)

        slack: Optional[ConnectorProfileCredentialsSlack] = core.arg(default=None)

        snowflake: Optional[ConnectorProfileCredentialsSnowflake] = core.arg(default=None)

        trendmicro: Optional[ConnectorProfileCredentialsTrendmicro] = core.arg(default=None)

        veeva: Optional[ConnectorProfileCredentialsVeeva] = core.arg(default=None)

        zendesk: Optional[ConnectorProfileCredentialsZendesk] = core.arg(default=None)


@core.schema
class ConnectorProfilePropertiesSlack(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSlack.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesDynatrace(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesDynatrace.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesVeeva(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesVeeva.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesHoneycode(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfilePropertiesInforNexus(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesInforNexus.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesZendesk(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesZendesk.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesSalesforce(core.Schema):

    instance_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    is_sandbox_environment: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        instance_url: Optional[Union[str, core.StringOut]] = None,
        is_sandbox_environment: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSalesforce.Args(
                instance_url=instance_url,
                is_sandbox_environment=is_sandbox_environment,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        is_sandbox_environment: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class ConnectorProfilePropertiesTrendmicro(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfilePropertiesMarketo(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesMarketo.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class OauthProperties(core.Schema):

    auth_code_url: Union[str, core.StringOut] = core.attr(str)

    oauth_scopes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    token_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        auth_code_url: Union[str, core.StringOut],
        oauth_scopes: Union[List[str], core.ArrayOut[core.StringOut]],
        token_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OauthProperties.Args(
                auth_code_url=auth_code_url,
                oauth_scopes=oauth_scopes,
                token_url=token_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_code_url: Union[str, core.StringOut] = core.arg()

        oauth_scopes: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        token_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesSapoData(core.Schema):

    application_host_url: Union[str, core.StringOut] = core.attr(str)

    application_service_path: Union[str, core.StringOut] = core.attr(str)

    client_number: Union[str, core.StringOut] = core.attr(str)

    logon_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    oauth_properties: Optional[OauthProperties] = core.attr(OauthProperties, default=None)

    port_number: Union[int, core.IntOut] = core.attr(int)

    private_link_service_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        application_host_url: Union[str, core.StringOut],
        application_service_path: Union[str, core.StringOut],
        client_number: Union[str, core.StringOut],
        port_number: Union[int, core.IntOut],
        logon_language: Optional[Union[str, core.StringOut]] = None,
        oauth_properties: Optional[OauthProperties] = None,
        private_link_service_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSapoData.Args(
                application_host_url=application_host_url,
                application_service_path=application_service_path,
                client_number=client_number,
                port_number=port_number,
                logon_language=logon_language,
                oauth_properties=oauth_properties,
                private_link_service_name=private_link_service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_host_url: Union[str, core.StringOut] = core.arg()

        application_service_path: Union[str, core.StringOut] = core.arg()

        client_number: Union[str, core.StringOut] = core.arg()

        logon_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        oauth_properties: Optional[OauthProperties] = core.arg(default=None)

        port_number: Union[int, core.IntOut] = core.arg()

        private_link_service_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectorProfilePropertiesDatadog(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesDatadog.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesGoogleAnalytics(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfilePropertiesRedshift(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    database_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        database_url: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesRedshift.Args(
                bucket_name=bucket_name,
                role_arn=role_arn,
                bucket_prefix=bucket_prefix,
                database_url=database_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesSnowflake(core.Schema):

    account_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    private_link_service_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stage: Union[str, core.StringOut] = core.attr(str)

    warehouse: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        stage: Union[str, core.StringOut],
        warehouse: Union[str, core.StringOut],
        account_name: Optional[Union[str, core.StringOut]] = None,
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        private_link_service_name: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSnowflake.Args(
                bucket_name=bucket_name,
                stage=stage,
                warehouse=warehouse,
                account_name=account_name,
                bucket_prefix=bucket_prefix,
                private_link_service_name=private_link_service_name,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_link_service_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stage: Union[str, core.StringOut] = core.arg()

        warehouse: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesAmplitude(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class Oauth2Properties(core.Schema):

    oauth2_grant_type: Union[str, core.StringOut] = core.attr(str)

    token_url: Union[str, core.StringOut] = core.attr(str)

    token_url_custom_properties: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    def __init__(
        self,
        *,
        oauth2_grant_type: Union[str, core.StringOut],
        token_url: Union[str, core.StringOut],
        token_url_custom_properties: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
    ):
        super().__init__(
            args=Oauth2Properties.Args(
                oauth2_grant_type=oauth2_grant_type,
                token_url=token_url,
                token_url_custom_properties=token_url_custom_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        oauth2_grant_type: Union[str, core.StringOut] = core.arg()

        token_url: Union[str, core.StringOut] = core.arg()

        token_url_custom_properties: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class ConnectorProfilePropertiesCustomConnector(core.Schema):

    oauth2_properties: Optional[Oauth2Properties] = core.attr(Oauth2Properties, default=None)

    profile_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        oauth2_properties: Optional[Oauth2Properties] = None,
        profile_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesCustomConnector.Args(
                oauth2_properties=oauth2_properties,
                profile_properties=profile_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        oauth2_properties: Optional[Oauth2Properties] = core.arg(default=None)

        profile_properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class ConnectorProfilePropertiesServiceNow(core.Schema):

    instance_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectorProfilePropertiesServiceNow.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectorProfilePropertiesSingular(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfileProperties(core.Schema):

    amplitude: Optional[ConnectorProfilePropertiesAmplitude] = core.attr(
        ConnectorProfilePropertiesAmplitude, default=None
    )

    custom_connector: Optional[ConnectorProfilePropertiesCustomConnector] = core.attr(
        ConnectorProfilePropertiesCustomConnector, default=None
    )

    datadog: Optional[ConnectorProfilePropertiesDatadog] = core.attr(
        ConnectorProfilePropertiesDatadog, default=None
    )

    dynatrace: Optional[ConnectorProfilePropertiesDynatrace] = core.attr(
        ConnectorProfilePropertiesDynatrace, default=None
    )

    google_analytics: Optional[ConnectorProfilePropertiesGoogleAnalytics] = core.attr(
        ConnectorProfilePropertiesGoogleAnalytics, default=None
    )

    honeycode: Optional[ConnectorProfilePropertiesHoneycode] = core.attr(
        ConnectorProfilePropertiesHoneycode, default=None
    )

    infor_nexus: Optional[ConnectorProfilePropertiesInforNexus] = core.attr(
        ConnectorProfilePropertiesInforNexus, default=None
    )

    marketo: Optional[ConnectorProfilePropertiesMarketo] = core.attr(
        ConnectorProfilePropertiesMarketo, default=None
    )

    redshift: Optional[ConnectorProfilePropertiesRedshift] = core.attr(
        ConnectorProfilePropertiesRedshift, default=None
    )

    salesforce: Optional[ConnectorProfilePropertiesSalesforce] = core.attr(
        ConnectorProfilePropertiesSalesforce, default=None
    )

    sapo_data: Optional[ConnectorProfilePropertiesSapoData] = core.attr(
        ConnectorProfilePropertiesSapoData, default=None
    )

    service_now: Optional[ConnectorProfilePropertiesServiceNow] = core.attr(
        ConnectorProfilePropertiesServiceNow, default=None
    )

    singular: Optional[ConnectorProfilePropertiesSingular] = core.attr(
        ConnectorProfilePropertiesSingular, default=None
    )

    slack: Optional[ConnectorProfilePropertiesSlack] = core.attr(
        ConnectorProfilePropertiesSlack, default=None
    )

    snowflake: Optional[ConnectorProfilePropertiesSnowflake] = core.attr(
        ConnectorProfilePropertiesSnowflake, default=None
    )

    trendmicro: Optional[ConnectorProfilePropertiesTrendmicro] = core.attr(
        ConnectorProfilePropertiesTrendmicro, default=None
    )

    veeva: Optional[ConnectorProfilePropertiesVeeva] = core.attr(
        ConnectorProfilePropertiesVeeva, default=None
    )

    zendesk: Optional[ConnectorProfilePropertiesZendesk] = core.attr(
        ConnectorProfilePropertiesZendesk, default=None
    )

    def __init__(
        self,
        *,
        amplitude: Optional[ConnectorProfilePropertiesAmplitude] = None,
        custom_connector: Optional[ConnectorProfilePropertiesCustomConnector] = None,
        datadog: Optional[ConnectorProfilePropertiesDatadog] = None,
        dynatrace: Optional[ConnectorProfilePropertiesDynatrace] = None,
        google_analytics: Optional[ConnectorProfilePropertiesGoogleAnalytics] = None,
        honeycode: Optional[ConnectorProfilePropertiesHoneycode] = None,
        infor_nexus: Optional[ConnectorProfilePropertiesInforNexus] = None,
        marketo: Optional[ConnectorProfilePropertiesMarketo] = None,
        redshift: Optional[ConnectorProfilePropertiesRedshift] = None,
        salesforce: Optional[ConnectorProfilePropertiesSalesforce] = None,
        sapo_data: Optional[ConnectorProfilePropertiesSapoData] = None,
        service_now: Optional[ConnectorProfilePropertiesServiceNow] = None,
        singular: Optional[ConnectorProfilePropertiesSingular] = None,
        slack: Optional[ConnectorProfilePropertiesSlack] = None,
        snowflake: Optional[ConnectorProfilePropertiesSnowflake] = None,
        trendmicro: Optional[ConnectorProfilePropertiesTrendmicro] = None,
        veeva: Optional[ConnectorProfilePropertiesVeeva] = None,
        zendesk: Optional[ConnectorProfilePropertiesZendesk] = None,
    ):
        super().__init__(
            args=ConnectorProfileProperties.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                honeycode=honeycode,
                infor_nexus=infor_nexus,
                marketo=marketo,
                redshift=redshift,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                snowflake=snowflake,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: Optional[ConnectorProfilePropertiesAmplitude] = core.arg(default=None)

        custom_connector: Optional[ConnectorProfilePropertiesCustomConnector] = core.arg(
            default=None
        )

        datadog: Optional[ConnectorProfilePropertiesDatadog] = core.arg(default=None)

        dynatrace: Optional[ConnectorProfilePropertiesDynatrace] = core.arg(default=None)

        google_analytics: Optional[ConnectorProfilePropertiesGoogleAnalytics] = core.arg(
            default=None
        )

        honeycode: Optional[ConnectorProfilePropertiesHoneycode] = core.arg(default=None)

        infor_nexus: Optional[ConnectorProfilePropertiesInforNexus] = core.arg(default=None)

        marketo: Optional[ConnectorProfilePropertiesMarketo] = core.arg(default=None)

        redshift: Optional[ConnectorProfilePropertiesRedshift] = core.arg(default=None)

        salesforce: Optional[ConnectorProfilePropertiesSalesforce] = core.arg(default=None)

        sapo_data: Optional[ConnectorProfilePropertiesSapoData] = core.arg(default=None)

        service_now: Optional[ConnectorProfilePropertiesServiceNow] = core.arg(default=None)

        singular: Optional[ConnectorProfilePropertiesSingular] = core.arg(default=None)

        slack: Optional[ConnectorProfilePropertiesSlack] = core.arg(default=None)

        snowflake: Optional[ConnectorProfilePropertiesSnowflake] = core.arg(default=None)

        trendmicro: Optional[ConnectorProfilePropertiesTrendmicro] = core.arg(default=None)

        veeva: Optional[ConnectorProfilePropertiesVeeva] = core.arg(default=None)

        zendesk: Optional[ConnectorProfilePropertiesZendesk] = core.arg(default=None)


@core.schema
class ConnectorProfileConfig(core.Schema):

    connector_profile_credentials: ConnectorProfileCredentials = core.attr(
        ConnectorProfileCredentials
    )

    connector_profile_properties: ConnectorProfileProperties = core.attr(ConnectorProfileProperties)

    def __init__(
        self,
        *,
        connector_profile_credentials: ConnectorProfileCredentials,
        connector_profile_properties: ConnectorProfileProperties,
    ):
        super().__init__(
            args=ConnectorProfileConfig.Args(
                connector_profile_credentials=connector_profile_credentials,
                connector_profile_properties=connector_profile_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connector_profile_credentials: ConnectorProfileCredentials = core.arg()

        connector_profile_properties: ConnectorProfileProperties = core.arg()


@core.resource(type="aws_appflow_connector_profile", namespace="aws_appflow")
class ConnectorProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_mode: Union[str, core.StringOut] = core.attr(str)

    connector_label: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connector_profile_config: ConnectorProfileConfig = core.attr(ConnectorProfileConfig)

    connector_type: Union[str, core.StringOut] = core.attr(str)

    credentials_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_mode: Union[str, core.StringOut],
        connector_profile_config: ConnectorProfileConfig,
        connector_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        connector_label: Optional[Union[str, core.StringOut]] = None,
        kms_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConnectorProfile.Args(
                connection_mode=connection_mode,
                connector_profile_config=connector_profile_config,
                connector_type=connector_type,
                name=name,
                connector_label=connector_label,
                kms_arn=kms_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_mode: Union[str, core.StringOut] = core.arg()

        connector_label: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connector_profile_config: ConnectorProfileConfig = core.arg()

        connector_type: Union[str, core.StringOut] = core.arg()

        kms_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
