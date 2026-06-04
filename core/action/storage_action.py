import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
import core.storage.manager as StorageManager
logger = logging.getLogger(__name__)

class storage_action:
    def __init__(self,task_app):
        self.task_app = task_app

    def load_storage(self):
        logger.info("Loading storage")
        data = StorageManager.load_page()
        logger.info(f"Storage load result: {data}")
        if data.success:
            for page_name in StorageManager.manifest_files_load_data().data["pages"]:
                if page_name not in data.data.keys():
                    logger.error(f"Page {page_name} not found in storage system ")
                    return OperationResult(
                        success=False,
                        error=ErrorData(
                            error_boolean=True,
                            error_message=f"Page {page_name} not found in storage",
                            error_code="error-page-not-found"
                        )
                    )
            for page , data in data.data.items():
                result = self.task_app.import_category_data(page,data)
                logger.info(f"Task {data} loaded")
                logger.info(f"Task {data} result: {result}")
        
        else:
            logger.error(data.error.error_message)
            return data
        logger.info("Storage loaded")
        return OperationResult(
            success=True,
        )
    
    def save_storage(self):
        for page_changed in self.task_app.changed_pages:
            if page_changed.type_change == "add":
                storage_result = StorageManager.create_page(page_changed.page)

            elif page_changed.type_change == "remove":
                storage_result = StorageManager.delete_page(page_changed.page)
            elif page_changed.type_change == "modify":

                data = self.task_app.serialize_tasksofpage(page_changed.page)
                storage_result = StorageManager.save_page(page_changed.page,data)
            else:
                self.task_app.changed_pages = []
                logger.warning(f"Unknown page type change: {page_changed.type_change}")
                return OperationResult(
                    success=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"Unknown page type change: {page_changed.type_change}",
                        error_code="error-unknown-page-type-change"
                    )
                )
            if not storage_result.success:
                self.task_app.changed_pages = []
                return storage_result
        data_list = []
        self.task_app.changed_pages = []
        for page in self.task_app.taskpage:
            data_list.append(page.category)
        StorageManager.manifest_files_save_data(data_list)
        return OperationResult(
            success=True,
        )
            
        
        
           