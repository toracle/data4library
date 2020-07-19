import requests

from data4library.utils import to_camel_case


class Client:
    base_url = 'http://data4library.kr/api'

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()

    def send(self, action, **options):
        url = f'{self.base_url}/{action}'
        params = {
            'auth_key': self.api_key,
            'format': 'json',
            **{
                to_camel_case(k): v
                for k, v in options.items()
            }
        }
        response = requests.get(url, params)
        return response

    def search_library(self):
        response = self.send('libSrch')
        return response
