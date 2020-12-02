# https://documentation.elasticpath.com/commerce-cloud/docs/api/


import requests


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
