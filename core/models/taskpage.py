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
                    return "The given category is alreay exist"
        
        newpage = self.taskpage.append(TaskList(category))
        return {"success": True, "message":f"Page is added of category {category}", "data":newpage}
        
    def category_finder(self,category):
        for page in self.taskpage:
            if page.category == category:
                return page
        return None
    
    def remove_page(self,category):
        page = self.category_finder(category)
        if page:
            self.taskpage.remove(page)
            logger.info(f" Category : {category} is removed")
            return f"Category : {category} is removed"
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}

    def set_default(self,category):
        page = self.category_finder(category)
        if page:
            self.default = page
            logger.info(f" Category : {category} is set as default")
            return f"Category : {category} is set as default"
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}
    
    #----------------------------------Change in task-------------------------------------------
    def _execute_page_method(self,action,*args,category):
        if category is None:
            
            if self.default is None:
                logger.warning("Not set default page or mention page")
                return {"success": False,"message": "Not set default page or mention page","task": None}

            page = self.default
        else:
            page = self.category_finder(category)
            if page is None:
                logger.warning(f"Page Category not found: {category}")
                return {"success": False,"message": "Category not found"}
            
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

    def highpriority_task(self,id,category = None):
        return self._execute_page_method(
            "highpriority_task",
            id,
            category=category
        )

    def Normalpriority_task(self,id,category = None):
        return self._execute_page_method(
            "Normalpriority_task",
            id,
            category=category
        )

    def lowpriority_task(self,id,category = None):
        return self._execute_page_method(
            "lowpriority_task",
            id,
            category=category
        )
    
    #----------------------------------Display task---------------------------------------------
    def display_all(self,category = "*"):
        if category == "*":
            for page in self.taskpage:
                page.display_all()
            return
        else:
            page = self.category_finder(category)
            if page:
                page.display_all()
                return
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}
    
    def display_bymonths(self,months,year,category= "*"):
        if category == "*":
            for page in self.taskpage:
                page.display_bymonths(months,year)
        else:
            page = self.category_finder(category)
            if page:
                page.display_bymonths(months,year)
                return
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}
    
    def display_byweek(self,week,year,category= "*"):
        if category == "*":
            for page in self.taskpage:
                page.display_byweek(week,year)
        else:
            page = self.category_finder(category)
            if page:
                page.display_byweek(week,year)
                return
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}
    
    def display_byday(self,day,months,year,category = "*"):
        if category == "*":
            for page in self.taskpage:
                page.display_byday(day,months,year)
        else:
            page = self.category_finder(category)
            if page:
                page.display_byday(day,months,year)
                return
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}
    
    def display_byyear(self,year,category = "*"):
        if category == "*":
            for page in self.taskpage:
                page.display_byyear(year)
        else:
            page = self.category_finder(category)
            if page:
                page.display_byyear(year)
                return
        logger.warning(f"Page Category not found: {category}")
        return {"success": False,"message":"Category not found"}

    def display_analysis(self):
        if self.taskpage:
            for page in self.taskpage:
                print(page.completion_bar())
        else:
            print("No pages are there")

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
        