from data4library.utils import to_camel_case


def test_to_camel_case():
    assert to_camel_case('auth_key') == 'authKey'
    assert to_camel_case('page_size') == 'pageSize'
    assert to_camel_case('page_no') == 'pageNo'
