import json
from .conftest import read_fixture


def test_get_libraries_fixture():
    text = read_fixture('search_libraries_response.txt')
    content = json.loads(text)
    assert 'response' in content

    resp = content['response']
    assert resp['numFound'] == 1047
    assert resp['pageNo'] == 1
    assert resp['pageSize'] == 10
    assert resp['resultNum'] == 10
    assert resp['request'] == {'pageNo': '1', 'pageSize': '10'}


def test_get_libraries(requests_mock, client):
    requests_mock.get(
        'http://data4library.kr/api/libSrch',
        text=read_fixture('search_libraries_response.txt')
    )

    libs = client.get_libraries()
    assert len(libs) == 10


def test_get_book_detail(requests_mock, client):
    requests_mock.get(
        'http://data4library.kr/api/srchDtlList',
        text=read_fixture('get_book_detail_response.txt')
    )

    book = client.get_book_detail('9788983921987')
    assert book
    assert book.name == '해리포터와 혼혈왕자'
