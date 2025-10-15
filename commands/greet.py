from rich.console import Console
from colorama import init

init()
console = Console()

def run():
    console.print("☕ Welcome to Mocha.sh!", style="bold green")
    console.print("Your cozy terminal companion.", style="italic yellow")
