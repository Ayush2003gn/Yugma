from core.models.task import Task
import datetime
import logging
import uuid
logger = logging.getLogger(__name__)

def datetime_now():
    return datetime.datetime.now()

class TaskList:
    def __init__(self, category):
        self.category = category 
        self.tasklist = []
        self.ui_id_count = 0
        self.changed = False

    #----------------------------------Create task---------------------------------------------
    def add_task(self,task):
        internal_id = str(uuid.uuid4())
        ui_id = self.ui_id_generator()

        newtask = Task(task, internal_id, ui_id, datetime_now(), datetime_now())
        
        self.tasklist.append(newtask)
        self.changed = True

        logger.info(f"{self.category} page:task added [{task}]")
        return {"success": True,"message": f"{self.category} page:task added [{newtask.task}]","task": newtask}
    
    def importing_task(self,task, internal_id, created_date, modified_date, priority, done):
        ui_id = self.ui_id_generator()
        newtask = Task(task, internal_id, ui_id, datetime.datetime.fromisoformat(created_date), datetime.datetime.fromisoformat(modified_date), priority, done)
        self.tasklist.append(newtask)

    def ui_id_generator(self):
        self.ui_id_count += 1
        return self.ui_id_count
    
    def internal_id_find(self,internal_id):
        for task in self.tasklist:
            if task.internal_id == internal_id:
                return task
            
        return None
    
    #----------------------------------Remove task---------------------------------------------
    def remove_task(self, internal_id):
        task = self.id_find(internal_id)
        if task:
            self.tasklist.remove(task)
            logger.info(f"{self.category} page: Id : {internal_id} is removed")
            self.changed = True
            return {"success": True,"message":f"Id : {internal_id} is removed"}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False,"message":f"Id not found in {self.category} page"}
    
    #----------------------------------Update task---------------------------------------------    
    def update_task(self, internal_id, task):
        task_found = self.id_find(internal_id)
        if task_found == None:
            logger.warning(f"{self.category} page: Task ID not found: {internal_id}")
            return {"success": False,"message":f"Id not found in {self.category} page" }
        
        else:
            task_found.correction(task,datetime_now())
            logger.info(f"{self.category} page: Task updated: id={internal_id}, new_value='{task}'")
            self.changed = True
            return {"success": True,"message":f"successfully Update task of id {internal_id} in {self.category} page","task":task_found}
    
    def mark_done(self, internal_id):
        task_found = self.id_find(internal_id)
        if task_found == None:
            logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
            return {"success": False,"message":f"Id not found in {self.category} page"}
        else:
            task_found.mark_done(datetime_now())
            logger.info(f"{self.category} page: Task status updated: {internal_id} ")
            self.changed = True
            return {"success": True,"message":f"successfully Update status of id {internal_id} in {self.category} page","task":task_found}
        
    def mark_undone(self,internal_id):
        task_found = self.id_find(internal_id)
        if task_found == None:
            logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
            return {"success": False,"message":f"Id not found in {self.category} page"}
        else:
            task_found.mark_undone(datetime_now())
            logger.info(f"{self.category} page: Task status updated: {internal_id}")
            self.changed = True
            return {"success": True,"message":f"successfully Update status of id {internal_id} in {self.category} page","task":task_found}
    
    def high_priority_task(self,internal_id):
        task_found = self.id_find(internal_id)
        if task_found == None:
            logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
            return {"success": False,"message":f"Id not found in {self.category} page"}
        else:
            task_found.priority_high(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {internal_id} ")
            self.changed = True
            return {"success": True,"message":f"successfully Update priority level of id {internal_id} in {self.category} page","task":task_found}
        
    def Normal_priority_task(self,internal_id):
        task_found = self.id_find(internal_id)
        if task_found == None:
            logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
            return {"success": False,"message":"Id not found"}
        else:
            task_found.priority_normal(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {internal_id}")
            self.changed = True
            return {"success": True,"message":f"successfully Update priority level of id {internal_id} in {self.category} page","task":task_found}
        
    def low_priority_task(self,internal_id):
        task_found = self.id_find(internal_id)
        if task_found == None:
            logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
            return {"success": False,"message":"Id not found"}
        else:
            task_found.priority_low(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {internal_id} ")
            self.changed = True
            return {"success": True,"message":f"successfully Update priority level of id {internal_id} in {self.category} page","task":task_found}
    
    #----------------------------------Display task---------------------------------------------
    def display_all(self):
        print()
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            return "No tasks available"
        logger.debug(f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ")
        return self.tasklist



    def display_bymonths(self,months,year):
        print()
        print("# ",self.category)
        count = 0
        no_task = True
        if not self.tasklist:
            print("No tasks available")
            logger.warning(f"{self.category} page: No tasks available")
            return
        for task in self.tasklist:
            if task.created_date.strftime("%B").lower() == months.lower() and task.created_date.year == year:
                print(task)
                count += 1
                
            else:
                continue
        if count == 0:
            print("No tasks available")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")

    def display_byweek(self,week,year):
        print()
        print("# ",self.category)
        count = 0
        if not self.tasklist:
            print(f"{self.category} page: No tasks available in {self.category} page")
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
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")    
    
    def display_byyear(self,year):
        print()
        print("# ",self.category)
        count = 0
        if not self.tasklist:
            print(f"{self.category} page: No tasks available in {self.category} page")
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
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")

    def display_byday(self,day,months,year):
        print()
        print("# ",self.category)
        count = 0
        if not self.tasklist:
            print(f"{self.category} page: No tasks available in {self.category} page")
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
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")

    def percent_done(self):
        count_done = 0
        for task in self.tasklist:
            if task.done:
                count_done += 1
        try:
            return (count_done/len(self.tasklist))*100
        except ZeroDivisionError:
            return 0
    
    def completion_bar(self):
        percent_inten = int(self.percent_done()/10.0)
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
        logger.debug(f"{self.category} page: Prepared {len(json_list)} tasks for saving")
        return json_list
