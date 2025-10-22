#!/usr/bin/env python3
import click
import os
import importlib.util
import pathlib

from mocha.commands import note, greet, hydrate, todo, timer, coffee


@click.group()
def cli():
    """Mocha.sh — your cozy terminal companion ☕"""
    pass




@cli.command(name="greet")
def greet():
    """Send a friendly greeting"""
    from mocha.commands import greet as greet_module
    greet_module.run()


@cli.command(name="note")
@click.argument("args", nargs=-1)
def note_cmd(args):
    """Create, list, view, edit, or delete notes"""
    if not args:
        note.list_notes()
    elif args[0].lower() == "list":
        note.list_notes()
    elif args[0].lower() == "view":
        note.view_note(int(args[1]))
    elif args[0].lower() == "delete":
        note.delete_note(int(args[1]))
    elif args[0].lower() == "edit":
        note.edit_note(int(args[1]))
    else:
        note.run(" ".join(args))


@cli.command(name="timer")
@click.argument("minutes", type=int)
def timer_cmd(minutes):
    """Start a focus timer (in minutes)"""
    timer.start_timer(minutes)


@cli.command(name="todo")
@click.argument("args", nargs=-1)
def todo_cmd(args):
    """Add or list to-do items"""
    if not args:
        click.echo("Please provide a todo text or 'list'.")
        return

    if args[0].lower() == "list":
        todo.list_tasks()
    else:
        todo.add_task(" ".join(args))


@cli.group(name="coffee")
def coffee_group():
    """Track your daily coffee cups ☕"""
    pass


@coffee_group.command(name="add")
def add_coffee():
    """Add one cup of coffee"""
    coffee.add_coffee()


@coffee_group.command(name="stats")
def coffee_stats():
    """Show your coffee stats"""
    coffee.show_stats()


@coffee_group.command(name="reset")
def coffee_reset():
    """Reset all coffee data"""
    coffee.reset_coffee()



@cli.group(name="hydrate")
def hydrate_group():
    """Track your daily water intake 💧"""
    pass


@hydrate_group.command(name="add")
def hydrate_add():
    """Add one glass of water"""
    hydrate.add_glass()


@hydrate_group.command(name="stats")
def hydrate_stats():
    """Show hydration stats"""
    hydrate.show_stats()


@hydrate_group.command(name="reset")
def hydrate_reset():
    """Reset hydration data"""
    hydrate.reset_hydration()


PLUGIN_DIR = os.path.join(pathlib.Path.home(), ".mocha_plugins")


def load_plugins(cli):
    """Load all plugins from ~/.mocha_plugins/ directory."""
    if not os.path.exists(PLUGIN_DIR):
        os.makedirs(PLUGIN_DIR)
        click.echo(f"📦 Created plugin folder at {PLUGIN_DIR}")
        return

    for filename in os.listdir(PLUGIN_DIR):
        if not filename.endswith(".py"):
            continue

        path = os.path.join(PLUGIN_DIR, filename)
        spec = importlib.util.spec_from_file_location(filename[:-3], path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, "register"):
                module.register(cli)
        except Exception as e:
            click.echo(f"⚠️ Failed to load plugin {filename}: {e}")



if __name__ == "__main__":
    load_plugins(cli)
    cli()
