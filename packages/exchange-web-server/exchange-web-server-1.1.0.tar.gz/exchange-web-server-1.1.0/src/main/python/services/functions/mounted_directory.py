import os


def construct_file_path(dir_: str, file: str = '') -> os.path:
    """
    :param dir_: Specify the upper directory to look in.
    :param file: Filename of txt.
    :return: os.path to NAS.
    """
    search_string = 'src'
    abs_path = os.path.join(os.path.abspath(__file__))
    if search_string in abs_path:
        src_index = abs_path.rfind(search_string)
        abs_path = abs_path[:src_index + len(search_string)]
        if file:
            return os.path.join(abs_path, 'mnt', dir_, file)
        return os.path.join(abs_path, 'mnt', dir_)
    if file:
        return os.path.join(r'src', 'mnt', dir_, file)
    return os.path.join(r'src', 'mnt', dir_)
