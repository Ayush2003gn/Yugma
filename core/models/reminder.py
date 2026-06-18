from core.contracts.reminder_task_data import ReminderTaskData
class reminder:
    def __init__(self):
        self.reminder_tasks = []
        self.counter = 0
    
    def get_reminder_id(self):
        self.counter += 1
        return self.counter

    def add_reminder_task(self, iid, page_id, title, reminder_time, reminder_addition_message):
        reminder_id = self.get_reminder_id()
        new_reminder_task = ReminderTaskData(
            reminder_id = reminder_id,
            task_iid = iid,
            task_page_id = page_id,
            task_title = title,
            reminder_time = reminder_time,
            reminder_addition_message = reminder_addition_message
        )
        self.reminder_tasks.append(new_reminder_task)

    def remove_reminder_task(self, iid):
        self.reminder_tasks = [task for task in self.reminder_tasks if task.reminder_id != iid]

    def get_reminder_tasks(self):
        return self.reminder_tasks
    
    def get_reminder_task_by_id(self, reminder_id):
        for task in self.reminder_tasks:
            if task.reminder_id == reminder_id:
                return task
        return None
    
    