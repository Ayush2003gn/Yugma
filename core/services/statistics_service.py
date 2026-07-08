from core.services.filter_service import FilterService
class StatisticsService:
    #option 1
    def __init__(self,taskapp):
        self.taskapp = taskapp
        self.tasks = self.taskapp.get_all_tasks()
        self._filter = FilterService(taskapp)
        
    def total_tasks(self):
        return len(self.taskapp.get_all_tasks())
    
    def total_done_tasks(self):
        return sum(
            1 for task in self.taskapp.get_all_tasks()
            if task.done
        )

    def total_pending_tasks(self):
        return sum(
            1 for task in self.taskapp.get_all_tasks()
            if task.done == False
        )
    
    def total_tasks_by_priority(self,priority):
        count = 0
        for page in self.taskapp.taskapp:
            for task in self.taskapp.get_all_tasks():
                if task.priority == priority:
                    count += 1
        return count

    def total_tasks_by_tag(self,tags):
        count = 0
        for task in self.taskapp.get_all_tasks():
            if tags in task.tags:
                count += 1
        return count
    
    def total_tasks_by_page(self,page_id):
        count = 0
        for task in self.taskapp.get_all_tasks():
            if task.page_id == page_id:
                count += 1
        return count
    
    def total_tasks_done_by_page(self,page_id):
        count = 0
        for task in self.taskapp.get_all_tasks():
            if task.page_id == page_id:
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
#option 2
    def Statistics(task=None,done=None,priority=None,tag=None,tag_type=None,page_id=None,iid=None,uid=None,date_created=None,date_modified=None):
        filter = FilterService(task,done,priority,tag,tag_type,page_id,iid,uid,date_created,date_modified)
        no_tasks = len(filter.filter().data)
        return no_tasks