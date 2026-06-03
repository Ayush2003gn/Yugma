import logging
from rich import print 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

logger = logging.getLogger(__name__)


def decision_renderer(action, result):

    if result.success is True:

        if "display" in action:

            if "analysis" in action:
                display_analysis(result.data)

            else:
                display_task_list(result.data)

        elif "help" in action:
            display_help()

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

    console.print(
        Panel.fit(
            "[bold cyan]Yukta Help[/bold cyan]\n"
            "[green]Task Management CLI[/green]",
            border_style="cyan"
        )
    )

    # ---------------- TASK COMMANDS ----------------

    task_table = Table(title="Task Commands")

    task_table.add_column("Command", style="cyan", no_wrap=True)
    task_table.add_column("Description", style="green")
    task_table.add_column("Example", style="yellow")

    task_table.add_row(
        "add",
        "Add a new task",
        "add -t 'Study Python'"
    )

    task_table.add_row(
        "remove",
        "Remove a task",
        "remove -uid Y1"
    )

    task_table.add_row(
        "update",
        "Update task name",
        "update -uid Y1 -t 'New Task'"
    )

    task_table.add_row(
        "done",
        "Mark task as completed",
        "done -uid Y1"
    )

    task_table.add_row(
        "undone",
        "Mark task as pending",
        "undone -uid Y1"
    )

    task_table.add_row(
        "priority",
        "Change task priority",
        "priority -uid Y1"
    )

    console.print(task_table)

    # ---------------- PAGE COMMANDS ----------------

    page_table = Table(title="Page Commands")

    page_table.add_column("Command", style="cyan", no_wrap=True)
    page_table.add_column("Description", style="green")
    page_table.add_column("Example", style="yellow")

    page_table.add_row(
        "page",
        "Manage task pages",
        "page add Work"
    )

    console.print(page_table)

    # ---------------- DISPLAY COMMANDS ----------------

    display_table = Table(title="Display Commands")

    display_table.add_column("Command", style="cyan", no_wrap=True)
    display_table.add_column("Description", style="green")
    display_table.add_column("Example", style="yellow")

    display_table.add_row(
        "display",
        "Display tasks",
        "display"
    )

    display_table.add_row(
        "display --analysis",
        "Show task analysis",
        "analysis"
    )

    console.print(display_table)

    # ---------------- UTILITY COMMANDS ----------------

    utility_table = Table(title="Utility Commands")

    utility_table.add_column("Command", style="cyan", no_wrap=True)
    utility_table.add_column("Description", style="green")
    utility_table.add_column("Example", style="yellow")

    utility_table.add_row(
        "help",
        "Show help screen",
        "help"
    )

    utility_table.add_row(
        "exit",
        "Exit Yukta",
        "exit"
    )

    console.print(utility_table)

def display_exit():
    print()
    print("[bold green]Exiting....[/bold green]")
    print("[bold green]Saving data...[/bold green]")
    print("[bold green]Goodbye![/bold green]")
    print()