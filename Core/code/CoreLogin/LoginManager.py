import CoreWallet
import CoreFileSystem
import CoreDatabase

from .InvalidPassword import InvalidPassword
from . import CurrentLogin

def login(username: str,password: str,remember_me = False):
    wallets_manager = CoreWallet.DefaultWalletsManager.get_default_wallets_manager()
    wallet = wallets_manager.get_wallet(username)
    credentials = wallet.get_credentials()
    wallet_password = credentials.get_data_element("password")
    if password != wallet_password and wallet_password != "":
        raise InvalidPassword("The provided password is invalid.")
    CurrentLogin._current_login_username = username

    if remember_me:
        _set_remember_me({"username": CurrentLogin._current_login_username})
    else:
        _erase_remember_me()
def _erase_remember_me():
    _set_remember_me({})
def _set_remember_me(data: dict):
    remember_me_path = CoreFileSystem.CoreDirectories.get_core_directory().create_node("remember_me.json")
    remember_me_database_writer = CoreDatabase.DatabaseWriter.DatabaseWriterFactory.get_json_database_writer_from(remember_me_path)
    remember_me_database_writer.overwrite_data(data)
