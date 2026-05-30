from core.models.tasklist import TaskList
import logging
from core.contracts.error_data import ErrorData
from core.contracts.operation_result import OperationResult
from dataclasses import dataclass
logger = logging.getLogger(__name__)

@dataclass
class PageChanged:
    page:TaskList
    type_change:str = "modify" #"add"|"remove"|"modify"

class TaskPage:
    def __init__(self):
        self.taskpage = []
        self.default = None
        self.changed_pages = []

    #-------------------------------------Changes in Page------------------------------------------
    def add_page(self,category):
        if self.taskpage:
            for page in self.taskpage:
                if page.category.lower() == category.lower():
                    logger.warning(f"Category:{category} is alreay exist")
                    return OperationResult(
                        success=False,
                        data=None,
                        error=ErrorData(
                            error_boolean=True,
                            error_message=f"Category:{category} is alreay exist",
                            error_code="error-category-already-exist"
                        )
                    )
                
        newpage = TaskList(category)
        self.taskpage.append(newpage)
        page_changed = PageChanged(page=newpage.category,type_change="add")
        self.changed_pages.append(page_changed)

        return OperationResult(
            success=True,
            message=f"Category:{category} is added",
            data=newpage,
        )
    def resolve_uid(self, uid, category = None):
        if category is None:
            page = self.default
        else:
            page_dict = self.category_finder(category)
            if page_dict.success == False:
                logger.warning(f"Page Category not found: {category}")
                return OperationResult(
                    success=False,
                    data=None,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"Page Category not found: {category}",
                        error_code="error-category-not-found"
                    )
                )
            page = page_dict.data
            uid_result = page.resolve_uid(uid)
        return uid_result
    
    def category_finder(self,category):
        for page in self.taskpage:
            if page.category.lower() == category.lower():
                return OperationResult(
                    success=True,
                    message=f"Category:{category} is found",
                    data=page
                )
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Category:{category} is not found",
                error_code="error-category-not-found"
            )
        )
    
    def remove_page(self,category):
        page = self.category_finder(category)

        if page.success:
            
            if self.default == page.data:

                self.default = None
                page_changed = PageChanged(page=page.data.category,type_change="remove")
                self.changed_pages.append(page_changed)

            self.taskpage.remove(page.data)
            logger.info(f" Category : {category} is removed")

            return OperationResult(
                success=True,
                message=f"Category : {category} is removed",
                data=None
            )
        
        logger.warning(f"Page Category not found: {category}")
        return page

    def set_default(self,category):
        page = self.category_finder(category)
        if page.success:
            self.default = page.data
            logger.info(f" Category : {category} is set as default")
            return OperationResult(
                success=True,
                message=f"Category : {category} is set as default",
                data=page.data
            )
        logger.warning(f"Page Category not found: {category}")
        return page
    
    #----------------------------------Change in task-------------------------------------------
    def _execute_page_method(self,action,*args,category):
        if category is None:
            
            if self.default is None:

                logger.warning("Not set default page or mention page")
                return OperationResult(
                    success=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message="Not set default page or mention page",
                        error_code="error-default-page-not-set"
                    )
                )

            page = self.default
        else:
            page_dict = self.category_finder(category)

            if page_dict.success == False:

                logger.warning(f"Page Category not found: {category}")
                return page_dict
            
            page = page_dict.data
        if "display" not in action:
            page_changed = PageChanged(page=page.category,type_change="modify")
            self.changed_pages.append(page_changed)

        method = getattr(page, action)
        method(*args)

        return OperationResult(
            success=True,
            message="Sccessfully executed action",
            data=page
        )

    #----------------------------------Create task---------------------------------------------
    def add_task(self,task,category = None):
        return self._execute_page_method(
        "add_task_iid",
        task,
        category=category)
    
    #----------------------------------Remove task---------------------------------------------
    def remove_task(self, iid,category = None):
        return self._execute_page_method(
            "remove_task_iid",
            iid,
            category=category
        )
    
    #----------------------------------Update task---------------------------------------------    
    def update_task(self,iid,task,category = None):
        return self._execute_page_method(
            "update_task_iid",
            iid,
            task,
            category=category
        )
    
    def mark_done(self,iid,category = None):
        return self._execute_page_method(
            "mark_done_iid",
            iid,
            category=category
        )

    def mark_undone(self,iid,category = None):
        return self._execute_page_method(
            "mark_undone_iid",
            iid,
            category=category
        )

    def high_priority_task(self,iid,category = None):
        return self._execute_page_method(
            "high_priority_task_iid",
            iid,
            category=category
        )

    def medium_priority_task(self,iid,category = None):
        return self._execute_page_method(
            "medium_priority_task_iid",
            iid,
            category=category
        )

    def low_priority_task(self,iid,category = None):
        return self._execute_page_method(
            "low_priority_task_iid",
            iid,
            category=category
        )
    
    #----------------------------------Display task---------------------------------------------
    def _execute_page_display(self,type_display,*args,category = None):
        display = []
        if category == None:
            for page in self.taskpage:
                method = getattr(page, type_display)
                method_data = method(*args)
                display.append(method_data)
            return OperationResult(
                success=True,
                message="Ready for display",
                data=display
            )
        else:
            page_dict = self.category_finder(category)
            if page_dict.success:
                page = page_dict.data
                method = getattr(page, type_display)
                method_data = method(*args)
                display.append(method_data)
                return OperationResult(
                    success=True,
                    message="Ready for display",
                    data=display
                )
        logger.warning(f"Page Category not found: {category}")
        return page
            

    #-------------------------------------------------------------------------------------------
    def display_all(self,category = None):
        return self._execute_page_display(
            "display_all",
            category=category
            )
        
    
    def display_by_months(self,months,year,category = None):
        return self._execute_page_display(
            "display_by_months",
            months,
            year,
            category=category
            )
        
    
    def display_by_week(self,week,year,category = None):
        return self._execute_page_display(
            "display_by_week",
            week,
            year,
            category=category
            )
    
    def display_by_day(self,day,months,year,category = None):
        return self._execute_page_display(
            "display_by_day",
            day,
            months,
            year,
            category=category
            )
    
    def display_by_year(self,year,category = None):
        return self._execute_page_display(
            "display_by_year",
            year,
            category=category
            )

    def display_analysis(self):
        display = []
        if self.taskpage:
            for page in self.taskpage:
                display.append(page.completion_bar())
            return OperationResult(
                success=True,
                message="Ready for display",
                data=display
            )
        else:
            display.append("No pages are there")
            return OperationResult(
                success=True,
                message="Ready for display",
                data=display
            )

    def display_done(self,category):
        return self._execute_page_display(
            "display_by_done",
            category=category
        )
    
    def display_pending(self,category):
        return self._execute_page_display(
            "display_by_pending",
            category=category
        )

#-----------------------------Data handling for persistence--------------------------------------

    def category_datapath_dict(self):
        category_list = {}
        if self.taskpage:
            for page in self.taskpage:
                category = page.category
                category_list[category + "_data.json"] = category
            return category_list
        return {}

    def serialize_tasksofpage(self,category):
        page = self.category_finder(category)
        if page.success:
            return page.data.serialize_dict_of_tasks()

    def import_category_data(self,category,data_list):
        page = self.add_page(category)
        if page.success:
            page = page.data
            for data in data_list:
                page.importing_task(
                    task = data["Task"],
                    iid = data["iid"],
                    created_date = data["Created Date"],
                    modified_date = data["Modified Date"],
                    priority = data["Priority"],
                    done = data["Done"]
                )
            return OperationResult(
                success=True,
                data=page
            )
