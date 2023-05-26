from ..requests_studio import Requests
from typing import Dict


def test_get_resource_json() -> None:
    url = 'https://reqres.in/api/%5E%25%5E7Bresource%5E%25%5E7D'

    querystring = {'page':'1','per_page':'10'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://reqres.in/api-docs/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': '__stripe_mid=e3839eff-eff6-407a-8017-8ce5edb15b1b8edfaf',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
    }

    res = Requests.get(url=url, headers=headers, params=querystring)
    assert isinstance(res, Dict)

def test_get_users_json() -> None:
    url = 'https://reqres.in/api/users'

    querystring = {'page':'1','per_page':'10'}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://reqres.in/api-docs/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": "__stripe_mid=e3839eff-eff6-407a-8017-8ce5edb15b1b8edfaf",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

    res = Requests.get(url=url, headers=headers, params=querystring)
    assert isinstance(res, Dict)

