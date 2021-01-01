import CorePath
import CoreFileSystem
import CoreParsers
from typing import Union

from .InvalidDatabaseFile import InvalidDatabaseFile

def is_valid_database_file(common_file_path: Union[CorePath.PathNode,str]):
    try:
        get_database_name_for_common_file(common_file_path)
        return True
    except InvalidDatabaseFile:
        pass
    return False
def get_database_for_common_file(common_file_path: Union[CorePath.PathNode,str]):
    from . import DatabaseFactory
    name = get_database_name_for_common_file(common_file_path)
    if name == "JSONDatabase":
        return DatabaseFactory.get_json_database_from(common_file_path)
    return DatabaseFactory.get_simple_list_database_from(common_file_path)
def get_database_name_for_common_file(common_file_path: Union[CorePath.PathNode,str]):
    file = CoreFileSystem.FileSystem.get_common_file(common_file_path)
    extension = file.get_extension()
    
    simple_list_database_extensions = ["sl","simplelist","simple_list"]
    if extension in simple_list_database_extensions:
        return "SimpleListDatabase"

    json_database_extensions = ["json"]
    if extension in json_database_extensions:
        return "JSONDatabase"

    try:
        data = file.read_all().decode("utf-8")
        CoreParsers.JSONParser.parse_to_dict(data)

        return "JSONDatabase"
    except:
        pass

    raise InvalidDatabaseFile("The provided file is not recognized as any database format.")
