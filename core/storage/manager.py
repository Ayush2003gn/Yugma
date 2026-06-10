import core.storage.path_manager as pathmanager
import core.storage.json_storage as jsonstorage
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
from core.storage.Sqlite.sqlite_manager import SqliteManager
import logging
logger = logging.getLogger(__name__)

class StorageManager:
    def __init__(self):
        self.sqlite_manager = SqliteManager(pathmanager.get_data_folder())
        self.json_storage = jsonstorage.JsonStorage(pathmanager.config_file())
        pathmanager.ensure_data_folder_directory()
        