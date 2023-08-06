from python.configuration.config import create_account
from python.logs.date_time import CurrentDate


def save_attachment_steubing_reports(exchange_folder_name: str, account_var, lastitems):
    from exchangelib import FileAttachment
    import os.path
    current_date = CurrentDate()
    this_month_path = os.path.join(rf'O:\Steubing\{current_date.yesterday.year}\{current_date.current_month}')
    frankfurt_path = os.path.join(this_month_path, 'Frankfurt')
    tradegate_path = os.path.join(this_month_path, 'Tradegate')
    xitaro_path = os.path.join(this_month_path, 'Xitaro')

    for exchange_path in [this_month_path, frankfurt_path, tradegate_path, xitaro_path]:
        if not os.path.isdir(exchange_path):
            os.mkdir(exchange_path)

    folder = account_var.inbox / exchange_folder_name
    for item in folder.all().order_by('-datetime_received')[:lastitems]:
        if item.datetime_received.astimezone() > current_date.today_as_ews_datetime:  # aktuell gestern
            for attachment in item.attachments:
                if isinstance(attachment, FileAttachment):
                    if 'TC_ORCXOXI' in attachment.name:
                        local_path = os.path.join(xitaro_path, attachment.name)
                        with open(local_path, 'wb') as f:
                            f.write(attachment.content)
                    elif 'TC_ORCATD' in attachment.name:
                        local_path = os.path.join(tradegate_path, attachment.name)
                        with open(local_path, 'wb') as f:
                            f.write(attachment.content)
                    elif 'TC_Orca' in attachment.name:
                        local_path = os.path.join(frankfurt_path, attachment.name)
                        with open(local_path, 'wb') as f:
                            f.write(attachment.content)


def main():
    account = create_account('lenski')
    save_attachment_steubing_reports('Steubing Reports', account, lastitems=80)


if __name__ == '__main__':
    main()
