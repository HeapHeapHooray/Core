import os
import CorePath
import CoreSystem
from typing import Union

from .ItemNotFoundAtPath import ItemNotFoundAtPath

def open_path(path: Union[CorePath.PathNode,str]):
    path = CorePath.Path.create_from_os_path_or_path_node(path)
    path = path.get_os_path()
    system_info = CoreSystem.System.get_system_info()
    if system_info.is_windows():
        os.system('start "" "' + path + '"')
    if system_info.is_linux():
        os.system('xdg-open "' + path + '"')
def get_item(path_to_item: Union[CorePath.PathNode,str]):
    from .Item import Item
    return Item(path_to_item)
def get_common_file(path_to_common_file: Union[CorePath.PathNode,str]):
    from .CommonFile import CommonFile
    return CommonFile(path_to_common_file)
def get_directory(path_to_directory: Union[CorePath.PathNode,str]):
    from .Directory import Directory
    return Directory(path_to_directory)
def create_common_file(path_to_common_file: Union[CorePath.PathNode,str]):
    path = CorePath.Path.create_from_os_path_or_path_node(path_to_common_file)
    with open(path.get_os_path(),'a+') as file:
        pass
    return get_common_file(path)
def create_directory(path_to_directory: Union[CorePath.PathNode,str]):
    path = CorePath.Path.create_from_os_path_or_path_node(path_to_directory)
    os.mkdir(path.get_os_path())
    return get_directory(path)
def item_exists(path_to_item: Union[CorePath.PathNode,str]) -> bool:
    from .Item import Item
    try:
            Item(path_to_item)
    except ItemNotFoundAtPath:
        return False
    return True
