from core.contracts.filter_return import FilterReturn
class FilterService:
    def __init__(self,taskapp):
        self.taskapp = taskapp
    
    def filter(self,task=None,done=None,priority=None,tag=None,tag_type=None,page_id=None,iid=None,uid=None,date_created=None,date_modified=None):
        all_tasks = self.taskapp.get_all_tasks()
        filtered_tasks = all_tasks
        if task is not None:
            filtered_tasks = [t for t in filtered_tasks if t.task == task]

        if done is not None:
            filtered_tasks = [t for t in filtered_tasks if t.done == done]

        if priority is not None:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority]

        if tag is not None:
            tag_filtered_tasks = []
            if isinstance(tag, list):
                if tag_type is None:
                    tag_type = "any"
                search_tags = tag
                if tag_type == "any":
                    for t in filtered_tasks:
                        if any(search_tag in t.tags for search_tag in search_tags):
                            tag_filtered_tasks.append(t)
                elif tag_type == "all":
                    for t in filtered_tasks:
                        if all(search_tag in t.tags for search_tag in search_tags):
                            tag_filtered_tasks.append(t)
                else:
                    raise ValueError("tag_type should be 'any' or 'all'")

                filtered_tasks = tag_filtered_tasks
            else:
                raise ValueError("tag should be a list")
   
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
        
