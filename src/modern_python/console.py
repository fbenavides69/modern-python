import textwrap

import click

from . import __version__
from . import wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language Edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """ The Modern Python Project """
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
