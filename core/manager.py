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
                logger.error("Category missing in argument")
                break

            category = arg[count + 1]
            print(Todo.add_page(category))
            count += 2
            continue

        elif current in ["set-default", "--sd"]:

            if current == "set-default":

                if count + 1 >= len(arg):
                    print("Category missing")
                    logger.error("Category missing in argument")
                    break

                category = arg[count + 1]
                print(Todo.set_default(category))
                count += 2
                continue

            elif current == "--sd":

                if category is None:
                    print("No category entered")
                    logger.error("No category entered in argument")
                    break

                print(Todo.set_default(category))
                count += 1
                continue

        elif current in ["remove", "-rm"]:

            if count + 1 >= len(arg):
                print("Category missing")
                logger.error("Category missing in argument")
                break

            category = arg[count + 1]
            print(Todo.remove_page(category))
            count += 2
            continue

        else:
            print(f"Unknown argument: {current}")
            logger.error(f"Unknown argument: {current}")
            break
        

def cmd_add(arg):
    if arg[0] == "-t" or arg[0] == "-task":
        task = arg[1]
    else:
        print("You didn't enter task in proper order")
        logger.error("Didn't enter task in proper order")
        return
    
    if "--C" in arg:
        index = arg.index("--C") #manual setting category
        if index + 1 >= len(arg):
            print("Category missing")
            logger.error("Category missing in argument")
            return
        category = arg[index+1]
    else:
        category = None

    newtask = Todo.add_task(task,category)
    print(newtask["message"],category)

    if newtask["success"] == False:
        return
    
    count = 2
    id = newtask["task"].id

    while count < len(arg):
        current = arg[count]
        if current in ["--P","--priorty"]:
            level = arg[count + 1].lower()
            if level in ["high","low","normal"]:

                if level == "high":
                    Todo.highpriority_task(id,category)
                elif level == "low":
                    Todo.lowpriority_task(id,category)
                elif level == "normal":
                    Todo.Normalpriority_task(id,category)
                
            else:
                print("Not enter valid priority")
                logger.error("Not enter valid priority")
            count += 2
            continue

        elif current == "--MD":
            Todo.mark_done(id,category)
            continue

        elif current == "--MUD":
            Todo.mark_undone(id,category)
            continue
        else:
            print(f"Unknown argument: {current}")
            break
    count += 1

def cmd_remove(arg):
    if arg[0] == "-id":
        id = arg[1]
    else:
        print("You didn't enter id in proper order")
        logger.error("Didn't enter id in proper order")
        return
    
    if "--C" in arg:
        index = arg.index("--C") #manual setting category
        category = arg[index+1]
    else:
        category = None
    
    action = Todo.remove_task(id , category)
    print(action["message"])
    
def cmd_priorty(arg):
    if "--C" in arg:
        index = arg.index("--C") #manual setting category
        if index + 1 >= len(arg):
            print("Category missing")
            logger.error("Category missing in argument")
            return
        category = arg[index+1]
    else:
        category = None

    if arg[0] == "-id":
        id = arg[1]
    else:
        print("You didn't enter id in proper order")
        logger.error("Didn't enter id in proper order")
        return
    
    if arg[2] == "-P":
        level = arg[3].lower()
        if level in ["high","low","normal"]:

            if level == "high":
                action = Todo.highpriority_task(id,category)
            elif level == "low":
                action = Todo.lowpriority_task(id,category)
            elif level == "normal":
                action = Todo.Normalpriority_task(id,category)
            
            print(action["message"])
        else:
            print("Not enter priorty properly")
            logger.error("Not enter priorty properly")
            return
    else:
        print("didn't enter argument properly")
        logger.error("didn't enter argument properly")
        return
    

def cmd_status(arg):
    if arg[0] == "-id":
        id = arg[1]
    else:
        print("You didn't enter id in proper order")
        return
    
    if "--C" in arg:
        index = arg.index("--C") #manual setting category
        category = arg[index+1]
    else:
        category = None
    
    count = 2

    while count < len(arg):
        current = arg[count]

        if current in ["--MD","--Mark-done"]:
            action = Todo.mark_done(id,category)
            print(action["message"])
            break

        elif current in ["--MUD","--Mark-undone"]:
            action = Todo.mark_undone(id,category)
            print(action["message"])
            break
        else:
            print(f"Unknown argument: {current}")
            break
        


def cmd_display(arg):

    # ---------------- DEFAULT ----------------
    if not arg:
        Todo.display_all()
        return

    category = "*"

    # ---------------- CATEGORY ----------------
    if "--C" in arg:
        index = arg.index("--C")
        if index + 1 < len(arg):
            category = arg[index + 1]

    # ---------------- ALL TASKS ----------------
    if "--all" in arg:
        Todo.display_all(category)
        return

    # ---------------- ANALYSIS ----------------
    elif "--analysis" in arg or "--A" in arg:
        Todo.display_analysis()
        return

    # ---------------- YEAR ----------------
    elif "--year" in arg:
        index = arg.index("--year")

        if index + 1 >= len(arg):
            print("Year missing")
            return

        year = int(arg[index + 1])

        Todo.display_byyear(year, category)
        return

    # ---------------- MONTH ----------------
    elif "--month" in arg:
        index = arg.index("--month")

        if index + 2 >= len(arg):
            print("Month or Year missing")
            return

        month = arg[index + 1]
        year = int(arg[index + 2])

        Todo.display_bymonths(month, year, category)
        return

    # ---------------- WEEK ----------------
    elif "--week" in arg:
        index = arg.index("--week")

        if index + 2 >= len(arg):
            print("Week or Year missing")
            return

        week = int(arg[index + 1])
        year = int(arg[index + 2])

        Todo.display_byweek(week, year, category)
        return

    # ---------------- DAY ----------------
    elif "--day" in arg:
        index = arg.index("--day")

        if index + 3 >= len(arg):
            print("Day Month Year missing")
            return

        day = int(arg[index + 1])
        month = int(arg[index + 2])
        year = int(arg[index + 3])

        Todo.display_byday(day, month, year, category)
        return

    else:
        print("Unknown display command")

def cmd_help():

    print("""
================ Yukta Help =================

PAGE COMMANDS
-------------
page add <category>
page add <category> --sd
page set-default <category>
page remove <category>

TASK COMMANDS
-------------
add -t "task name"
add -t "task name" --C study
add -t "task name" --P high
add -t "task name" --MD

delete -id <task_id>

STATUS COMMANDS
---------------
status -id <task_id> --MD
status -id <task_id> --MUD

DISPLAY COMMANDS
----------------
display
display --all
display --analysis
display --year 2026
display --month May 2026
display --week 20 2026
display --day 11 5 2026

CATEGORY FILTER
---------------
display --all --C study

EXIT
----
exit

================================================
""")