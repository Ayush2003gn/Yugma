from core.models.task import Task
import datetime
import logging
from core.contracts.error_data import ErrorData
from core.contracts.operation_result import OperationResult
import uuid
logger = logging.getLogger(__name__)

def datetime_now():
    return datetime.datetime.now()

class TaskList:
    def __init__(self, category):
        self.category = category 
        self.tasklist = []
        self.uid_count = 0
        self.changed = False

    def uid_generator(self):
        self.uid_count += 1
        return OperationResult(
            success = True,
            message = "uid generated",
            data = self.uid_count
        )
    
    #----------------------------------Create task---------------------------------------------
    def add_task(self,task):
        iid = str(uuid.uuid4())
        uid = self.uid_generator().data

        newtask = Task(task, iid, uid, datetime_now(), datetime_now())
        
        self.tasklist.append(newtask)
        self.changed = True

        logger.info(f"{self.category} page:task added [{task}]")
        return OperationResult(
            success = True,
            message = f"{self.category} page:task added [{task}, iid: {iid}, uid: {uid}",
            data = newtask
        )
    
    def importing_task(self,task, iid, created_date, modified_date, priority, done):
        uid = self.uid_generator().data
        newtask = Task(
            task = task,
            iid = iid,
            uid = uid,
            created_date = created_date,
            modified_date = modified_date,
            priority = priority,
            done = done
        )
        self.tasklist.append(newtask)
        return OperationResult(
            success = True,
            message = f"{self.category} page:task imorted [{task}]",
            data = newtask
        )

    def iid_find(self,iid):
        for task in self.tasklist:
            if task.iid == iid:
                return OperationResult(
                    success = True,
                    message = "Got the file",
                    data = task
                )
            
        return OperationResult(
            success = False,
            message = None,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Can't able to find internal task id {iid}",
                error_code="error-iid-not-found"
            )
        )
    
    def uid_to_iid(self,uid):
        for task in self.tasklist:
            if task.uid == uid:
                iid = task.iid
                return OperationResult(
                    success = True,
                    message = "Got the iid",
                    data = iid
                )
            
        return OperationResult(
            success = False,
            message = None,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Can't able to find internal task id {uid}",
                error_code="error-uid-not-found"
            )
        )
    #----------------------------------Remove task---------------------------------------------

    def remove_task_iid(self, iid):
        task = self.iid_find(iid)
        if task.success:

            self.tasklist.remove(task.data)
            logger.info(f"{self.category} page: Id : {iid} is removed")
            self.changed = True

            return OperationResult(
                success = True,
                message = f"{self.category} page: Id : {iid} is removed",
                data = None
            )
        
        logger.warning(f"{self.category} page: Task ID not found: {iid} ")
         
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"{self.category} page: Task ID not found: {iid} ",
                error_code="error-iid-not-found"
            )
        )
    
    #----------------------------------Update task---------------------------------------------    
    def update_task_iid(self, iid, task):
        task_found = self.iid_find(iid)

        if task_found.success:
            task_found.data.correction(task,datetime_now())

            logger.info(f"{self.category} page: Task updated: id={iid}, new_value='{task}'")

            self.changed = True
            return OperationResult(
                success = True,
                message = f"{self.category} page: Task updated: id={iid}, new_value='{task}'",
                data = task_found.data
            )
        
        logger.warning(f"{self.category} page: Task ID not found: {iid}")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"{self.category} page: Task ID not found: {iid}",
                error_code="error-iid-not-found"
            )
        )
    
    def mark_done_iid(self, iid):
        task_found = self.iid_find(iid)

        if task_found.success:

            task_found.data.mark_done(datetime_now())

            logger.info(f"{self.category} page: Task status updated: {iid} ")
            self.changed = True
            return OperationResult(
                success = True,
                message = f"successfully Update status of id {iid} in {self.category} page",
                data = task_found.data
            )
        
        logger.warning(f"{self.category} page: Task ID not found: {iid} ")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Id not found in {self.category} page",
                error_code="error-iid-not-found"
            )
        )
        
    def mark_undone_iid(self,iid):
        task_found = self.iid_find(iid)
        if task_found.success:
            task_found.data.mark_undone(datetime_now())
            logger.info(f"{self.category} page: Task status updated: {iid}")
            self.changed = True
            return OperationResult(
                success = True,
                message = f"successfully Update status of id {iid} in {self.category} page",
                data = task_found.data
            )
        logger.warning(f"{self.category} page: Task ID not found: {iid} ")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Id not found in {self.category} page",
                error_code="error-iid-not-found"
            )
        )
    def high_priority_task_iid(self,iid):
        task_found = self.iid_find(iid)
        if task_found.success:
            task_found.data.priority_high(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {iid} ")
            self.changed = True
            return OperationResult(
                success = True,
                message = f"successfully Update priority level of id {iid} in {self.category} page",
                data = task_found.data
            )
        logger.warning(f"{self.category} page: Task ID not found: {iid} ")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Id not found in {self.category} page",
                error_code="error-iid-not-found"
            )
        )

    def medium_priority_task_iid(self,iid):
        task_found = self.iid_find(iid)
        if task_found.success:
            task_found.data.priority_medium(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {iid}")
            self.changed = True
            return OperationResult(
                success = True,
                message = f"successfully Update priority level of id {iid} in {self.category} page",
                data = task_found.data
            )
                
        logger.warning(f"{self.category} page: Task ID not found: {iid} ")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Id not found in {self.category} page",
                error_code="error-iid-not-found"
            )
        )

    def low_priority_task_iid(self,iid):
        task_found = self.iid_find(iid)
        if task_found.success:
            
            task_found.data.priority_low(datetime_now())
            logger.info(f"{self.category} page: Task priority level updated: {iid} ")
            self.changed = True
            return OperationResult(
                success = True,
                message = f"successfully Update priority level of id {iid} in {self.category} page",
                data = task_found.data
            )
        logger.warning(f"{self.category} page: Task ID not found: {iid} ")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Id not found in {self.category} page",
                error_code="error-iid-not-found"
            )
        )
    #----------------------------------Display task---------------------------------------------
    def display_all(self):
        display = [f"# {self.category}"]
        if not self.tasklist:
            logger.warning("{self.category} page: No tasks available ")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            display.append(str(task))
        
        display.append("")
        
        logger.debug(f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )


    def display_by_months(self,months,year):
        display = [f"# {self.category}"]
        count = 0

        if not self.tasklist:
            logger.warning(f"{self.category} page: No tasks available")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            if task.created_date.strftime("%B").lower() == months.lower() and task.created_date.year == year:
                display.append(str(task))
                count += 1
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )


    def display_by_week(self,week,year):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning(f"{self.category} page: No tasks available")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            if int(task.created_date.isocalendar().week) == week and task.created_date.year == year:
                display.append(str(task))
                count += 1
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )   
    

    def display_by_year(self,year):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning(f"{self.category} page: No tasks available")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            if task.created_date.year == year:
                display.append(str(task))
                count += 1
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )

    def display_by_day(self,day,month,year):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning(f"{self.category} page: No tasks available")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            if task.created_date.day == day and task.created_date.month == month and task.created_date.year == year:
                display.append(str(task))
                count += 1
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )

    def display_by_done(self):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning(f"{self.category} page: No tasks available")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            if task.done == True:
                display.append(str(task))
                count += 1
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )

    def display_by_pending(self):
        display = [f"# {self.category}"]
        count = 0
        if not self.tasklist:
            logger.warning(f"{self.category} page: No tasks available")
            display.append("No tasks available")
            display.append("")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        for task in self.tasklist:
            if task.done == False :
                display.append(str(task))
                count += 1
        
        if count == 0:
            display.append(f"No tasks available out of {len(self.tasklist)} tasks")
            display.append("")
            logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
            return OperationResult(
                success = False,
                message = f"No tasks available",
                data = display
            )
        
        display.append("")
        logger.debug(f"{self.category} page: Displayed {count}/{len(self.tasklist)} tasks")
        return OperationResult(
            success=True,
            message=f"{self.category} page: Displayed {len(self.tasklist)}/{len(self.tasklist)} tasks ",
            data=display
        )


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
        percent_inten = int(self.percent_done()/20.0)
        bar = ""
        for i in range(percent_inten):
            bar += "="
        for i in range(20-percent_inten):
            bar += " "
        return OperationResult(
            success=True,
            message=None,
            data=f"{self.category} page: [{bar}]"
        )
    
    #----------------------------------------File saving proccess---------------------------------
    def serialize_dict_of_tasks(self):
        json_list = []
        for task in self.tasklist:
            jlist = task.to_dict()
            json_list.append(jlist)
        logger.debug(f"{self.category} page: Prepared {len(json_list)} tasks for saving")
        return json_list
