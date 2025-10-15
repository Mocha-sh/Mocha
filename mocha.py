#!/usr/bin/env python3
import click
from commands import greet, note, timer

@click.group()
def cli():
    """☕ Mocha.sh - Cozy CLI Tool for Developers"""
    pass

@cli.command()
def greet_cmd():
    """Display a cozy greeting"""
    greet.run()

@cli.command()
@click.argument('args', nargs=-1)
def note_cmd(args):
    """Save a quick note or list notes"""
    if not args:
        click.echo("Please provide a note or 'list' to see all notes.")
        return
    if args[0].lower() == "list":
        note.list_notes()
    else:
        note.run(" ".join(args))

@cli.command()
@click.argument('minutes', type=int)
def timer_cmd(minutes):
    """Start a focus timer (minutes)"""
    timer.run(minutes)

if __name__ == "__main__":
    cli()
