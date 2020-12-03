# https://documentation.elasticpath.com/commerce-cloud/docs/api/carts-and-checkout/carts/

import requests


def add_product_to_cart(access_token: str, customer: str, product_id: str, quantity: int) -> dict:
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json',
    }

    data = {
        'data': {
            'id': product_id,
            'type': 'cart_item',
            'quantity': quantity,
        }
    }

    response = requests.post('https://api.moltin.com/v2/carts/{}/items'.format(customer), headers=headers, json=data)
    response.raise_for_status()

    return response.json()
