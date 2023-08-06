import pathlib


_root_dir = pathlib.Path(__file__).absolute().parent.parent


def get_root_dir():
    return _root_dir
