"""
Created on 20.04.2021

@author: baier
"""
import logging
import os
import exchangelib
import pandas as pd
from dotenv import load_dotenv

from python.services.functions.send_email import send_email
from python.services.functions.save_attachment import save_attachment

load_dotenv()


def save_and_edit_caceis_japan_trades(path: os.path) -> os.path:
    df = pd.read_excel(path, sheet_name=0)

    # edit the file
    new_header = df.iloc[1]
    df = df[2:]
    df.columns = new_header
    df = df.reset_index(drop=True)
    rows = df[df.columns[0]].count()
    col_c = df['ISIN']
    for isin in range(rows):
        if col_c[isin][:2] != "JP":
            df = df.drop([isin])

    # change width of columns
    new_excel_name: str = 'reportJP.xlsx'
    output_path: os.path = os.path.join(os.path.dirname(__file__), new_excel_name)
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='report', index=False, na_rep='NaN')
        # Auto-adjust columns' width
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets['report'].set_column(col_idx, col_idx, column_width)

    return output_path


def send_caceis_japan_trades(path: os.path, account: exchangelib.Account) -> None:
    with open(path, 'rb') as f:
        content = f.read()
    attachments = [(os.path.basename(path), content)]

    send_email(
        account,
        'JP Common Stocks',
        'This is an automated email - do not reply',
        ['kugler@orcacapital.de'],
        attachments=attachments
    )


def process_japan_file(account: exchangelib.Account) -> None:
    logging.info("Start processing Japan file...")
    locally_saved_report = save_attachment('JoinITReport', os.path.dirname(__file__), account)
    new_excel_file = save_and_edit_caceis_japan_trades(locally_saved_report)
    os.remove(locally_saved_report)
    logging.info(f"Removed file {locally_saved_report}")
    send_caceis_japan_trades(new_excel_file, account)
    logging.info(f"Email was sent to kugler@orcacapital.de")

    os.remove(new_excel_file)
    logging.info(f"Removed file [{new_excel_file}]")
    logging.info("Processed Japan file!")
