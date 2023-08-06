import logging
import exchangelib

from python.logs.date_time import CurrentDate
from python.services.functions.mounted_directory import construct_file_path


def save_attachment_morrison_reports(
        exchange_folder_name: str,
        exchange_subfolder_name: str,
        account_var: exchangelib.Account,
        lastitems: int
):
    from exchangelib import FileAttachment
    import os.path

    current_date = CurrentDate()

    this_day_path = construct_file_path(
        rf'Morrison Evolution/Bestände/{current_date.current_month}/{current_date.yesterday.day:02}'
    )

    for path in [this_day_path]:
        if not os.path.isdir(path[:-3]):
            os.mkdir(path[:-3])
            logging.info(f'Created directory: [{path[:-3]}].')
        if not os.path.isdir(path):
            os.mkdir(path)
            logging.info(f'Created directory: [{path}].')

    folder = account_var.inbox / exchange_folder_name / exchange_subfolder_name
    for item in folder.all().order_by('-datetime_received')[:lastitems]:
        if item.datetime_received.astimezone() > current_date.yesterday_as_ews_datetime:
            for attachment in item.attachments:
                if isinstance(attachment, FileAttachment):
                    if 'TPFUDI_Orca_ContractNotesListing' in attachment.name or 'HoldingsStatement' in attachment.name:
                        logging.info(f'Found {attachment.name}.')
                        local_path = os.path.join(this_day_path, attachment.name)
                        with open(local_path, 'wb') as f:
                            f.write(attachment.content)
                        logging.info(f"Saved {attachment.name} to {local_path}")


def save_reports_morrison(account: exchangelib.Account):
    save_attachment_morrison_reports('Fibu', 'Evolution', account, lastitems=20)
    logging.info('Processed Morrison Reports!')
