import CoreVLC
import CorePath
from typing import Union

from .VideoDisplay import VideoDisplay

def create_for_url(url: str,title: str = "Untitled"):
    instance = CoreVLC.get_vlc_instance()
    player = instance.media_player_new()
    player.set_mrl(url)

    return VideoDisplay(instance,player,title)
def create_for_file(path_to_file: Union[CorePath.PathNode,str],title: str = "Untitled"):
    path_to_file = CorePath.Path.create_from_os_path_or_path_node(path_to_file)
    instance = CoreVLC.get_vlc_instance()
    player = instance.media_player_new()
    player.set_mrl(path_to_file.get_os_path())
        
    return VideoDisplay(instance,player,title)
