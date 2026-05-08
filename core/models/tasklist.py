from core.models.task import Task
import datetime
import logging
logger = logging.getLogger(__name__)

def datetime_now():
    return datetime.datetime.now()

class TaskList:
    def __init__(self, category):
        self.category = category 
        self.tasklist = []
    #----------------------------------Create task---------------------------------------------
    def add_task(self,task):
        id = datetime.datetime.now().strftime("%d%m%y%H%M%S%f")
        newtask = Task(task,id,datetime_now(),datetime_now())
        self.tasklist.append(newtask)
        logger.info(f"{self.category}:task added [{task}]")
        return newtask
    
    def id_find(self,id):
        for task in self.tasklist:
            if task.id == id:
                return task
        return None
    
    #----------------------------------Remove task---------------------------------------------
    def remove_task(self, id):
        task = self.id_find(id)
        if task:
            self.tasklist.remove(task)
            logger.info(f"{self.category}: Id : {id} is removed")
            return f"Id : {id} is removed"
        logger.warning(f"{self.category}: Task ID not found: {id} ")
        return "Id not found in {self.category} page"
    
    #----------------------------------Update task---------------------------------------------    
    def update_task(self,id,task):
        task_found = self.id_find(id)
        if task_found == None:
            logger.warning(f"{self.category}: Task ID not found: {id}")
            return "Id not found in {self.category} page"
        else:
            task_found.correction(task,datetime_now())
            logger.info(f"{self.category}: Task updated: id={id}, new_value='{task}'")
            self.changed = True
            return f"successfully Update task of id {id} in {self.category} page"
    
    def mark_done(self,id):
        task_found = self.id_find(id)
        if task_found == None:
            logger.warning(f"{self.category}: Task ID not found: {id} ")
            return "Id not found in {self.category} page"
        else:
            task_found.mark_done(datetime_now())
            logger.info(f"{self.category}: Task status updated: {id} ")
            self.changed = True
            return f"successfully Update status of id {id} in {self.category} page"
        
    def mark_undone(self,id):
        task_found = self.id_find(id)
        if task_found == None:
            logger.warning(f"{self.category}: Task ID not found: {id} ")
            return "Id not found in {self.category} page"
        else:
            task_found.mark_undone(datetime_now())
            logger.info(f"{self.category}: Task status updated: {id}")
            self.changed = True
            return f"successfully Update status of id {id} in {self.category} page"
    
    def highpriority_task(self,id):
        task_found = self.id_find(id)
        if task_found == None:
            logger.warning(f"{self.category}: Task ID not found: {id} ")
            return "Id not found in {self.category} page"
        else:
            task_found.priority_high(datetime_now())
            logger.info(f"{self.category}: Task priority level updated: {id} ")
            self.changed = True
            return f"successfully Update priority level of id {id} in {self.category} page"
        
    def Normalpriority_task(self,id):
        task_found = self.id_find(id)
        if task_found == None:
            logger.warning(f"{self.category}: Task ID not found: {id} ")
            return "Id not found"
        else:
            task_found.priority_normal(datetime_now())
            logger.info(f"{self.category}: Task priority level updated: {id}")
            self.changed = True
            return f"successfully Update priority level of id {id} in {self.category} page"
        
    def lowpriority_task(self,id):
        task_found = self.id_find(id)
        if task_found == None:
            logger.warning(f"{self.category}: Task ID not found: {id} ")
            return "Id not found"
        else:
            task_found.priority_low(datetime_now())
            logger.info(f"{self.category}: Task priority level updated: {id} ")
            self.changed = True
            return f"successfully Update priority level of id {id} in {self.category} page"
    
    #----------------------------------Display task---------------------------------------------
    def display_all(self):
        print(self.category)
        if not self.tasklist:
            print("No tasks available")
            logger.warning("{self.category}: No tasks available ")
            return
        for task in self.tasklist:
            print(task)
        logger.debug(f"{self.category}: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ")

    def display_bymonths(self,months,year):
        
        print(self.category)
        count = 0
        no_task = True
        if not self.tasklist:
            print("No tasks available")
            logger.warning(f"{self.category}: No tasks available")
            return
        for task in self.tasklist:
            if task.created_date.strftime("%B").lower() == months.lower() and task.created_date.year == year:
                print(task)
                count += 1
                
            else:
                continue
        if count == 0:
            print("No tasks available")
        logger.debug(f"{self.category}: Displayed {count}/{len(self.tasklist)} tasks ")

    def display_byweek(self,week,year):
        print(self.category)
        count = 0
        if not self.tasklist:
            print(f"{self.category}: No tasks available in {self.category} page")
            logger.warning("No tasks available in {self.category} page")
            return
        for task in self.tasklist:
            if int(task.created_date.isocalendar().week) == week and task.created_date.year == year:
                print(task)
                count += 1
            else:
                continue
        if count == 0:
            print("No tasks available")
        logger.debug(f"{self.category}: Displayed {count}/{len(self.tasklist)} tasks ")    
    
    def display_byyear(self,year):
        print(self.category)
        count = 0
        if not self.tasklist:
            print(f"{self.category}: No tasks available in {self.category} page")
            logger.warning("No tasks available in {self.category} page")
            return
        for task in self.tasklist:
            if task.created_date.year == year:
                print(task)
                count += 1
            else:
                continue
        if count == 0:
            print("No tasks available")
        logger.debug(f"{self.category}: Displayed {count}/{len(self.tasklist)} tasks ")

    def display_byday(self,day,months,year):
        print(self.category)
        count = 0
        if not self.tasklist:
            print(f"{self.category}: No tasks available in {self.category} page")
            logger.warning("No tasks available in {self.category} page")
            return
        for task in self.tasklist:
            if task.created_date.day == day and task.created_date.month == months and task.created_date.year == year:
                print(task)
                count += 1
            else:
                continue
        if count == 0:
            print("No tasks available")
        logger.debug(f"{self.category}: Displayed {count}/{len(self.tasklist)} tasks ")

    def percent_done(self):
        count_done = 0
        for task in self.tasklist:
            if task.done:
                count_done += 1
        return (count_done/len(self.tasklist))*100
    
    def completion_bar(self):
        percent_inten = int(self.percent_done/10)
        bar = ""
        for i in range(percent_inten):
            bar += "="
        for i in range(10-percent_inten):
            bar += " "
        return self.category+" page: ["+bar+"]"
    
    #----------------------------------------File saving proccess---------------------------------
    def serialize_tasks(self):
        json_list = []
        for task in self.tasklist:
            jlist = task.to_dict()
            json_list.append(jlist)
        logger.debug(f"{self.category}: Prepared {len(json_list)} tasks for saving")
        return json_list
