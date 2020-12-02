# https://documentation.elasticpath.com/commerce-cloud/docs/api/catalog/products/

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
