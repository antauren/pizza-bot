# https://documentation.elasticpath.com/commerce-cloud/docs/api/advanced/files/

import requests


def create_file_from_url(access_token: str, url: str, filename: str) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }

    file = requests.get(url)

    files = {
        'file': (filename, file.content),
        'public': (None, 'true'),
    }

    response = requests.post('https://api.moltin.com/v2/files', headers=headers, files=files)
    response.raise_for_status()

    return response.json()
