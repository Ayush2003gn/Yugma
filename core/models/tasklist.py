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

        newtask = Task(task, internal_id, ui_id["data"], datetime_now(), datetime_now())
        
        self.tasklist.append(newtask)
        self.changed = True

        logger.info(f"{self.category} page:task added [{task}]")
        return {"success": True, "message": f"{self.category} page:task added [{newtask.task}]", "data": newtask}
    
    def importing_task(self,task, internal_id, created_date, modified_date, priority, done):
        ui_id = self.ui_id_generator()
        newtask = Task(task, internal_id, ui_id["data"], datetime.datetime.fromisoformat(created_date), datetime.datetime.fromisoformat(modified_date), priority, done)
        self.tasklist.append(newtask)
        return {"success": True, "message": f"{self.category} page:task imported [{newtask.task}]", "data": newtask}

    def ui_id_generator(self):
        self.ui_id_count += 1
        return {"success": True, "message": None, "data": self.ui_id_count}
    
    def internal_id_find(self,internal_id):
        for task in self.tasklist:
            if task.internal_id == internal_id:
                return {"success": True, "message": "Got the file", "data": task}
            
        return {"success": False, "message": "Can't able to find internal task id {internal_id}", "data": None}
    
    #----------------------------------Remove task---------------------------------------------
    def remove_task_internal_id(self, internal_id):
        task = self.internal_id_find(internal_id)
        if task["success"]:
            self.tasklist.remove(task["data"])
            logger.info(f"{self.category} page: Id : {internal_id} is removed")
            self.changed = True
            return {"success": True, "message":f"Id : {internal_id} is removed", "data":None}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False, "message":f"Id not found in {self.category} page","data" : None}
    
    #----------------------------------Update task---------------------------------------------    
    def update_task_internal_id(self, internal_id, task):
        task_found = self.internal_id_find(internal_id)
        if task_found["success"]:
            task_found["data"].correction(task,datetime_now())
            logger.info(f"{self.category} page: Task updated: id={internal_id}, new_value='{task}'")
            self.changed = True
            return {"success": True,"message":f"successfully Update task of id {internal_id} in {self.category} page","data":task_found["data"]}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id}")
        return {"success": False,"message":f"Id not found in {self.category} page", "data":None}
    
    def mark_done_internal_id(self, internal_id):
        task_found = self.internal_id_find(internal_id)
        if task_found["success"]:
            task_found["data"].mark_done(datetime_now())
            logger.info(f"{self.category} page: Task status updated: {internal_id} ")
            self.changed = True
            return {"success": True,"message":f"successfully Update status of id {internal_id} in {self.category} page","data":task_found["data"]}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False,"message":f"Id not found in {self.category} page","data": None}
        
    def mark_undone_internal_id(self,internal_id):
        task_found = self.internal_id_find(internal_id)
        if task_found["success"]:
            task_found["data"].mark_undone(datetime_now())
            logger.info(f"{self.category} page: Task status updated: {internal_id}")
            self.changed = True
            return {"success": True,"message":f"successfully Update status of id {internal_id} in {self.category} page","data":task_found["data"]}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False,"message":f"Id not found in {self.category} page","data": None}

    def high_priority_task_internal_id(self,internal_id):
        task_found = self.internal_id_find(internal_id)
        if task_found["success"]:
            task_found["data"].priority_high(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {internal_id} ")
            self.changed = True
            return {"success": True,"message":f"successfully Update priority level of id {internal_id} in {self.category} page","data":task_found["data"]}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False, "message":f"Id not found in {self.category} page", "data": None}

    def Normal_priority_task(self,internal_id):
        task_found = self.internal_id_find(internal_id)
        if task_found["success"]:
            task_found["data"].priority_normal(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {internal_id}")
            self.changed = True
            return {"success": True,"message":f"successfully Update priority level of id {internal_id} in {self.category} page","data":task_found["data"]}
        
        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False,"message":f"Id not found in {self.category} page","data": None}

    def low_priority_task_internal_id(self,internal_id):
        task_found = self.internal_id_find(internal_id)
        if task_found["success"]:
            
            task_found["data"].priority_low(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {internal_id} ")
            self.changed = True
            return {"success": True,"message":f"successfully Update priority level of id {internal_id} in {self.category} page","data":task_found["data"]}

        logger.warning(f"{self.category} page: Task ID not found: {internal_id} ")
        return {"success": False,"message":f"Id not found in {self.category} page","data": None}

    #----------------------------------Display task---------------------------------------------
    def display_all(self):
        display = [f"# {self.category}"]
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return {"success": False, "message":"No tasks available", "data": display}
        
        for task in self.tasklist:
            display.append(str(task))
        
        display.append("")
        
        logger.debug(f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ")
        return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}


    def display_by_months(self,months,year):
        display = [f"# {self.category}"]
        count = 0

        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return {"success": False, "message":"No tasks available", "data": display}
        
        for task in self.tasklist:
            if task.created_date.strftime("%B").lower() == months.lower() and task.created_date.year == year:
                display.append(str(task))
        
                count += 1
            else:
                continue
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks ")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
            return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
        return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}


    def display_by_week(self,week,year):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return {"success": False, "message":"No tasks available", "data": display}
        
        for task in self.tasklist:
            if int(task.created_date.isocalendar().week) == week and task.created_date.year == year:
                display.append(str(task))
        
                count += 1
            else:
                continue
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks ")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
            return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
        return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}   
    

    def display_by_year(self,year):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return {"success": False, "message":"No tasks available", "data": display}
        for task in self.tasklist:
            if task.created_date.year == year:
                display.append(str(task))
        
                count += 1
            else:
                continue
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks ")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
            return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
        return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}



    def display_by_done(self):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return {"success": False, "message":"No tasks available", "data": display}
        
        for task in self.tasklist:
            if task.done == True:
                display.append(str(task))

                count += 1
            else:
                continue
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks ")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
            return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
        return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}

    def display_by_pending(self):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return {"success": False, "message":"No tasks available", "data": display}
        
        for task in self.tasklist:
            if task.done == False :
                display.append(str(task))
                
                count += 1
            else:
                continue
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks ")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
            return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks ")
        return {"success": True, "message":f"Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks in {self.category} page", "data": display}


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
        return {"success": True, "message":None, "data":f"{self.category} page: ["+{bar}+"]"}
    
    #----------------------------------------File saving proccess---------------------------------
    def serialize_tasks(self):
        json_list = []
        for task in self.tasklist:
            jlist = task.to_dict()
            json_list.append(jlist)
        logger.debug(f"{self.category} page: Prepared {len(json_list)} tasks for saving")
        return {"success": True, "message":None, "data":json_list}
