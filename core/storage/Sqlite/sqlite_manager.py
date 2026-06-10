import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)
import sqlite3
import core.storage.Sqlite.page as page
import core.storage.Sqlite.task as task
import core.storage.path_manager as path_manager

class SqliteManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    #region Page Operations
    def create_page(self, page_name,id,create_date,update_date):
        page.create_page.create_page(page_id=id,title=page_name, created_at=create_date, updated_at=update_date,path=self.folder_path)
    def get_page_id(self,page_id):
        return page.get_page.get_page_id(page_id=page_id,path=self.folder_path)
    def get_page_name(self,page_name):
        return page.get_page.get_page_name(page_name=page_name,path=self.folder_path)
    def update_page(self,page_id, new_title,update_date):
        return page.update_page.update_page(page_id=page_id, new_title=new_title,update_date=update_date,path=self.folder_path)
    def delete_page(self,page_id):
        return page.delete_page.delete_page(page_id=page_id,path=self.folder_path)
