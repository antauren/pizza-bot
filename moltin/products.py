# https://documentation.elasticpath.com/commerce-cloud/docs/api/catalog/products/

import requests


def filter_products_by_one_category_and_live_status(access_token: str, category_id: str) -> dict:
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    params = {'filter': 'eq(category.id,{}),eq(status,live)'.format(category_id)}

    response = requests.get('https://api.moltin.com/v2/products', headers=headers, params=params)
    response.raise_for_status()

    return response.json()


def get_product(product_id: str, access_token: str) -> dict:
    headers = {'Authorization': 'Bearer {}'.format(access_token)}

    response = requests.get('https://api.moltin.com/v2/products/{}'.format(product_id), headers=headers)
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


def get_product_display_price(product: dict) -> dict:
    return product['meta']['display_price']['with_tax']
