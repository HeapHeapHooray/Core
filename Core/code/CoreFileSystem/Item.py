import os
import shutil
import CorePath
from typing import Union

from .ItemNotFoundAtPath import ItemNotFoundAtPath
from . import FileSystem

class Item:
    def __init__(self,path_to_item: Union[CorePath.PathNode,str]):
        path_to_item = CorePath.Path.create_from_os_path_or_path_node(path_to_item)
        self.item_path = path_to_item
        exists = os.path.exists(self.get_path().get_os_path())
        if not exists:
            raise ItemNotFoundAtPath("The provided path doesn't leads to an item (i.e. theres nothing in the specified path !)")
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.item_path)
    def get_name(self) -> str:
        return self.get_path().get_name()
    def is_common_file(self) -> bool:
        return os.path.isfile(self.get_path().get_os_path())
    def is_directory(self) -> bool:
        return os.path.isdir(self.get_path().get_os_path())
    def is_unknown_item_type(self) -> bool:
        return self.get_item_type() == "Unknown"
    def get_item_type(self) -> str:
        if self.is_common_file():
            return "CommonFile"
        if self.is_directory():
            return "Directory"
        return "Unknown"
    def open(self):
        FileSystem.open_path(self.get_path())
    def get_specialized_item_object(self):
        if self.is_common_file():
            return FileSystem.get_common_file(self.get_path())
        if self.is_directory():
            return FileSystem.get_directory(self.get_path())
        return None
    def rename(self,new_name: str):
        current_path = self.get_path()
        new_path = CorePath.Path.create_from_path_node(self.get_path())
        new_path.set_name(new_name)
        os.rename(current_path.get_os_path(),new_path.get_os_path())
        self.item_path = new_path
    def copy_and_paste(self,location_to_paste: Union[CorePath.PathNode,str]):
        location_to_paste = CorePath.Path.create_from_os_path_or_path_node(location_to_paste)
        if self.is_directory():
            shutil.copytree(self.get_path().get_os_path(),location_to_paste.create_node(self.get_name()).get_os_path())
        else:
            shutil.copy2(self.get_path().get_os_path(),location_to_paste.get_os_path())
    def move(self,location_to_move: Union[CorePath.PathNode,str]):
        location_to_move = CorePath.Path.create_from_os_path_or_path_node(location_to_move)
        new_path = CorePath.Path.create_from_os_path(shutil.move(self.get_path().get_os_path(),location_to_move.get_os_path()))
        self.item_path = new_path
