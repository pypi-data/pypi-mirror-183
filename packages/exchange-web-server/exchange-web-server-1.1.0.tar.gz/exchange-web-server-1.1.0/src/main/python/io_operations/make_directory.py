import logging
import os


def make_directory(path: os.path) -> os.path:
    if not os.path.isdir(path):
        os.mkdir(path)
        logging.info(f'Created directory: [{path}].')
        return path
    logging.info(f'Directory: [{path}] already existed. Not creating folder.')
    return path
