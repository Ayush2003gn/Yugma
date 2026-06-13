import logging
logger = logging.getLogger(__name__)
class Task:
    def __init__(self, task, iid, uid, created_date, modified_date, priority = "Medium", done = False , tags = [], description = ""):
        self.task = task
        self.iid = iid
        self.uid = uid 
        self.created_date = created_date
        self.modified_date = modified_date
        self.priority = priority #1 = high | 2 = medium | 3 = low
        self.done = done
        self.description = description

        if tags is None:
            tags = []
        elif not isinstance(tags, list):
            logger.warning(f"Tags should be a list, got {type(tags)}. Converting to list.")
            tags = [tags]
        elif not all(isinstance(tag, str) for tag in tags):
            logger.warning(f"All tags should be strings. Converting non-string tags to strings.")
            tags = [str(tag) for tag in tags]
        else:            
            logger.info(f"Tags are valid: {tags}")
        
        self.tags = tags
        
    def correction(self, task, modified_date):
        self.task = task
        self.modified_date = modified_date

    #status
    def mark_done(self, modified_date):
        self.done = True
        self.modified_date = modified_date

    def mark_undone(self, modified_date):
        self.done = False
        self.modified_date = modified_date

    #priority
    def priority_high(self, modified_date):
        self.priority = "High"
        self.modified_date = modified_date

    def priority_medium(self, modified_date):
        self.priority = "Medium"
        self.modified_date = modified_date

    def priority_low(self, modified_date):
        self.priority = "Low"
        self.modified_date = modified_date

    def add_tags(self, tags, modified_date):
        if tags is None:
            tags = []
        elif not isinstance(tags, list):
            logger.warning(f"Tags should be a list, got {type(tags)}. Converting to list.")
            tags = [tags]
        elif not all(isinstance(tag, str) for tag in tags):
            logger.warning(f"All tags should be strings. Converting non-string tags to strings.")
            tags = [str(tag) for tag in tags]
        else:            
            logger.info(f"Tags are valid: {tags}")
        self.tags.extend(tags)
        self.modified_date = modified_date
    
    def remove_tags(self, tags, modified_date):
        self.tags = [tag for tag in self.tags if tag not in tags]
        self.modified_date = modified_date
    
    def update_description(self, description, modified_date):
        self.description = description
        self.modified_date = modified_date

    
    #file representation

    def to_dict(self):
        return {
            "iid" : self.iid, 
            "uid" : self.uid,
            "task" : self.task, 
            "done" : self.done,
            "date_created":self.created_date.isoformat(), 
            "date_modified":self.modified_date.isoformat(), 
            "priority":self.priority,
            "description": self.description,
            "tags": self.tags
        }
    # display of task

    def __str__(self):
        is_done = "√" if self.done else "x"
        return f"{self.iid} ||| {self.uid} || {is_done} | {self.task} | {self.priority}"
