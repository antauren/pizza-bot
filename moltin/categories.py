# https://documentation.elasticpath.com/commerce-cloud/docs/api/catalog/categories/

import requests


def create_category(access_token, name: str, slug: str, description: str, status: str = 'live') -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {
        'data': {
            'type': 'category',
            'name': name,
            'slug': slug,
            'description': description,
            'status': status
        }
    }

    response = requests.post('https://api.moltin.com/v2/categories', headers=headers, json=data)
    response.raise_for_status()

    return response.json()
