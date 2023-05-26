import requests
import rich
from typing import Dict, Optional, Any


class Requests:
    def __init__(self):
        pass

    @staticmethod
    def request(method: str, url: str, params: Optional[Dict] = None, data: Optional[Dict] = None,
                json: Optional[Dict] = None, headers: Optional[Dict] = None, cookies: Optional[Dict] = None,
                timeout: Optional[float] = None) -> Optional[Dict]:
        response = requests.request(method=method, url=url, params=params,
                                data=data, json=json, headers=headers, cookies=cookies,
                                timeout=timeout)
        # response.raise_for_status()
        try:
            res = response.json()
        except requests.exceptions.JSONDecodeError:
            res = None
        if not res:
            response.raise_for_status()
        return res

    @staticmethod
    def get(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='GET', **kwargs)

    @staticmethod
    def post(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='POST', **kwargs)

    @staticmethod
    def head(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='HEAD', **kwargs)

    @staticmethod
    def options(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='OPTIONS', **kwargs)

    @staticmethod
    def put(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='PUT', **kwargs)

    @staticmethod
    def patch(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='PATCH', **kwargs)

    @staticmethod
    def delete(**kwargs: Any) -> Optional[Dict]:
        return Requests.request(method='DELETE', **kwargs)


if __name__ == '__main__':
    # _requests = Requests()
    # rich.print(dir(requests))
    # r = Requests.get(url='https://reqres.in/api/users?page=1')
    # r = Requests.post(url='https://reqres.in/api/users', json={'name': 'morpheus', 'job': 'leader'})
    # rich.print(r)

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
    print(res)

