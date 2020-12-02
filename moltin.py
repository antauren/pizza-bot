# https://documentation.elasticpath.com/commerce-cloud/docs/api/

import datetime as dt

import requests

_access_token = ''
_datetime = dt.datetime.now() - dt.timedelta(hours=1)
_token_expires_in = 0


def get_access_token(client_id: str, client_secret: str) -> str:
    global _access_token
    global _token_expires_in
    global _datetime

    if dt.datetime.now() - _datetime > dt.timedelta(seconds=_token_expires_in):
        access_token_dict = _get_access_token(client_id, client_secret)

        _access_token = access_token_dict['access_token']
        _token_expires_in = access_token_dict['expires_in']

        _datetime = dt.datetime.now()

    return _access_token


def _get_access_token(client_id: str, client_secret: str) -> dict:
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post('https://api.moltin.com/oauth/access_token', data=data)
    response.raise_for_status()

    return response.json()


def create_product(access_token: str,
                   name: str,
                   slug: str,
                   sku: str,
                   description: str,
                   price: int,
                   currency: str = 'RUB',
                   includes_tax: bool = True,
                   status: str = 'live',
                   manage_stock: bool = False,
                   commodity_type: str = 'physical',
                   ) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {
        'data': {
            'type': 'product',
            'name': name,
            'slug': slug,
            'sku': sku,
            'description': description,
            'manage_stock': manage_stock,
            'price': [
                {
                    'amount': price,
                    'currency': currency,
                    'includes_tax': includes_tax,
                }
            ],
            'status': status,
            'commodity_type': commodity_type
        }
    }

    response = requests.post('https://api.moltin.com/v2/products', headers=headers, json=data)
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


def create_main_image_relationship(access_token, product_id: str, image_id: str) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {'data': {'type': 'main_image', 'id': image_id}}

    response = requests.post('https://api.moltin.com/v2/products/{}/relationships/main-image'.format(product_id),
                             headers=headers,
                             json=data)
    response.raise_for_status()

    return response.json()


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
