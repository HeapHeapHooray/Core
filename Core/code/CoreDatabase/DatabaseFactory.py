import CorePath
from typing import Union

from .Database import Database
from .SimpleListDatabase import SimpleListDatabase
from .JSONDatabase import JSONDatabase

def get_database_from(common_file_path: Union[CorePath.PathNode,str]) -> Database:
    return Database(common_file_path)
def get_simple_list_database_from(common_file_path: Union[CorePath.PathNode,str]) -> SimpleListDatabase:
    return SimpleListDatabase(common_file_path)
def get_json_database_from(common_file_path: Union[CorePath.PathNode,str]) -> JSONDatabase:
    return JSONDatabase(common_file_path)
