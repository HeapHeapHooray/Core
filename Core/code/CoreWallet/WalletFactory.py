import CorePath
from typing import Union

from .Wallet import Wallet

def get_wallet_from(path: Union[CorePath.PathNode,str]) -> Wallet:
    return Wallet(path)
