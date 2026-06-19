from core.contracts.filter_return import FilterReturn
class FilterService:
    def __init__(self,taskapp):
        self.taskapp = taskapp
    
    def filter(self,task=None,done=None,priority=None,tag=None,page_id=None,group=None,iid=None,uid=None,date_created=None,date_modified=None):
        all_tasks = self.taskapp.get_all_tasks()
        filtered_tasks = all_tasks
        if task is not None:
            filtered_tasks = [t for t in filtered_tasks if t.task == task]
        if done is not None:
            filtered_tasks = [t for t in filtered_tasks if t.done == done]
        if priority is not None:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority]
        if tag is not None:
            tag = tag.lower()
            tag_filtered_tasks = []
            if isinstance(tag, list):
                for ftag in tag:
                    for task in filtered_tasks:
                        if ftag == task.tag.lower():
                            tag_filtered_tasks.append(task)
                filtered_tasks = tag_filtered_tasks
   
        if page_id is not None:
            filtered_tasks = [t for t in filtered_tasks if t.page_id == page_id]
        if iid is not None:
            filtered_tasks = [t for t in filtered_tasks if t.iid == iid]
        if uid is not None:
            filtered_tasks = [t for t in filtered_tasks if t.uid == uid]
        if date_created is not None:
            filtered_tasks = [t for t in filtered_tasks if t.date_created == date_created]
        if date_modified is not None:
            filtered_tasks = [t for t in filtered_tasks if t.date_modified == date_modified]
        return FilterReturn(
            success = True,
            message = "filtering completed",
            data = filtered_tasks
        )
        
