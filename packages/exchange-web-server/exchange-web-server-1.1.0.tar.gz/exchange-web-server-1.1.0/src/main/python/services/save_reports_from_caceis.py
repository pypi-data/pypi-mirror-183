"""
@author: baier, created on 08.07.2021
This script will provide automatically saved Caceis Files into the desired folder structure.
"""
import logging
import os
import exchangelib

from exchangelib import Message, FileAttachment, ItemAttachment
from python.io_operations.make_directory import make_directory
from python.logs.date_time import CurrentDate
from python.services.functions.mounted_directory import construct_file_path


def save_attachment_caseis_kontoauszuege(exchange_folder_name: str, account_var: exchangelib.Account, lastitems=50,
                                         current_date: CurrentDate = CurrentDate()):
    dest_fold = construct_file_path(r"Caceis/Kontoauszüge")

    current_month_path = os.path.join(dest_fold, current_date.current_month)
    make_directory(current_month_path)

    path = os.path.join(current_month_path, current_date.yesterday.strftime("%d.%m.%Y"))
    make_directory(path)

    count_up = 0

    folder: exchangelib.Folder = account_var.inbox / exchange_folder_name
    for item in folder.all().order_by('-datetime_received')[:lastitems]:
        if item.datetime_received.astimezone() > current_date.today_as_ews_datetime:
            for attachment in item.attachments:
                if isinstance(attachment, FileAttachment):
                    local_path = os.path.join(path, attachment.name)
                    if os.path.exists(local_path):
                        logging.warning(f'{attachment.name} is already saved.')
                    else:
                        with open(local_path, 'wb') as f:
                            f.write(attachment.content)
                        logging.info(f"Saved {attachment.name} to {local_path}")
                    count_up += 1
                elif isinstance(attachment, ItemAttachment):
                    if isinstance(attachment.item, Message):
                        print(attachment.item.subject, attachment.item.body)
    if count_up == 0:
        return logging.error(f'Found {count_up} Caceis Kontoauszüge - they are missing!')
    return logging.info(f'Found [{count_up}] files.')


def save_attachment_caseis_clearing(exchange_folder_name: str, account_var: exchangelib.Account, lastitems=1,
                                    current_date: CurrentDate = CurrentDate()):
    dest_folders = [construct_file_path(mnt_directory) for mnt_directory in
                    [r"Caceis/WP Abrechnungen", r"Caceis/Depotauszüge", rf"1 Konvertierer/Caceis/Umbuchungen/"
                                                                        rf"{current_date.today.year}"]]
    make_directory(dest_folders[2])
    for i, mnt_path in enumerate(dest_folders):
        constructed_path: os.path = os.path.join(mnt_path, current_date.current_month)
        make_directory(constructed_path)
        dest_folders[i] = constructed_path

    count_up = 0

    folder: exchangelib.Folder = account_var.inbox / exchange_folder_name
    for item in folder.all().order_by('-datetime_received')[:lastitems]:
        if item.datetime_received.astimezone() > current_date.today_as_ews_datetime:
            for attachment in item.attachments:
                if isinstance(attachment, FileAttachment):
                    if attachment.name == 'phyabrech.pdf':
                        log_and_save_attachment(attachment, dest_folders, current_date, 0)
                        count_up += 1
                    elif attachment.name == 'phyoffpos.pdf':
                        log_and_save_attachment(attachment, dest_folders, current_date, 1)
                        count_up += 1
                    elif attachment.name == 'misctransaction.csv':
                        log_and_save_attachment(attachment, dest_folders, current_date, 2)
                        count_up += 1
    if count_up != 3:
        return logging.error(f'Found {count_up} Caceis Clearings - some of them are missing!')
    elif count_up == 0:
        return logging.error(f'Found {count_up} Caceis Clearings - they are missing!')
    return logging.info(f'Found [{count_up}] files.')


def log_and_save_attachment(attachment: FileAttachment, dest_folders: list, current_date: CurrentDate, index: int) -> None:
    logging.info(f'Found {attachment.name}.')
    path_to_save = os.path.join(dest_folders[index], f"{current_date.yesterday.strftime('%d.%m.%Y')} {attachment.name}")
    if os.path.exists(path_to_save):
        return logging.warning(f'{attachment.name} is already saved.')
    with open(path_to_save, 'wb') as f:
        f.write(attachment.content)
    return logging.info(f"Saved {attachment.name} to {path_to_save}")


def save_reports_from_caceis(account: exchangelib.Account):
    current_date: CurrentDate = CurrentDate()
    logging.info(f"Current month is [{current_date.current_month}]")
    logging.info(f"Processing date of [{current_date.yesterday.strftime('%d.%m.%Y')}] ...")
    save_attachment_caseis_kontoauszuege(
        exchange_folder_name='Caceis reporting',
        account_var=account,
        current_date=current_date
    )  # 'Kontoauszüge Caceis' bei Johannas Postfach

    save_attachment_caseis_clearing(
        exchange_folder_name='Clearing Caceis',
        account_var=account,
        current_date=current_date
    )
    logging.info(f"Processed Caceis Reports!")
