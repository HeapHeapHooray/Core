import CoreSystem
from typing import Union
from .PathNode import PathNode

def create_from_os_path(path: str) -> PathNode:
    system_info = CoreSystem.System.get_system_info()
    if system_info.is_windows():
        return create_from_windows_path(path)
    return create_from_linux_path(path)
def create_from_path_node(node: PathNode) -> PathNode:
    full_path = node.get_full_path()
    if len(full_path) < 1:
        return PathNode("",None)
    root_node = PathNode(full_path[0].get_name(),None)
    if len(full_path) < 2:
        return root_node
    new_node = root_node
    for node in full_path[1::]:
        new_node = new_node.create_node(node.get_name())
    return new_node
def create_from_os_path_or_path_node(os_path_or_path_node: Union[PathNode,str]) -> PathNode:
    if type(os_path_or_path_node) is str:
        return create_from_os_path(os_path_or_path_node)
    last_node = os_path_or_path_node
    return create_from_path_node(last_node)
def create_from_linux_path(path: str) -> PathNode:
    split = path.split('/')
    split = [element for element in split if element != '']
    if len(split) < 1:
        return PathNode(path,None)
    if path[0] == '/':
        new_split = ['/']
        new_split.extend(split)
        split = new_split
    current = PathNode(split[0],None)
    for node in split[1::]:
        current = current.create_node(node)
    return current
def create_from_windows_path(path: str) -> PathNode:
    split = path.split('\\')
    split = [element for element in split if element != '']
    if len(split) < 1:
        return PathNode(path,None)
    current = PathNode(split[0],None)
    for node in split[1::]:
        current = current.create_node(node)
    return current
