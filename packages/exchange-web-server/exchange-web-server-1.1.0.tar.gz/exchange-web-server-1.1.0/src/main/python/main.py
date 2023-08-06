import logging
from time import sleep

import schedule
from python.configuration.config import create_accounts
from python.logs.logger import create_logger
from python.services.functions.save_attachment import save_attachment
from python.services.functions.mounted_directory import construct_file_path
from python.services.save_crypto_currencies_exchange_rates import get_daily_crypto_currencies_exchange_rates
from python.services.save_isin_mapping import map_isins
from python.services.save_reports_from_caceis import save_reports_from_caceis
from python.services.save_reports_morrison import save_reports_morrison
from python.services.send_caceis_japan_trades import process_japan_file


def main() -> None:
    create_logger()
    accounts: dict = create_accounts()
    trade_overview_steubing_path = construct_file_path("Steubing")

    logging.info("Starting scheduling tasks...")

    schedule.every().monday.at('03:00').do(map_isins)
    schedule.every().tuesday.at('03:00').do(map_isins)
    schedule.every().wednesday.at('03:00').do(map_isins)
    schedule.every().thursday.at('03:00').do(map_isins)
    schedule.every().friday.at('03:00').do(map_isins)

    schedule.every().day.at('06:00').do(
        get_daily_crypto_currencies_exchange_rates
    )

    schedule.every().tuesday.at('07:00').do(save_reports_from_caceis, accounts["beck"])
    schedule.every().wednesday.at('07:00').do(save_reports_from_caceis, accounts["beck"])
    schedule.every().thursday.at('07:00').do(save_reports_from_caceis, accounts["beck"])
    schedule.every().friday.at('07:00').do(save_reports_from_caceis, accounts["beck"])
    schedule.every().saturday.at('07:00').do(save_reports_from_caceis, accounts["beck"])

    schedule.every().monday.at('08:15').do(save_reports_morrison, accounts["buchhaltung"])
    schedule.every().tuesday.at('08:15').do(save_reports_morrison, accounts["buchhaltung"])
    schedule.every().wednesday.at('08:15').do(save_reports_morrison, accounts["buchhaltung"])
    schedule.every().thursday.at('08:15').do(save_reports_morrison, accounts["buchhaltung"])
    schedule.every().friday.at('08:15').do(save_reports_morrison, accounts["buchhaltung"])

    schedule.every().monday.at('18:45').do(process_japan_file, accounts["kreutmair"])
    schedule.every().tuesday.at('18:45').do(process_japan_file, accounts["kreutmair"])
    schedule.every().wednesday.at('18:45').do(process_japan_file, accounts["kreutmair"])
    schedule.every().thursday.at('18:45').do(process_japan_file, accounts["kreutmair"])
    schedule.every().friday.at('18:45').do(process_japan_file, accounts["kreutmair"])

    schedule.every().monday.at('23:45').do(save_attachment, "Steubing", trade_overview_steubing_path, accounts["kreutmair"])
    schedule.every().tuesday.at('23:45').do(save_attachment, "Steubing", trade_overview_steubing_path, accounts["kreutmair"])
    schedule.every().wednesday.at('23:45').do(save_attachment, "Steubing", trade_overview_steubing_path, accounts["kreutmair"])
    schedule.every().thursday.at('23:45').do(save_attachment, "Steubing", trade_overview_steubing_path, accounts["kreutmair"])
    schedule.every().friday.at('23:45').do(save_attachment, "Steubing", trade_overview_steubing_path, accounts["kreutmair"])

    while True:  # Outer Loop for Docker Runtime
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main()
