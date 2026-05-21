import logging
from rich import print 

logger = logging.getLogger(__name__)

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