"""
Created on 30.04.2021
This script can save email attachments into one specific directory and rename the file.
@author: baier
"""
import logging
import os
from exchangelib import Message, FileAttachment, ItemAttachment


def save_attachment(
        exchange_folder_name: str,
        save_to_folder: str,
        account_var,
        suffix: int = 0,
        prename: str = '',
        last_items: int = 1) -> str:
    folder = account_var.inbox / exchange_folder_name
    logging.info(f'Started looking for {exchange_folder_name}.')
    for item in folder.all().order_by('-datetime_received')[:last_items]:
        for attachment in item.attachments:
            logging.info(f'Number of Attachment found: {len(item.attachments)}.')
            if isinstance(attachment, FileAttachment):
                logging.info(f'Found {attachment.name}.')
                local_path = os.path.join(save_to_folder, f"{prename}{attachment.name[suffix:]}")
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                logging.info(f"Saved {attachment.name} to {local_path}")
                return local_path
            elif isinstance(attachment, ItemAttachment):
                if isinstance(attachment.item, Message):
                    print(attachment.item.subject, attachment.item.body)
