import os
import CoreFileSystem
import CoreSystem

try:
    system_info = CoreSystem.System.get_system_info()
    
    if system_info.is_windows():
        third_party_path = CoreFileSystem.CoreDirectories.get_third_party_directory_path()
        vlc_path = third_party_path.create_node("Windows").create_node("VLC")
        os.add_dll_directory(vlc_path.get_os_path())
        del vlc_path
        del third_party_path
    del system_info

    import vlc
except:
    pass

def get_vlc_instance():
    return vlc.Instance("--verbose=-1 --no-video-title --no-snapshot-preview --no-xlib")
