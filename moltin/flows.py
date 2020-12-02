# https://documentation.elasticpath.com/commerce-cloud/docs/api/advanced/custom-data/

import requests


def create_flow(access_token: str, name: str, slug: str, description: str, enabled: bool = True) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {
        'data': {
            'type': 'flow',
            'name': name,
            'slug': slug,
            'description': description,
            'enabled': enabled
        }
    }

    response = requests.post('https://api.moltin.com/v2/flows', headers=headers, json=data)
    response.raise_for_status()

    return response.json()
