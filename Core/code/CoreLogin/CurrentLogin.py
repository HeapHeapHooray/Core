import CoreWallet
import CoreFileSystem
import CoreDatabase

_current_login_username = None

def get_wallet():
    wallets_manager = CoreWallet.DefaultWalletsManager.get_default_wallets_manager()
    global _current_login_username
    wallet = wallets_manager.get_wallet(_current_login_username)
    return wallet
def _initialize():
    global _current_login_username
    wallets_manager = CoreWallet.DefaultWalletsManager.get_default_wallets_manager()
    if not "default" in wallets_manager.get_wallets_list():
        wallets_manager.create_wallet("default","")
    remember_me_path = CoreFileSystem.CoreDirectories.get_core_directory().create_node("remember_me.json")
    if CoreFileSystem.FileSystem.item_exists(remember_me_path):
        remember_me_database = CoreDatabase.DatabaseFactory.get_json_database_from(remember_me_path)
        remember_me_dict = remember_me_database.get_data_as_dict()
        if "username" in remember_me_dict.keys():
            _current_login_username = remember_me_dict["username"]
        else:
            _current_login_username = "default"
    else:
        _current_login_username = "default"

_initialize()
