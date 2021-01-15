import CoreFileSystem

from .DatabasesDirectory import DatabasesDirectory
from . import DatabasesDirectoryFactory

class DefaultDatabases:
    def get_default_databases() -> DatabasesDirectory:
        return DatabasesDirectoryFactory.get_databases_directory_from(CoreFileSystem.CoreDirectories.get_default_databases_directory_path())
