import CorePath
import CoreDatabase
from typing import Union

from .IncorrectPassword import IncorrectPassword

class Wallet:
    def __init__(self,path: Union[CorePath.PathNode,str]):
        self.path = CorePath.Path.create_from_os_path_or_path_node(path)
    def get_path(self) -> CorePath.PathNode:
        return CorePath.Path.create_from_path_node(self.path)
    def get_databases(self) -> CoreDatabase.DatabasesDirectory:
        databases_directory_path = self.get_path().create_node("databases")
        return CoreDatabase.DatabasesDirectoryFactory.get_databases_directory_from(databases_directory_path)
    def get_credentials(self) -> CoreDatabase.Database:
        credentials_path = self.get_path().create_node("credentials.json")
        return CoreDatabase.DatabaseFactory.get_database_from(credentials_path)
    def get_username(self) -> str:
        database = self.get_credentials()
        database_data = database.get_data_as_dict()
        return database_data["username"]
    def set_password(self,new_password: str,current_password: str):
        credentials_path = self.get_credentials().get_path()
        database_writer = CoreDatabase.DatabaseWriter.DatabaseWriterFactory.get_json_database_writer_from(credentials_path)
        credentials_data = database_writer.get_data_as_dict()
        if credentials_data["password"] != current_password:
            raise IncorrectPassword("The provided current password is incorrect.")
        credentials_data["password"] = new_password
        database_writer.overwrite_data(credentials_data)
