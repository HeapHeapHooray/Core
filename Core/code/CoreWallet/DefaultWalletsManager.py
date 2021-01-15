import CoreFileSystem

from .WalletsManager import WalletsManager
from . import WalletsManagerFactory

def get_default_wallets_manager() -> WalletsManager:
    return WalletsManagerFactory.get_wallets_manager_from(CoreFileSystem.CoreDirectories.get_wallets_directory_path())
