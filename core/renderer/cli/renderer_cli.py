import logging
from rich import print 

logger = logging.getLogger(__name__)

def display_message(message):
    print()
    print(f"[green]{message}[/green]")
    print()

def display_task_list(task_list):
    print()
    for task in task_list:
        print(f"- [blue]{task}[/blue]")
    print()


def display_error(error_message):
    print()
    print(f"[red]Error: {error_message}[/red]")
    print()