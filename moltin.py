# https://documentation.elasticpath.com/commerce-cloud/docs/api/


import requests


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


def create_field(access_token: str,
                 flow_id: str,
                 name: str,
                 slug: str,
                 description: str,
                 field_type: str = 'string',
                 validation_rules: list = None,
                 required: bool = False,
                 default=None,
                 enabled: bool = True,
                 order: int = 1,
                 omit_null: bool = False
                 ) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    if validation_rules is None:
        validation_rules = []

    data = {
        'data': {
            'type': 'field',
            'name': name,
            'slug': slug,
            'field_type': field_type,
            'validation_rules': validation_rules,
            'description': description,
            'required': required,
            'default': default,
            'enabled': enabled,
            'order': order,
            'omit_null': omit_null,
            'relationships': {
                'flow': {
                    'data': {
                        'type': 'flow',
                        'id': flow_id
                    }
                }
            }
        }
    }

    response = requests.post('https://api.moltin.com/v2/fields', headers=headers, json=data)
    response.raise_for_status()

    return response.json()


def create_entry(access_token: str, flow_slug: str, entry: dict) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {'data': {'type': 'entry', }}
    data['data'].update(entry)

    response = requests.post('https://api.moltin.com/v2/flows/{}/entries'.format(flow_slug), headers=headers, json=data)
    response.raise_for_status()

    return response.json()
