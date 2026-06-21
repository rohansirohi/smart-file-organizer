import typer
from pathlib import Path
from src.file_organizer.organizer import organize_folder

app = typer.Typer()


@app.command()
def main(
    folder: str = typer.Argument(..., help="Path to the messy folder you want to organize"),
    config: str = typer.Option("configs/rules.yml", help="Path to your rules.yml file"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without moving files"),
):
    """Smart File Organizer - sorts your messy folder automatically!"""

    if not Path(folder).exists():
        typer.echo(f"Error: Folder '{folder}' does not exist!")
        raise typer.Exit(1)

    typer.echo(f"Organizing folder: {folder}")
    organize_folder(folder, config, dry_run)
    typer.echo("Done! ✅")


if __name__ == "__main__":
    app()