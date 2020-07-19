import requests

from data4library.utils import to_camel_case
from data4library.entities import (
    Book,
    Library,
)


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
        return response.json()['response']

    def get_libraries(self):
        response = self.send('libSrch')
        return [
            Library.read(lib['lib'])
            for lib in response['libs']
        ]

    def get_book_detail(self, isbn13):
        response = self.send('srchDtlList',
                             isbn13=isbn13,
                             loaninfoYN='N')
        return Book.read(response['detail'][0]['book'])
