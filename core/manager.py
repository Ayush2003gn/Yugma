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
    
def import_data():
    dict_file = storage.pathcategory_finder()
    print(dict_file)
    def create_category():
        print("create_category active")
        for category,filepath in dict_file.items():
            Todo.add_page(category)
            data = storage.json_to_py(filepath)
            print(category,"data",data)
            imortingdata_to_category(category,data)
        
    def imortingdata_to_category(category,data):
        print("imortingdata_to_category active")
        for ftask in data:
            Todo.category_finder(category).importing_task(ftask["Task"], ftask["Id"], ftask["Date Created"], ftask["Date Modified"], ftask["Priority"], ftask["Done"])
        
    create_category()


