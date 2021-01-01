import CorePath
import CoreFileSystem
import CoreParsers
from typing import Union,List

from ..SimpleListDatabase import SimpleListDatabase

class SimpleListDatabaseWriter(SimpleListDatabase):
    def __init__(self,common_file_path: Union[CorePath.PathNode,str]):
        super().__init__(common_file_path)
    def overwrite_data(self,new_data: List[str]):
        self.__create_file_if_does_not_exists()
        file = CoreFileSystem.FileSystem.get_common_file(self.get_path())
        data = CoreParsers.SimpleListParser.convert_list_to_simple_list_data(new_data).encode("utf-8")
        file.overwrite_data(data)
    def append_to_data(self,appending: List[str]):
        self.__create_file_if_does_not_exists()
        file = CoreFileSystem.FileSystem.get_common_file(self.get_path())
        data = CoreParsers.SimpleListParser.convert_list_to_simple_list_data(appending)
        if file.get_size() != 0:
            data = '\n' + data
        data = data.encode("utf-8")
        file.append_to_data(data)
    def __create_file_if_does_not_exists(self):
        if not CoreFileSystem.FileSystem.item_exists(self.get_path()):
            CoreFileSystem.FileSystem.create_common_file(self.get_path())
