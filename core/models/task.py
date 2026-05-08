import logging
logger = logging.getLogger(__name__)
class Task:
    def __init__(self, task, id, created_date, modified_date, priority = 2, done = False):
        self.task = task
        self.id = id
        self.created_date = created_date
        self.modified_date = modified_date
        self.priority = priority #1 = high | 2 = Normal | 3 = low
        self.done = done
        
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
        self.priority = 1
        self.modified_date = modified_date
    def priority_normal(self, modified_date):
        self.priority = 2
        self.modified_date = modified_date
    def priority_low(self, modified_date):
        self.priority = 3
        self.modified_date = modified_date
    #file representation
    def to_dict(self):
        return {"Id" : self.id, "Task" : self.task, "Done" : self.done, "Date Created":self.created_date, "Date Modified":self.modified_date, "Priority":self.priority}
    # display of task
    def __str__(self):
        is_done = "√" if self.done else "x"
        return f"{self.created_date} | {self.id} | {is_done} | {self.task}"
