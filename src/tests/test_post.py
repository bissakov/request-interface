from ..requests_studio import Requests
from typing import Dict


def test_post_login_error() -> None:
    url = 'https://reqres.in/api/login'

    payload = {
        'username': 'test',
        'email': 'test',
        'password': 'test'
    }

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
        'Cache-Control': 'no-cache'
    }

    res = Requests.post(url=url, headers=headers, json=payload)
    assert isinstance(res, Dict) and res['error'] == 'user not found'

