from core.models.taskpage import TaskPage
import logging
from core.contracts.error_data import ErrorData
from core.contracts.operation_result import OperationResult
from dataclasses import dataclass
logger = logging.getLogger(__name__)

@dataclass
class PageChanged:
    page:str
    type_change:str = "modify" #"add"|"remove"|"modify"

class TaskApp:
    def __init__(self):
        self.taskapp = []
        self.default = None
        self.changed_pages = []

    #-------------------------------------Changes in Page------------------------------------------
    def add_page(self,category):
        if self.taskapp:
            for page in self.taskapp:
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
                
        newpage = TaskPage(category)
        self.taskapp.append(newpage)
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
        for page in self.taskapp:
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

            self.taskapp.remove(page.data)
            logger.info(f" Category : {category} is removed")
            page_changed = PageChanged(page=page.data.category,type_change="remove")
            self.changed_pages.append(page_changed)
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
            
        method = getattr(page, action)
        result = method(*args)
        if result.success and "display" not in action:
            self.changed_pages.append(
                PageChanged(
                    page=page.category,
                    type_change="modify"
                )
            )
        return result

    #----------------------------------Create task---------------------------------------------
    def add_task(self,task,category = None):
        return self._execute_page_method(
        "add_task",
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
    
    def add_tag(self,iid,tag,category = None):
        return self._execute_page_method(
            "add_tag_iid",
            iid,
            tag,
            category=category
        )
    
    def remove_tag(self,iid,tag,category = None):
        return self._execute_page_method(
            "remove_tag_iid",
            iid,
            tag,
            category=category
        )
    
    def update_description(self,iid,description,category = None):
        return self._execute_page_method(
            "update_discription_iid",
            iid,
            description,
            category=category
        )
    
    def update_group(self,group,category = None):
        return self._execute_page_method(
            "update_group",
            group,
            category=category
        )

    #----------------------------------Display task---------------------------------------------
    def _execute_page_display(self,type_display,*args,category = None):
        logger.info(f"Displaying {type_display}")
        display = []
        if category == None:
            logger.info("Displaying all pages")
            for page in self.taskapp:
                method = getattr(page, type_display)
                method_data = method(*args)
                display.append(method_data)
            logger.info(f"Displayed {len(self.taskapp)} pages")
            return OperationResult(
                success=True,
                message="Ready for display",
                data=display
            )
        else:
            logger.info(f"Displaying {category} page")
            page_dict = self.category_finder(category)
            logger.info(f"message:{page_dict.message} and error_message:{page_dict.error.error_message}")
            if page_dict.success:
                page = page_dict.data

                method = getattr(page, type_display)
                method_data = method(*args)

                logger.info(f"message:{method_data.message} and error_message:{method_data.error.error_message}")
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
        if self.taskapp:
            for page in self.taskapp:
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
        if self.taskapp:
            for page in self.taskapp:
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
        self.changed_pages = []
        if page.success:
            page = page.data
            for data in data_list:
                page.importing_task(
                    task = data["Task"],
                    iid = data["iid"],
                    created_date = data["Date Created"],
                    modified_date = data["Date Modified"],
                    priority = data["Priority"],
                    done = data["Done"]
                )
            return OperationResult(
                success=True,
                data=page
            )

    def reset_changed_pages(self):
        self.changed_pages = []