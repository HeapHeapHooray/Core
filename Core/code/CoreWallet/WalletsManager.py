import CorePath
import CoreDatabase
import CoreFileSystem
from typing import Union,List

from .Wallet import Wallet
from .WalletNotFound import WalletNotFound
from . import WalletFactory

class WalletsManager:
    def __init__(self,path: Union[CorePath.PathNode,str]):
        self.path = CorePath.Path.create_from_os_path_or_path_node(path)
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.path)
    def get_wallets_list(self) -> List[str]:
        directory = CoreFileSystem.FileSystem.get_directory(self.get_path())
        content = directory.get_content()
        folders = [item for item in content if item.is_directory()]
        folder_names = [item.get_name() for item in folders]
        return folder_names
    def get_wallet(self,username: str) -> Wallet:
        directory = CoreFileSystem.FileSystem.get_directory(self.get_path())
        content = directory.get_content()
        folders = [item for item in content if item.is_directory()]
        same_name = [item for item in folders if item.get_name() == username]
        if len(same_name) < 1:
            raise WalletNotFound("A Wallet with the provided username couldn't be found!")
        return WalletFactory.get_wallet_from(same_name[0].get_path())
    def create_wallet(self,username: str,password: str) -> Wallet:
        wallet_path = self.get_path().create_node(username)
        wallet_directory = CoreFileSystem.FileSystem.create_directory(wallet_path)
        databases_path = wallet_path.create_node("databases")
        databases_directory = CoreFileSystem.FileSystem.create_directory(databases_path)

        credentials_dict = {"username": username,"password": password}
        credentials_path = wallet_path.create_node("credentials.json")
        database_writer = CoreDatabase.DatabaseWriter.DatabaseWriterFactory.get_json_database_writer_from(credentials_path)
        database_writer.overwrite_data(credentials_dict)

        return WalletFactory.get_wallet_from(wallet_path)
