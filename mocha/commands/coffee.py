from pathlib import Path
from datetime import date
from rich.console import Console
from colorama import init

init()
console = Console()

COFFEE_FILE = Path.home() / ".mocha_coffee.txt"

def _load_data():
    """Read coffee data from file"""
    if not COFFEE_FILE.exists():
        return {}
    with open(COFFEE_FILE, "r") as f:
        lines = f.readlines()
    data = {}
    for line in lines:
        try:
            d, count = line.strip().split(":")
            data[d] = int(count)
        except ValueError:
            continue
    return data

def _save_data(data):
    """Save coffee data to file"""
    with open(COFFEE_FILE, "w") as f:
        for d, count in data.items():
            f.write(f"{d}:{count}\n")

def add_coffee():
    today = str(date.today())
    data = _load_data()
    data[today] = data.get(today, 0) + 1
    _save_data(data)
    console.print(f"☕ Added one coffee! Total today: {data[today]}", style="green")

def show_stats():
    """Show coffee count for today and this week"""
    data = _load_data()
    if not data:
        console.print("No coffee tracked yet!", style="yellow")
        return

    today = str(date.today())
    today_count = data.get(today, 0)

    from datetime import timedelta
    week_dates = [(date.today() - timedelta(days=i)).isoformat() for i in range(7)]
    week_total = sum(data.get(d, 0) for d in week_dates)

    console.print("☕ [bold cyan]Mocha Coffee Tracker[/bold cyan]")
    console.print(f"  Today: {today_count} cup{'s' if today_count != 1 else ''}")
    console.print(f"  Last 7 days: {week_total} cup{'s' if week_total != 1 else ''}")

def reset_coffee():
    if COFFEE_FILE.exists():
        COFFEE_FILE.unlink()
    console.print("☕ Coffee data reset!", style="red")
    