import requests

from data4library.utils import to_camel_case
from data4library.entities import (
    make_entity,
    Book,
    Library,
    PopularLoan,
)


class ClientException(Exception):
    pass


class Paginator:
    def __init__(self, client, action, params=None, page_size=10):
        '''
        :param client: a client
        :type client: Client
        :param action: an action name
        :type action: str
        :param params: parameters
        :type params: dict
        '''
        self.client = client
        self.page = 1
        self.action = action
        self.params = params or {}
        self.page_size = page_size

    def __iter__(self):
        while True:
            if not self.page:
                return

            response = self.client.send(self.action,
                                        page_no=self.page,
                                        page_size=self.page_size,
                                        **self.params)
            yield response

            if response.get('pageNo') == self.page:
                return
            self.update_page(response)

    def update_page(self, response):
        result_num = response['resultNum']
        if result_num < self.page_size:
            self.page = None
            return

        self.page += 1


class Client:
    base_url = 'http://data4library.kr/api'

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()

    def send(self, action, **options):
        url = f'{self.base_url}/{action}'
        params = {
            'authKey': self.api_key,
            'format': 'json',
            **{
                to_camel_case(k): v
                for k, v in options.items()
            }
        }
        response = requests.get(url, params)
        if response.status_code != 200:
            raise ClientException(response.content)

        content = response.json()
        if 'error' in content['response']:
            raise ClientException(content['response']['error'])

        return content['response']

    def get_libraries(self):
        paginator = Paginator(self, 'libSrch')
        for page in paginator:
            for lib in page['libs']:
                yield make_entity(Library, lib['lib'])

    def get_book_detail(self, isbn13):
        response = self.send('srchDtlList',
                             isbn13=isbn13,
                             loaninfoYN='N')
        return make_entity(Book, response['detail'][0]['book'])

    def get_popular_loans(self):
        paginator = Paginator(self, 'loanItemSrch', page_size=300)
        for page in paginator:
            for doc in page['docs']:
                yield make_entity(PopularLoan, doc['doc'])
