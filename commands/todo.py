from pathlib import Path
from InquirerPy import inquirer
from rich.console import Console
from colorama import init

init()
console = Console()

TODO_FILE = Path.home() / ".mocha_todo.txt"

def load_tasks():
    if not TODO_FILE.exists():
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(tasks) + "\n")

def add_task(text):
    tasks = load_tasks()
    tasks.append(f"[ ] {text.strip()}")
    save_tasks(tasks)
    console.print(f"☕ Added task: {text}", style="green")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        console.print("No tasks yet!", style="yellow")
        return

    while True:
        choice = inquirer.select(
            message="📋 Mocha To-Do List (Enter = toggle, q = quit)",
            choices=[task for task in tasks] + ["[Exit]"],
            pointer="☕ ",
        ).execute()

        if choice == "[Exit]":
            break

        index = tasks.index(choice)
        if tasks[index].startswith("[ ]"):
            tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
        elif tasks[index].startswith("[x]"):
            tasks[index] = tasks[index].replace("[x]", "[ ]", 1)

        save_tasks(tasks)
        console.print(f"Toggled: {tasks[index]}", style="cyan")

    
    tasks = [t for t in tasks if not t.startswith("[x]")]
    save_tasks(tasks)
    console.print("\n✨ Completed tasks removed!", style="green")
