import cv2
import CoreImage
import CoreGUI
import CorePath
from typing import Union

class Video:
    #path_to_file can be a str or a PathNode.
    def __init__(self,*,path_to_file : Union[CorePath.PathNode,str,None] = None,url : Union[str,None] = None):
        path = ""
        self.is_path_url = False
        self._title = "Untitled"
        if path_to_file is not None:
            path_to_file = CorePath.Path.create_from_os_path_or_path_node(path_to_file)
            path = path_to_file.get_os_path()
            path_node = path_to_file
            self._title = path_node.get_name()
        if url is not None:
            path = url
            self.is_path_url = True
            self._title = path
            
        self._video_resource = cv2.VideoCapture(path)
        self.video_path = path
    def get_frame_count(self):
        self.update()
        frame_count = int(self._video_resource.get(cv2.CAP_PROP_FRAME_COUNT))-self.get_framerate()
        if frame_count < 0:
            frame_count = 1
        return frame_count
    def display(self,*,muted=False):
        if self.is_path_url:
            display = CoreGUI.VideoDisplayFactory.create_for_url(self.video_path,
                                                                 self._title)
        else:
            display = CoreGUI.VideoDisplayFactory.create_for_file(self.video_path,
                                                                  self._title)
        if muted:
            display.mute()
        else:
            display.unmute()
            
        display.open()
        return display
    def set_title(self,title: str):
        self._title = title
    def get_title(self) -> str:
        return self._title
    def get_framerate(self):
        return int(self._video_resource.get(cv2.CAP_PROP_FPS))
    def get_duration(self):
        return self.get_frame_count()/self.get_framerate()
    def update(self):
        self._video_resource.release()
        self._video_resource = cv2.VideoCapture(self.video_path)
    def get_frame(self,frame_number):
        self.update()
        if frame_number < 0 or frame_number >= self.get_frame_count():
            return None
        self._video_resource.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
        success,data = self._video_resource.read()
        if not success:
            return None
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        image = CoreImage.ImageFactory.create_from_numpy_array(data)
        return image
    def get_first_frame(self):
        return self.get_frame(0)
    def get_last_frame(self):
        return self.get_frame(self.get_frame_count()-1)
        
