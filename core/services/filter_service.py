from core.contracts.filter_return import FilterReturn
class FilterService:
    def __init__(self,taskapp):
        self.taskapp = taskapp
    
    def filter(self,task=None,done=None,priority=None,tag=None,page_id=None,group=None,iid=None,uid=None,date_created=None,date_modified=None):
        if type(self.taskapp) != classmethod:
            raise TypeError("taskapp must be an instance of TaskApp class")
        
        