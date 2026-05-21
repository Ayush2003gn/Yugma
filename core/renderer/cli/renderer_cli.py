import logging
from rich import print 

logger = logging.getLogger(__name__)

def decision_renderer(cmd, result):
    if result["success"]:
        if cmd == "display":
            display_task_list(result["data"])
        else:                    
            display_message(result["message"])
    else:
        display_error(result["message"])

def welcome_message():
    print()
    print("[bold green]Welcome to Yukta CLI![/bold green]")
    print("Type [blue]help[/blue] to see available commands.")
    print()

def display_message(message):
    print()
    print(f"[green]{message}[/green]")
    print()

def display_task_list(taskpage):
    print()
    for task_page in taskpage:
        for task in task_page:
            print(f"- [blue]{task}[/blue]")
    print()


def display_error(error_message):
    print()
    print(f"[red]Error: {error_message}[/red]")
    print()