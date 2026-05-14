from core.models.tasklist import TaskList
import logging
logger = logging.getLogger(__name__)

class TaskPage:
    def __init__(self):
        self.taskpage = []
        self.default = None

    #-------------------------------------Changes in Page------------------------------------------
    def add_page(self,category):
        if self.taskpage:
            for page in self.taskpage:
                if page.category.lower() == category.lower():
                    logger.warning(f"Category:{category} is alreay exist")
                    return {"success": False, "message":f"Category:{category} is alreay exist", "data":None}
        
        newpage = self.taskpage.append(TaskList(category))
        return {"success": True, "message":f"Page is added of category {category}", "data":newpage}
        
    def category_finder(self,category):
        for page in self.taskpage:
            if page.category == category:
                return {"success": True, "message":f"Page Category found: {category}", "data":page}
        return {"success": False, "message":f"Page Category not found: {category}", "data":None}
    
    def remove_page(self,category):
        page = self.category_finder(category)
        if page["success"] :
            self.taskpage.remove(page)
            logger.info(f" Category : {category} is removed")
            return {"success": True, "message":f"Category : {category} is removed","data":None}
        logger.warning(f"Page Category not found: {category}")
        return page

    def set_default(self,category):
        page = self.category_finder(category)
        if page:
            self.default = page
            logger.info(f" Category : {category} is set as default")
            return {"success": True, "message":f"Category : {category} is set as default","data":None}
        logger.warning(f"Page Category not found: {category}")
        return page
    
    #----------------------------------Change in task-------------------------------------------
    def _execute_page_method(self,action,*args,category):
        if category is None:
            
            if self.default is None:
                logger.warning("Not set default page or mention page")
                return {"success": False, "message": "Not set default page or mention page", "data": None}

            page = self.default
        else:
            page = self.category_finder(category)
            if page["success"] == False:
                logger.warning(f"Page Category not found: {category}")
                return page
            
        method = getattr(page, action)
        return method(*args)

    #----------------------------------Create task---------------------------------------------
    def add_task(self,task,category = None):
        return self._execute_page_method(
        "add_task",
        task,
        category=category)
    
    #----------------------------------Remove task---------------------------------------------
    def remove_task(self, id,category = None):
        return self._execute_page_method(
            "remove_task",
            id,
            category=category
        )
    
    #----------------------------------Update task---------------------------------------------    
    def update_task(self,id,task,category = None):
        return self._execute_page_method(
            "update_task",
            id,
            task,
            category=category
        )
    
    def mark_done(self,id,category = None):
        return self._execute_page_method(
            "mark_done",
            id,
            category=category
        )

    def mark_undone(self,id,category = None):
        return self._execute_page_method(
            "mark_undone",
            id,
            category=category
        )

    def high_priority_task(self,id,category = None):
        return self._execute_page_method(
            "high_priority_task",
            id,
            category=category
        )

    def Normal_priority_task(self,id,category = None):
        return self._execute_page_method(
            "Normal_priority_task",
            id,
            category=category
        )

    def low_priority_task(self,id,category = None):
        return self._execute_page_method(
            "low_priority_task",
            id,
            category=category
        )
    
    #----------------------------------Display task---------------------------------------------
    def _execute_page_display(self,type_display,*args,category = "*"):
        display = []
        if category == "*":
            for page in self.taskpage:
                method = getattr(page, type_display)
                method_data = method(*args)
                display.append(method_data)
            return {"success":True, "message":"Ready for display","data":display}
        else:
            page = self.category_finder(category)
            if page["success"]:
                method = getattr(page, type_display)
                method_data = method(*args)
                display.append(method_data)
                return {"success":True, "message":"Ready for display","data":display}
        logger.warning(f"Page Category not found: {category}")
        return page
            

    #-------------------------------------------------------------------------------------------
    def display_all(self,category = "*"):
        return self._execute_page_display(
            "display_all",
            category
            )
        
    
    def display_by_months(self,months,year,category= "*"):
        return self._execute_page_display(
            "display_by_months",
            months,
            year,
            category
            )
        
    
    def display_by_week(self,week,year,category= "*"):
        return self._execute_page_display(
            "display_by_week",
            week,
            year,
            category
            )
    
    def display_by_day(self,day,months,year,category = "*"):
        return self._execute_page_display(
            "display_by_day",
            day,
            months,
            year,
            category
            )
    
    def display_by_year(self,year,category = "*"):
        return self._execute_page_display(
            "display_by_year",
            year,
            category
            )

    def display_analysis(self):
        display = []
        if self.taskpage:
            for page in self.taskpage:
                display.append(page.completion_bar())
                return {"success":True, "message":"Ready for display","data":display}
        else:
            display.append("No pages are there")
            return {"success":True, "message":"Ready for display","data":display}

    def display_done(self,category):
        return self._execute_page_display(
            "display_by_done",
            category
        )
    
    def display_pending(self,category):
        return self._execute_page_display(
            "display_by_pending",
            category
        )

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
        if page:
            return page.serialize_tasks()

