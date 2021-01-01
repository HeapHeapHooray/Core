import CorePath
import CoreFileSystem
import CoreParsers
from typing import Union

from ..JSONDatabase import JSONDatabase

class JSONDatabaseWriter(JSONDatabase):
    def __init__(self,common_file_path: Union[CorePath.PathNode,str]):
        super().__init__(common_file_path)
    def overwrite_data(self,new_data: dict):
        self.__create_file_if_does_not_exists()
        file = CoreFileSystem.FileSystem.get_common_file(self.get_path())
        data = CoreParsers.JSONParser.convert_dictionary_to_json(new_data).encode("utf-8")
        file.overwrite_data(data)
    def __create_file_if_does_not_exists(self):
        if not CoreFileSystem.FileSystem.item_exists(self.get_path()):
            CoreFileSystem.FileSystem.create_common_file(self.get_path())
