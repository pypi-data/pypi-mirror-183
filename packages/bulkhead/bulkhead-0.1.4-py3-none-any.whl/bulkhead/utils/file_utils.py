import os


def make_full_filename(prefix: str, file_name: str) -> str:
    """
    The make_full_filename function takes a prefix and a file_name as input.
    If the prefix is None, then the file_name is returned unchanged.
    Otherwise, if the file name starts with 'http://' or 'ftp://', then it's assumed to be an URL and
    the full_filename will contain both the prefix and file_name; otherwise, only return full_filename = file_name.

    :param prefix: Used to Add a prefix to the file_name.
    :param file_name: Used to Create a full file_name for the file to be downloaded.
    :return: The full file_name with the prefix added to the beginning of the file_name.

    :doc-author: Trelent
    """
    if prefix is None:
        file_name = file_name
    elif prefix.endswith("/") and file_name.startswith("/"):
        file_name = prefix + file_name[1:]
    elif prefix.endswith("/") or file_name.startswith("/"):
        file_name = prefix + file_name
    else:
        file_name = prefix + "/" + file_name
    return file_name


def check_make_dir(dir_name: str) -> None:
    """
    The check_make_dir function checks if a directory exists. If it does not exist, the function creates it.

    :param dir_name:str: Used to Specify the folder name.
    :return: None.

    :doc-author: Julian M. Kleber
    """

    check_folder = os.path.isdir(dir_name)
    # If folder doesn't exist, then create it.
    if not check_folder:
        os.makedirs(dir_name)
