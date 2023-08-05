import click

from ..utils import execute


@click.command()
def cmd() -> None:
    execute("conda", "clean", "--all")
    execute("pip", "cache", "purge")
