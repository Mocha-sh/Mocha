from pathlib import Path
from datetime import date, timedelta
from rich.console import Console
from colorama import init

init()
console = Console()

HYDRATE_FILE = Path.home() / ".mocha_hydrate.txt"
DAILY_GOAL = 8  # Gläser pro Tag

def _load_data():
    """Read hydration data from file"""
    if not HYDRATE_FILE.exists():
        return {}
    data = {}
    with open(HYDRATE_FILE, "r") as f:
        for line in f:
            try:
                d, count = line.strip().split(":")
                data[d] = int(count)
            except ValueError:
                continue
    return data

def _save_data(data):
    """Save hydration data to file"""
    with open(HYDRATE_FILE, "w") as f:
        for d, count in data.items():
            f.write(f"{d}:{count}\n")

def add_glass():
    """Add a glass of water"""
    today = str(date.today())
    data = _load_data()
    data[today] = data.get(today, 0) + 1
    _save_data(data)

    remaining = DAILY_GOAL - data[today]
    if remaining > 0:
        console.print(f"💧 Added one glass! {data[today]}/{DAILY_GOAL} for today. Keep going!", style="cyan")
    else:
        console.print(f"💧 Added one glass! {data[today]}/{DAILY_GOAL} — Goal reached! 🎉", style="green")

def show_stats():
    """Show hydration stats"""
    data = _load_data()
    if not data:
        console.print("No hydration data yet. Start with: mocha hydrate", style="yellow")
        return

    today = str(date.today())
    today_count = data.get(today, 0)
    week_dates = [(date.today() - timedelta(days=i)).isoformat() for i in range(7)]
    week_total = sum(data.get(d, 0) for d in week_dates)

    console.print("💧 [bold cyan]Mocha Hydration Tracker[/bold cyan]")
    console.print(f"  Today: {today_count}/{DAILY_GOAL} glasses")
    console.print(f"  Last 7 days: {week_total} total glasses")

    if today_count < DAILY_GOAL:
        console.print("🥤 Stay hydrated!", style="blue")
    else:
        console.print("✅ You’ve reached your goal today!", style="green")

def reset_hydration():
    """Reset hydration data"""
    if HYDRATE_FILE.exists():
        HYDRATE_FILE.unlink()
    console.print("💧 Hydration data reset!", style="red")
