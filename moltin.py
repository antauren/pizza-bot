# https://documentation.elasticpath.com/commerce-cloud/docs/api/


import requests


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
