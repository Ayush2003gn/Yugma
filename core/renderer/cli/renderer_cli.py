import logging
from rich import print 

logger = logging.getLogger(__name__)


def decision_renderer(action, result):

    if result.success is True:

        if "display" in action:

            if "analysis" in action:
                display_analysis(result.data)

            elif "help" in action:
                display_help()

            else:
                display_task_list(result.data)
        

        else:
            display_message(result.message)
    
    if result.error.error_boolean is True:
        logger.error(result.error.error_message)
        display_error(result.error.error_message)
    else:
        logger.info(result.message)

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
        for task in task_page.data:
            print(f"- [blue]{task}[/blue]")
    print()

def display_analysis(message):
    print()
    for line in message:
        print(f"[yellow]{line['data']}[/yellow]")
    print()

def display_error(error_message):
    print()
    print(f"[red]Error: {error_message}[/red]")
    print()

def display_help():
    print()
    print("[bold green]Help[/bold green]")
    print("[bold green]Type [blue]add[/blue] to add tasks.[/bold green]")
    print("[bold green]Type [blue]display[/blue] to display tasks.[/bold green]")
    print("[bold green]Type [blue]help[/blue] to see available commands.[/bold green]")
    print("[bold green]Type [blue]exit[/blue] to exit.[/bold green]")
    print("[bold green]Type [blue]analysis[/blue] to see analysis.[/bold green]")
    print("[bold green]Type [blue]update[/blue] to update tasks.[/bold green]")
    print("[bold green]Type [blue]page[/blue] to do operations on page.[/bold green]")
    print()

def display_exit():
    print()
    print("[bold green]Exiting....[/bold green]")
    print("[bold green]Saving data...[/bold green]")
    print("[bold green]Goodbye![/bold green]")
    print()