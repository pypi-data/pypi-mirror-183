import logging


def create_logger() -> None:
    logging.getLogger("exchangelib").setLevel(logging.WARNING)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    )

    logging.info('Logger has started')


if __name__ == '__main__':
    create_logger()
