import os
import CorePath
from typing import Union,List

from .Item import Item
from .DirectoryNotFoundAtPath import DirectoryNotFoundAtPath

class Directory(Item):
    def __init__(self,path_to_directory: Union[CorePath.PathNode,str]):
        super().__init__(path_to_directory)
        if not self.is_directory():
            raise DirectoryNotFoundAtPath("The provided path doesn't leads to a directory.")
    def get_content(self) -> List[Item]:
        names = os.listdir(self.get_path().get_os_path())
        paths = [CorePath.Path.create_from_path_node(self.get_path()).create_node(name) for name in names]
        items = [Item(path) for path in paths]

        return items
    def is_empty(self) -> bool:
        return len(self.get_content()) == 0
