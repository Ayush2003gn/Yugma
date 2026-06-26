class StatisticsService:
    def __init__(self,taskapp):
        self.taskapp = taskapp
        self.tasks = self.taskapp.get_all_tasks()
        self.page = self.taskapp.taskapp
        
    def total_tasks(self):
        return len(self.taskapp.get_all_tasks())
    
    def total_done_tasks(self):
        count = 0
        for page in self.taskapp.taskapp:
            for task in page.taskpage.tasklist:
                if task.done == True:
                    count += 1
        return count

    def total_pending_tasks(self):
        count = 0
        for page in self.taskapp.taskapp:
            for task in page.taskpage.tasklist:
                if task.done == False:
                    count += 1
        return count
    
    def total_tasks_by_priority(self,priority):
        count = 0
        for page in self.taskapp.taskapp:
            for task in page.taskpage.tasklist:
                if task.priority == priority:
                    count += 1
        return count

    def total_tasks_by_tag(self,tag):
        count = 0
        for page in self.taskapp.taskapp:
            for task in page.taskpage.tasklist:
                if task.tags == tag:
                    count += 1
        return count
    
    def total_tasks_by_page(self,page_id):
        count = 0
        for page in self.taskapp.taskapp:
            if page.page_id == page_id:
                for task in page.taskpage.tasklist:
                    count += 1
        return count
    
    def total_tasks_done_by_page(self,page_id):
        count = 0
        for page in self.taskapp.taskapp:
            if page.page_id == page_id:
                for task in page.taskpage.tasklist:
                    if task.done == True:
                        count += 1
        return count

    
    def completion_percentage(self):
        try:
            compl_per = (self.total_done_tasks() / self.total_tasks()) * 100
            return compl_per
        except ZeroDivisionError:
            return 0
    
    def completion_percentage_by_page(self,page_id):
        try:
            return (self.total_tasks_done_by_page(page_id) / self.total_tasks_by_page(page_id)) * 100

        except ZeroDivisionError:
            return 0