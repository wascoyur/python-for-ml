"""Console script for python_starter."""

import typer
from rich.console import Console

from python_starter import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for python_starter."""
    console.print("Replace this message by putting your code into "
               "python_starter.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
