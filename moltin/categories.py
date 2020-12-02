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


def create_category_relationship(access_token: str, product_id: str, category_id: str) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {'data': [{'type': 'category', 'id': category_id}]}

    response = requests.post('https://api.moltin.com/v2/products/{}/relationships/categories'.format(product_id),
                             headers=headers,
                             json=data)
    response.raise_for_status()

    return response.json()
