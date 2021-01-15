import os
import CorePath

def get_code_directory_path() -> CorePath.PathNode :
    string_path = os.path.dirname(os.path.abspath(__file__))
    return CorePath.Path.create_from_os_path(string_path).get_parent()
def get_core_directory_path() -> CorePath.PathNode :
    return get_code_directory_path().get_parent()
def get_assets_directory_path() -> CorePath.PathNode :
    return get_core_directory_path().create_node("assets")
def get_third_party_directory_path() -> CorePath.PathNode:
    return get_core_directory_path().create_node("third_party")
def get_temporary_directory_path() -> CorePath.PathNode:
    return get_core_directory_path().create_node("temp")
def get_default_databases_directory_path() -> CorePath.PathNode:
    return get_core_directory_path().create_node("databases")
def get_wallets_directory_path() -> CorePath.PathNode:
    return get_core_directory_path().create_node("wallets")
