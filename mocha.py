#!/usr/bin/env python3
import click
from commands import greet, note, timer, todo, coffee, hydrate

@click.group()
def cli():
    """Mocha.sh — your cozy terminal companion ☕"""
    pass

@cli.command()
def greet_cmd():
    """Send a friendly greeting"""
    greet.run()

@cli.command()
@click.argument('args', nargs=-1)
def note_cmd(args):
    """Create or list quick notes"""
    if not args:
        note.list_notes()
    elif args[0].lower() == "list":
        note.list_notes()
    elif args[0].lower() == "delete":
        note.delete_note(" ".join(args[1:]))
    else:
        note.run(" ".join(args))

@cli.command()
@click.argument('minutes', type=int)
def timer_cmd(minutes):
    """Start a focus timer (in minutes)"""
    timer.start_timer(minutes)

@cli.command()
@click.argument('args', nargs=-1)
def todo_cmd(args):
    """Add or list to-do items"""
    if not args:
        click.echo("Please provide a todo text or 'list'.")
        return

    if args[0].lower() == "list":
        todo.list_tasks()
    else:
        todo.add_task(" ".join(args))

@cli.group()
def coffee_cmd():
    """Track your daily coffee cups ☕"""
    pass

@coffee_cmd.command("add")
def add_coffee():
    """Add one cup of coffee"""
    coffee.add_coffee()

@coffee_cmd.command("stats")
def stats():
    """Show your coffee stats"""
    coffee.show_stats()

@coffee_cmd.command("reset")
def reset():
    """Reset all coffee data"""
    coffee.reset_coffee()

@cli.group()
def hydrate():
    """Track your daily water intake"""
    pass

@hydrate.command("add")
def hydrate_add():
    from commands import hydrate
    hydrate.add_glass()

@hydrate.command("stats")
def hydrate_stats():
    from commands import hydrate
    hydrate.show_stats()

@hydrate.command("reset")
def hydrate_reset():
    from commands import hydrate
    hydrate.reset_hydration()

if __name__ == "__main__":
    cli()
