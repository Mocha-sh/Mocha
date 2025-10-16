#!/usr/bin/env python3
import click
from commands import greet, note, timer, todo

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


if __name__ == "__main__":
    cli()
