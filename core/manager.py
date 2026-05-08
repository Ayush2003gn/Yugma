import logging
from core.models.taskpage import TaskPage
import core.storage as storage
logger = logging.getLogger(__name__)

Todo = TaskPage()

def command_paths():
    default = Todo.default
    if default == None:
        return "Yukta/root/-"
    else:
        return "Yukta/root/"+str(default.category)+"/-"
    
print(storage.pathcategory_finder())