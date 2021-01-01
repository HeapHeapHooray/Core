import CorePath
from typing import Union

from .DatabasesDirectory import DatabasesDirectory

def get_databases_directory_from(directory_path: Union[CorePath.PathNode,str]):
    return DatabasesDirectory(directory_path)
