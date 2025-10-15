from pathlib import Path
from rich.console import Console
from colorama import init

init()
console = Console()

NOTES_FILE = Path.home() / ".mocha_notes.txt"

def run(text):
    """Add a new note"""
    with open(NOTES_FILE, "a") as f:
        f.write(text + "\n")
    console.print(f"Saved note: {text}", style="green")

def list_notes():
    """List all saved notes"""
    if not NOTES_FILE.exists():
        console.print("No notes found.", style="yellow")
        return
    console.print("📓 Your Quick Notes:", style="bold cyan")
    with open(NOTES_FILE, "r") as f:
        for i, line in enumerate(f, 1):
            console.print(f"{i}. {line.strip()}")
