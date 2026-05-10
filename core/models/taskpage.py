from core.models.tasklist import TaskList
import logging
logger = logging.getLogger(__name__)

class TaskPage:
    def __init__(self):
        self.taskpage = []
        self.default = None

    #-------------------------------------Changes in Page------------------------------------------
    def add_page(self,category):
        if not self.taskpage:
            self.taskpage.append(TaskList(category))
            return f"Page is added of category {category}"
        else:
            for page in self.taskpage:
                if page.category.lower() == category.lower():
                    logger.warning(f"Category:{category} is alreay exist")
                    return "The given category is alreay exist"
                else:
                    self.taskpage.append(TaskList(category))
                    return f"Page is added of category {category}"
    
    def category_finder(self,category):
        for page in self.taskpage:
            if page.category == category:
                return page
        return None
    
    def remove_page(self,category):
        page = self.category_finder(category)
        if page:
            self.taskpaget.remove(page)
            logger.info(f" Category : {category} is removed")
            return f"Category : {category} is removed"
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"

    def set_default(self,category):
        page = self.category_finder(category)
        if page:
            self.default = page
            logger.info(f" Category : {category} is set as default")
            return f"Category : {category} is set as default"
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"
    
    #----------------------------------Create task---------------------------------------------
    def add_task(self,task,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.add_task(task)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.add_task(task)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"
    
    #----------------------------------Remove task---------------------------------------------
    def remove_task(self, id,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.remove_task(id)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.remove_task(id)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"
    
    #----------------------------------Update task---------------------------------------------    
    def update_task(self,id,task,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.update_task(id,task)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.update_task(id,task)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"
    
    def mark_done(self,id,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.mark_done(id)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.mark_done(id)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"

    def mark_undone(self,id,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.mark_undone(id)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.mark_undone(id)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"

    def highpriority_task(self,id,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.highpriority_task(id)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.highpriority_task(id)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"

    def Normalpriority_task(self,id,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.Normalpriority_task(id)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.Normalpriority_task(id)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"

    def lowpriority_task(self,id,category = None):
        if category == None:
            if self.default == None:
                logger.warning("Not set default page or mention page")
                return "Please set default page or mention page"
            else:
                x = self.default.lowpriority_task(id)
                return x
        else:
            page = self.category_finder(category)
        if page:
            x = page.lowpriority_task(id)
            return x
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"
    
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
        return "Category not found"
    
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
        return "Category not found"
    
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
        return "Category not found"
    
    def display_byday(self,day,months,year,category = "*"):
        if category == "*":
            for page in self.taskpage:
                page.display_day(day,months,year)
        else:
            page = self.category_finder(category)
            if page:
                page.display_byday(day,months,year)
                return
        logger.warning(f"Page Category not found: {category}")
        return "Category not found"
    
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
        return "Category not found"

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
        