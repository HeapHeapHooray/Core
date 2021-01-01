import CoreSystem

class PathNode:
    def __init__(self,name : str,parent=None):
        self.name = name
        self.parent = parent
    def get_name(self) -> str:
        return self.name
    def get_parent(self):
        return self.parent
    def set_parent(self,parent):
        self.parent = parent
    def set_name(self,name : str):
        self.name = name
    def create_node(self,name : str):
        return PathNode(name,self)
    def is_root(self):
        return self.get_parent() is None
    def __str__(self):
        return "PathNode: " + self.name
    def get_full_path(self):
        parent = self.get_parent()
        full_path = [self]
        while parent != None:
            full_path.append(parent)
            parent = parent.get_parent()
        full_path.reverse()
        return full_path
    def get_os_path(self) -> str:
        system_info = CoreSystem.System.get_system_info()
        if system_info.is_windows():
            return self.get_windows_path()
        return self.get_linux_path()
    def get_linux_path(self) -> str:
        full_path = self.get_full_path()
        linux_path = '/'.join([node.get_name() for node in full_path])
        if len(full_path) < 2:
            return linux_path
        if linux_path[0] == '/':
            linux_path = linux_path[1::]
        return linux_path
    def get_windows_path(self) -> str:
        full_path = self.get_full_path()
        if len(full_path) == 1 and ':' in full_path[0].get_name():
            return full_path[0].get_name() + "\\"
        return '\\'.join([node.get_name() for node in full_path])
