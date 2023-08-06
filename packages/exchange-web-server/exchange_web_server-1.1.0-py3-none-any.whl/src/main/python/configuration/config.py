import os

from exchangelib import Account, Configuration, OAuth2Credentials, OAUTH2, FaultTolerance, Identity, DELEGATE
from dotenv import load_dotenv
from oauthlib.oauth2 import InvalidClientIdError

load_dotenv()


class CredentialsError(Exception):
    def __init__(self):
        fail_msg = 'Invalid configuration for "client_id", "client_secret" or "tenant_id" in [.env]-file.'
        super(CredentialsError, self).__init__(fail_msg)


def create_credentials(primary_smtp_address: str) -> OAuth2Credentials:
    """Helper method to create an Account associated with our company."""

    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    tenant_id = os.environ.get("TENANT_ID")

    if client_id == 'XXX' or client_secret == 'XXX' or tenant_id == 'XXX':
        raise CredentialsError

    return OAuth2Credentials(
        client_id=client_id,
        client_secret=client_secret,
        tenant_id=tenant_id,
        identity=Identity(primary_smtp_address=primary_smtp_address)
    )


def create_config(credentials: OAuth2Credentials) -> Configuration:
    return Configuration(
        service_endpoint='https://outlook.office365.com/EWS/Exchange.asmx',
        credentials=credentials,
        auth_type=OAUTH2,
        retry_policy=FaultTolerance(max_wait=3600)
    )


def create_account(primary_smtp_address: str) -> Account:
    # Sanity-Check if emails endswith @orcacapital.de
    if not primary_smtp_address.endswith('@orcacapital.de'):
        raise ValueError(f'Provided user email was [{primary_smtp_address}] but the suffix should be "@orcacapital.de"')

    credentials = create_credentials(primary_smtp_address=primary_smtp_address)
    config = create_config(credentials)

    try:
        return Account(
            primary_smtp_address=primary_smtp_address,
            config=config,
            autodiscover=False,
            access_type=DELEGATE
        )
    except InvalidClientIdError:
        raise CredentialsError


def create_accounts() -> dict[str, Account]:
    """
    Creating a dict consisting of str and exchangelib.Account

    Account can be accessed through first name of employee.
    """

    suffix = '@orcacapital.de'

    usernames: list[str] = [
        'kreutmair',
        'baier',
        'beck',
        'lenski',
        'buchhaltung'
    ]

    return {user: create_account(f'{user}{suffix}') for user in usernames}

