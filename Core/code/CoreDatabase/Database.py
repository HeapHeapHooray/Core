import CorePath
from typing import Union

from . import Utils

class Database:
    def __init__(self,common_file_path: Union[CorePath.PathNode,str]):
        self.path = CorePath.Path.create_from_os_path_or_path_node(common_file_path)
        #We call this here because it will raise an exception if the file doesnt exists or
        #if its an invalid database file.
        Utils.get_database_name_for_common_file(common_file_path)
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.path)
    def get_specialized_database_object(self):
        return Utils.get_database_for_common_file(self.get_path())
    def get_data_as_dict(self) -> dict:
        return self.get_specialized_database_object().get_data_as_dict()
    def get_data_as_specialized_object(self):
        return self.get_specialized_database_object().get_data_as_specialized_object()
    def get_data_element(self,key):
        return self.get_specialized_database_object().get_data_element(key)
