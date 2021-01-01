import CoreTkinterRuntime
import CoreImage
import CoreUUID
import CoreFileSystem

class VideoDisplay:
    def __init__(self,vlc_instance,vlc_player,title):
        self._instance = vlc_instance
        self._player = vlc_player
        self.title = title
        self._window = None
    def open(self):
        if self.is_closed():
            self._window = CoreTkinterRuntime.VLCWindow(self.title,self._player)
        self.update()
    def close(self):
        if not self.is_closed():
            self._window.delete_window()
    def pause(self):
        self._player.pause()
    def play(self):
        if not self.is_closed():
            self._player.play()
    def mute(self):
        self._player.audio_set_mute(True)
    def unmute(self):
        self._player.audio_set_mute(False)
    def set_title(self,title: str):
        self.title = title
        self.update()
    def get_title(self):
        return self.title
    def set_current_frame(self,frame: int):
        position = (frame/self._player.get_fps())*1000
        self._player.set_time(int(position))
    def get_current_frame_as_image(self):
        snapshot_name = str(CoreUUID.UUIDGenerator.generate_random_uuid())
        path = CoreFileSystem.CoreDirectories.get_temporary_directory()
        path = path.create_node(snapshot_name+".png")
        self._player.video_take_snapshot(0,path.get_os_path(),0,0)
        image = CoreImage.ImageFactory.create_from_file(path.get_os_path())
        image.set_title("Video Display Snapshot: "+snapshot_name)
        return image
    def get_current_frame(self):
        frame = int(round((self._player.get_fps()*self._player.get_time()) / 1000))
        return frame
    def set_fullscreen(self,fullscreen: bool):
        if fullscreen == True:
            self._window.set_fullscreen()
        else:
            self._window.end_fullscreen()
    def is_closed(self):
        return self._window is None or self._window.is_destroyed()
    def update(self):
        if not self.is_closed():
            self._window.set_title(self.title)
