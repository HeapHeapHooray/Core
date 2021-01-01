import CorePath
import CoreFileSystem
from typing import Union,List

from .DatabaseNotFound import DatabaseNotFound
from . import DatabaseFactory
from . import Utils
from .Database import Database

class DatabasesDirectory:
    def __init__(self,directory_path):
        self.path = CorePath.Path.create_from_os_path_or_path_node(directory_path)
        #We call this here because it will raise an exception if the directory doesnt exists.
        CoreFileSystem.FileSystem.get_directory(directory_path)
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.path)
    def get_name(self) -> str:
        return self.get_path().get_name()
    def get_databases_list(self) -> List[str]:
        directory = CoreFileSystem.FileSystem.get_directory(self.get_path())
        content = directory.get_content()
        names = [item.get_name() for item in content if item.is_common_file() and Utils.is_valid_database_file(item.get_path())]
        return names
    def get_database(self,database_name: str) -> Database:
        directory = CoreFileSystem.FileSystem.get_directory(self.get_path())
        content = directory.get_content()
        filtered = [item for item in content if item.get_name() == database_name]
        if len(filtered) < 1 or not filtered[0].is_common_file() or not Utils.is_valid_database_file(filtered[0].get_path()):
            raise DatabaseNotFound("The provided database name was not found in the directory.")
        database_item = filtered[0]
        return DatabaseFactory.get_database_from(database_item.get_path())
