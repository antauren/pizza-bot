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
