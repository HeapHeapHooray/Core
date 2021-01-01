import os
import CorePath
from typing import Union

from .Item import Item
from .CommonFileNotFoundAtPath import CommonFileNotFoundAtPath
from . import Utils

class CommonFile(Item):
    def __init__(self,path_to_file: Union[CorePath.PathNode,str]):
        super().__init__(path_to_file)
        if not self.is_common_file():
            raise CommonFileNotFoundAtPath("The provided path doesn't leads to a common file.")
    def get_size(self) -> int:
        return os.path.getsize(self.get_path().get_os_path())
    def get_extension(self) -> Union[None,str]:
        return Utils.get_extension_from_name(self.get_name())
    def read_bytes(self,bytes_count: int,*,starting_point = 0) -> bytes:
        with open(self.get_path().get_os_path(),mode='rb') as file:
            file.seek(starting_point)
            return file.read(bytes_count)
    def read_all(self,*,starting_point = 0) -> bytes:
        with open(self.get_path().get_os_path(),mode='rb') as file:
            file.seek(starting_point)
            return file.read()
    def overwrite_data(self,new_data: bytes):
        with open(self.get_path().get_os_path(),mode='wb') as file:
            file.write(new_data)
    def append_to_data(self,appending: bytes):
        with open(self.get_path().get_os_path(),mode='ab') as file:
            file.write(appending)
