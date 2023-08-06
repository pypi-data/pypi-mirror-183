import os
import unittest.mock

from exchangelib import Identity, Configuration
from python.configuration.config import create_account, create_accounts, create_credentials, create_config, CredentialsError


class TestValidConfig(unittest.TestCase):
    email = 'baier@orcacapital.de'
    real_server_requests: bool = False if os.environ.get("CLIENT_ID") == 'XXX' else True

    @classmethod
    def setUp(cls) -> None:
        os.environ["CLIENT_ID"] = 'XXX'
        os.environ["CLIENT_SECRET"] = 'XXX'
        os.environ["TENANT_ID"] = 'XXX'

    def test_invalid_create_credentials(self):
        with self.assertRaises(CredentialsError) as err:
            create_credentials(self.email)
        self.assertEqual(
            err.exception.args[0],
            'Invalid configuration for "client_id", "client_secret" or "tenant_id" in [.env]-file.'
        )

    def test_invalid_create_account(self):
        if not self.real_server_requests:
            with self.assertRaises(CredentialsError):
                create_account(self.email)

    def test_invalid_create_accounts(self):
        if not self.real_server_requests:
            with self.assertRaises(CredentialsError):
                create_accounts()

    def test_primary_email_ends_with_orcacapital(self):
        with self.assertRaises(ValueError) as err:
            create_account('test@google.com')
        self.assertEqual(
            err.exception.args[0],
            'Provided user email was [test@google.com] but the suffix should be "@orcacapital.de"'
        )

    def test_invalid_create_config(self):
        with self.assertRaises(CredentialsError) as err:
            create_config(create_credentials(self.email))
        self.assertEqual(
            err.exception.args[0],
            'Invalid configuration for "client_id", "client_secret" or "tenant_id" in [.env]-file.'
        )

    def test_x_valid_create_config(self):
        os.environ["CLIENT_ID"] = 'XX'
        os.environ["CLIENT_SECRET"] = 'XX'
        os.environ["TENANT_ID"] = 'XX'
        creds = create_credentials(self.email)
        config = create_config(creds)
        self.assertEqual(type(config), Configuration)

    def test_y_valid_create_credentials(self):
        self.real_server_requests = True
        os.environ["CLIENT_ID"] = 'XX'
        os.environ["CLIENT_SECRET"] = 'XX'
        os.environ["TENANT_ID"] = 'XX'

        creds = create_credentials(self.email)
        self.assertEqual(creds.client_id, 'XX')
        self.assertEqual(creds.client_secret, 'XX')
        self.assertEqual(creds.tenant_id, 'XX')
        self.assertEqual(creds.identity, Identity(primary_smtp_address=self.email))

    def test_z_valid_create_accounts(self):
        self.real_server_requests = True
        os.environ["CLIENT_ID"] = 'your_client_id_here'
        os.environ["CLIENT_SECRET"] = 'your_client_secret_here'
        os.environ["TENANT_ID"] = 'your_tenant_id_here'
        with self.assertRaises(CredentialsError) as err:
            create_accounts()

    def test_z_valid_create_account(self):
        self.real_server_requests = True
        os.environ["CLIENT_ID"] = 'your_client_id_here'
        os.environ["CLIENT_SECRET"] = 'your_client_secret_here'
        os.environ["TENANT_ID"] = 'your_tenant_id_here'
        with self.assertRaises(CredentialsError) as err:
            create_account(self.email)
