from os import stat
import requests
from requests import Response
import rich
from typing import Dict, Optional, Any


class Requests:
    @staticmethod
    def request(method: str, url: str, params: Optional[Dict] = None, data: Optional[Dict] = None,
                json: Optional[Dict] = None, headers: Optional[Dict] = None, cookies: Optional[Dict] = None,
                timeout: Optional[float] = None) -> Optional[Dict]:
        response = requests.request(method=method, url=url, params=params,
                                data=data, json=json, headers=headers, cookies=cookies,
                                timeout=timeout)
        response.raise_for_status()
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return None

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
    r = Requests.post(url='https://reqres.in/api/users', json={'name': 'morpheus', 'job': 'leader'})
    # r = Requests.get('https://reqres.in')
    rich.print(r)

