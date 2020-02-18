import click
import locale
import requests

API_URL: str = "https://{{language}}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str) -> dict:
    """ Return a random page title and summary from a given language Wikipedia page

        :param language: Two/Three letter language standard format that denotes the given language from which
                            to do the extraction
        :return: title and summary response
    """
    # userLocale = locale.getlocale()[0].split("_")[0]
    url = API_URL.format(language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()

    except requests.exceptions.RequestException as e:
        message = str(e)
        raise click.ClickException(message)
