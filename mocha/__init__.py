#!/usr/bin/env python3
import click
import os
import importlib.util


@click.group()
def cli():
    """Mocha.sh — your cozy terminal companion ☕"""
    pass


from mocha.commands import note, greet, hydrate, todo, timer, coffee


@cli.command()
def greet_cmd():
    """Send a friendly greeting"""
    greet.run()


@cli.command()
@click.argument('args', nargs=-1)
def note_cmd(args):
    """Create, list, view, edit, or delete notes"""
    if not args:
        note.list_notes()
    elif args[0].lower() == "list":
        note.list_notes()
    elif args[0].lower() == "view":
        note.view_note(args[1])
    elif args[0].lower() == "delete":
        note.delete_note(args[1])
    elif args[0].lower() == "edit":
        note.edit_note(args[1])
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
def hydrate_cmd():
    """Track your daily water intake 💧"""
    pass


@hydrate_cmd.command("add")
def hydrate_add():
    hydrate.add_glass()


@hydrate_cmd.command("stats")
def hydrate_stats():
    hydrate.show_stats()


@hydrate_cmd.command("reset")
def hydrate_reset():
    hydrate.reset_hydration()


import pathlib

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
