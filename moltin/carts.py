# https://documentation.elasticpath.com/commerce-cloud/docs/api/carts-and-checkout/carts/

import requests


def get_cart_items(access_token: str, user: str) -> dict:
    headers = {'Authorization': 'Bearer {}'.format(access_token)}

    response = requests.get('https://api.moltin.com/v2/carts/{}/items'.format(user), headers=headers)
    response.raise_for_status()

    return response.json()


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


def remove_cart_item(access_token: str, user: str, product_id: str) -> dict:
    headers = {'Authorization': 'Bearer {}'.format(access_token)}

    response = requests.delete('https://api.moltin.com/v2/carts/{}/items/{}'.format(user, product_id), headers=headers)
    response.raise_for_status()

    return response.json()
