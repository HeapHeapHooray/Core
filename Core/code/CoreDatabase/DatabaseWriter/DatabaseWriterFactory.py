import CorePath
from typing import Union

from .SimpleListDatabaseWriter import SimpleListDatabaseWriter
from .JSONDatabaseWriter import JSONDatabaseWriter

def get_simple_list_database_writer_from(common_file_path: Union[CorePath.PathNode,str]):
    return SimpleListDatabaseWriter(common_file_path)
def get_json_database_writer_from(common_file_path: Union[CorePath.PathNode,str]):
    return JSONDatabaseWriter(common_file_path)
