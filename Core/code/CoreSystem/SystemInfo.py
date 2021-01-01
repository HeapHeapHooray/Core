class SystemInfo:
    def __init__(self,system):
        self._system = system
    def is_linux(self):
        return self._system == "Linux"
    def is_windows(self):
        return self._system == "Windows"
    def get_system_name(self):
        if self.is_linux():
            return "Linux"
        if self.is_windows():
            return "Windows"
        return "Unknown"
    def is_unknown(self):
        return self.get_system_name() == "Unknown"
