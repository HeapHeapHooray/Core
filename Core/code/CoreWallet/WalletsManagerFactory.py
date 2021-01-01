import CorePath
from typing import Union

from .WalletsManager import WalletsManager

def get_wallets_manager_from(path: Union[CorePath.PathNode,str]) -> WalletsManager:
    return WalletsManager(path)
