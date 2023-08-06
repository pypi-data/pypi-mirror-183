from exchangelib import Message, Mailbox, FileAttachment, Account
from exchangelib.properties import HTMLBody


def send_email(account: Account, subject: str, body: str, recipients: list[str], attachments=None):
    to_recipients = [Mailbox(email_address=recipient) for recipient in recipients]

    m = Message(account=account,
                folder=account.sent,
                subject=subject,
                body=HTMLBody(body),
                to_recipients=to_recipients)

    if attachments:
        for attachment_name, attachment_content in attachments:
            file = FileAttachment(name=attachment_name, content=attachment_content)
            m.attach(file)

    m.send_and_save()
