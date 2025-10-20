from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from colorama import init
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import TextArea, Static, Footer
from textual.reactive import reactive

init()
console = Console()


NOTES_DIR = Path.home() / ".mocha_notes"
NOTES_DIR.mkdir(exist_ok=True)


def _list_note_files():
    """Return all note files sorted by modification date (newest first)."""
    return sorted(NOTES_DIR.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)


def run(text):
    """Create a new markdown note."""
    if not text.strip():
        console.print("Please provide some text for the note.", style="red")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = NOTES_DIR / f"{timestamp}.md"

    with open(filename, "w") as f:
        f.write(text.strip() + "\n")

    console.print(f"📝 Created note: {filename.name}", style="green")


def list_notes():
    """Display all existing notes and show the first line of each file."""
    files = _list_note_files()
    if not files:
        console.print("No notes found.", style="yellow")
        return

    console.print("📓 [bold cyan]Your Mocha Notes[/bold cyan]\n")

    for i, file in enumerate(files, 1):
        try:
            with open(file, "r") as f:
                first_line = f.readline().strip()
            display_text = first_line if first_line else "(empty note)"
            console.print(f"{i}. {display_text}", style="white")
        except Exception as e:
            console.print(f"{i}. [Error reading {file.name}: {e}]", style="red")


def view_note(index):
    """Show the full content of a specific note by its index."""
    files = _list_note_files()
    if not files:
        console.print("No notes found.", style="yellow")
        return

    index = int(index)
    if index < 1 or index > len(files):
        console.print("Invalid note number.", style="red")
        return

    note_file = files[index - 1]
    console.print(f"📝 [bold cyan]{note_file.name}[/bold cyan]\n")
    with open(note_file, "r") as f:
        content = f.read()
    console.print(Panel(content, title="Note Content", border_style="cyan"))


def delete_note(index):
    """Delete a note by its index number."""
    files = _list_note_files()
    if not files:
        console.print("No notes found.", style="yellow")
        return

    index = int(index)
    if index < 1 or index > len(files):
        console.print("Invalid note number.", style="red")
        return

    note_file = files[index - 1]
    note_file.unlink()
    console.print(f"🗑️ Deleted note: {note_file.name}", style="green")


class MochaEditor(App):
    """Markdown editor with syntax highlighting, live preview, and a stylish status bar."""
    CSS_PATH = None
    show_preview = reactive(True)

    def __init__(self, note_file: Path, theme: str | None = None):
        super().__init__()
        self.note_file = note_file
        self.text_area: TextArea | None = None
        self.preview: Static | None = None
  
        self.syntax_theme = theme or "monokai"

    def compose(self) -> ComposeResult:
        """Define the layout of the editor and preview areas."""
        with Horizontal(id="layout"):

            self.text_area = TextArea(
                language="markdown",
                theme=self.syntax_theme,
                id="editor",
            )
            self.preview = Static(id="preview")
            yield self.text_area
            yield self.preview
        yield Footer()

    def on_mount(self):
        """Initialize the editor when it is first displayed."""
        text = self.note_file.read_text() if self.note_file.exists() else ""
        self.text_area.text = text
        self._update_preview(text)
        self.set_focus(self.text_area)
        self._render_status("📝 Editing • [Ctrl+S] Save | [Ctrl+Q] Quit | [Ctrl+P] Toggle Preview")

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        """Update the live preview whenever the text changes."""
        if self.show_preview:
            self._update_preview(self.text_area.text)

    def _update_preview(self, text: str) -> None:
        """Render the Markdown preview."""
        if self.preview:
            self.preview.update(Panel(Markdown(text), title="Preview", border_style="cyan"))

    def _render_status(self, msg: str) -> None:
        """Placeholder for future status bar messages."""
        pass

    def on_key(self, event):
        """Handle keybindings for saving, quitting, and toggling the preview."""
        key = event.key.lower()
        if key == "ctrl+s":
            self.note_file.write_text(self.text_area.text)
            if self.preview:
                self.preview.border_title = f"💾 Saved {self.note_file.name}"
        elif key == "ctrl+q":
            self.exit()
        elif key == "ctrl+p":
            self.show_preview = not self.show_preview
            self._toggle_preview()

    def _toggle_preview(self):
        """Toggle the visibility of the Markdown preview panel."""
        if not self.preview:
            return
        if self.show_preview:
            self._update_preview(self.text_area.text)
            self.preview.display = True
        else:
            self.preview.display = False


def edit_note(index):
    """Open a note in the Markdown editor with syntax highlighting and preview."""
    files = _list_note_files()
    if not files:
        console.print("No notes found.", style="yellow")
        return

    index = int(index)
    if index < 1 or index > len(files):
        console.print("Invalid note number.", style="red")
        return

    note_file = files[index - 1]
    console.print(f"📝 Opening Markdown editor for [cyan]{note_file.name}[/cyan]...\n")
    MochaEditor(note_file).run()
    console.print(f"💾 Exited editor for {note_file.name}", style="green")
