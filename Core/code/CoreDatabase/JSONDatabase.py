import CorePath
import CoreFileSystem
import CoreParsers
from typing import Union

class JSONDatabase:
    def __init__(self,common_file_path: Union[CorePath.PathNode,str]):
        self.path = CorePath.Path.create_from_os_path_or_path_node(common_file_path)
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.path)
    def get_data_as_dict(self) -> dict:
        file = CoreFileSystem.FileSystem.get_common_file(self.get_path())
        data = file.read_all().decode("utf-8")
        output_dict = CoreParsers.JSONParser.parse_to_dict(data)
        return output_dict
    def get_data_as_specialized_object(self) -> dict:
        return self.get_data_as_dict()
    def get_data_element(self,key):
        return self.get_data_as_dict()[key]
