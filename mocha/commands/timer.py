import time
from rich.console import Console
from colorama import init

init()
console = Console()

def run(minutes):
    console.print(f"Starting {minutes}-minute focus timer ☕", style="bold cyan")
    try:
        for i in range(minutes, 0, -1):
            console.print(f"{i} minutes remaining...", style="yellow")
            time.sleep(60)
        console.print("⏰ Timer finished! Take a break.", style="bold green")
    except KeyboardInterrupt:
        console.print("\nTimer cancelled.", style="red")
