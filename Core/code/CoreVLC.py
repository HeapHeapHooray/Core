import os
import CoreFileSystem
import CoreSystem

try:
    system_info = CoreSystem.System.get_system_info()
    
    if system_info.is_windows():
        path = CoreFileSystem.CoreDirectories.get_third_party_directory_path()
        path = path.create_node("Windows").create_node("VLC")
        os.add_dll_directory(path.get_os_path())

    import vlc
except:
    pass

def get_vlc_instance():
    return vlc.Instance("--verbose=-1 --no-video-title --no-snapshot-preview --no-xlib")
