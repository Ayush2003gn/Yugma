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
    def create_category():
        for category,filepath in dict_file.items():
            Todo.add_page(category)
            data = storage.json_to_py(filepath)
            imortingdata_to_category(category,data)
        
    def imortingdata_to_category(category,data):
        for ftask in data:
            Todo.category_finder(category).importing_task(ftask["Task"], ftask["Id"], ftask["Date Created"], ftask["Date Modified"], ftask["Priority"], ftask["Done"])
        
    create_category()

def export_data():
    category_datafile_dict = Todo.category_datapath_dict()

    def create_path():
        category_path_dict = {}
        for filename,category in category_datafile_dict.items():
            path = storage.path_make(filename)
            category_path_dict[path] = category
        return category_path_dict
    
    def ensure_filespath(path_dict):
        if path_dict:
            for path in path_dict:
                storage.ensure_datafile(path)
    
    def exporting_data_infiles(path_dict):
        if path_dict:
            for path , category in path_dict.items():
                data = Todo.serialize_tasksofpage(category)
                storage.exporting_data(path , data)
    
    path_dict = create_path()
    ensure_filespath(path_dict)
    exporting_data_infiles(path_dict)

def cmd_page(arg):
    count = 0
    category = None
    while count < len(arg):
        current = arg[count]
        if current in ["add", "-p"]:
            if count + 1 >= len(arg):
                print("Category missing")
                break

            category = arg[count + 1]
            print(Todo.add_page(category))
            count += 2
            continue

        elif current in ["set-default", "--sd"]:

            if current == "set-default":

                if count + 1 >= len(arg):
                    print("Category missing")
                    break

                category = arg[count + 1]
                print(Todo.set_default(category))
                count += 2
                continue

            elif current == "--sd":

                if category is None:
                    print("No category entered")
                    break

                print(Todo.set_default(category))
                count += 1
                continue

        elif current in ["remove", "-rm"]:

            if count + 1 >= len(arg):
                print("Category missing")
                break

            category = arg[count + 1]
            print(Todo.remove_page(category))
            count += 2
            continue

        else:
            print(f"Unknown argument: {current}")
            break
        

def cmd_add(arg):
    count = 0
    category = None

    while count < len(arg):
        current = arg[count]
        if current in ["-task", "-t"]:
            if count + 1 >= len(arg):
                print("task missing")
                break

            task = arg[count + 1]
            print(Todo.add_page(task)["message"])
            count += 2
            continue

        elif current in ["set-default", "--sd"]:

            if current == "set-default":

                if count + 1 >= len(arg):
                    print("Category missing")
                    break

                category = arg[count + 1]
                print(Todo.set_default(category))
                count += 2
                continue

            elif current == "--sd":

                if category is None:
                    print("No category entered")
                    break

                print(Todo.set_default(category))
                count += 1
                continue

        elif current in ["remove", "-rm"]:

            if count + 1 >= len(arg):
                print("Category missing")
                break

            category = arg[count + 1]
            print(Todo.remove_page(category))
            count += 2
            continue

        else:
            print(f"Unknown argument: {current}")
            break

def cmd_remove(arg):
    pass
    
def cmd_priorty(arg):
    pass

def cmd_status(arg):
    pass

def cmd_display(arg):
    pass