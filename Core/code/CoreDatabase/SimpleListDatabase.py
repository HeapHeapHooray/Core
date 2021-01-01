import CorePath
import CoreFileSystem
import CoreParsers
from typing import Union,List

class SimpleListDatabase:
    def __init__(self,common_file_path: Union[CorePath.PathNode,str]):
        self.path = CorePath.Path.create_from_os_path_or_path_node(common_file_path)
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.path)
    def get_data_as_list(self) -> List[str]:
        file = CoreFileSystem.FileSystem.get_common_file(self.get_path())
        data = file.read_all().decode("utf-8")
        output_list = CoreParsers.SimpleListParser.parse_to_list(data)
        return output_list
    def get_data_as_dict(self) -> dict:
        data = self.get_data_as_list()
        output_dict = {k:v for k,v in enumerate(data) }
        return output_dict
    def get_data_as_specialized_object(self) -> list:
        return self.get_data_as_list()
    def get_data_element(self,key: int) -> str:
        return self.get_data_as_list()[key]
