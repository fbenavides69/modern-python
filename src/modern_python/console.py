import sys
import locale
import textwrap

import click
import requests

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The Modern Python project."""
    try:
        userLocale = locale.getlocale()[0].split("_")[0]
        API_URL: str = f"https://{userLocale}.wikipedia.org/api/rest_v1/page/random/summary"

        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()

            title = data["title"]
            extract = data["extract"]

            click.secho(title, fg="green")
            click.echo(textwrap.fill(extract))

    except (requests.exceptions.Timeout,
            requests.ConnectionError,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.RequestException) as e:
        print(str(e))
        sys.exit(1)
