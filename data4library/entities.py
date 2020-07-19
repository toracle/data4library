from dataclasses import dataclass
from dataclasses import fields


DICT_TO_ENTITY_MAP = {
    'Library': {
        'libCode': 'code',
        'libName': 'name',
        'address': 'address',
        'BookCount': 'book_count',
        'closed': 'closed',
        'fax': 'fax',
        'homepage': 'homepage',
        'latitude': ('latitude', float),
        'longitude': ('longitude', float),
        'operatingTime': 'operating_time',
        'tel': 'tel',
    },
    'Book': {
        'isbn': 'isbn',
        'isbn13': 'isbn13',
        'bookname': 'name',
        'publication_year': 'publication_year',
        'publication_date': 'publication_date',
        'authors': 'authors',
        'publisher': 'publisher',
        'class_no': 'class_no',
        'bookImageURL': 'image_url',
        'description': 'description',
    },
    'PopularLoan': {
        'ranking': 'ranking',
        'bookname': 'name',
        'authors': 'authors',
        'publisher': 'publisher',
        'publication_year': 'publication_year',
        'vol': 'vol',
        'isbn13': 'isbn13',
        'class_no': 'class_no',
        'loan_count': 'loan_count',
        'bookImageURL': 'image_url',
    }
}


def make_entity(clazz, data):
    mapping = DICT_TO_ENTITY_MAP.get(clazz.__name__)

    initials = {}
    for from_field_name, field_value in data.items():
        if from_field_name not in mapping:
            continue

        field_def = mapping[from_field_name]
        if isinstance(field_def, (list, tuple)):
            to_field_name, typ = field_def
            initials[to_field_name] = typ(field_value)
        else:
            to_field_name = field_def
            initials[to_field_name] = field_value

    d = [
        initials[field.name]
        for field in fields(clazz)
    ]
    return clazz(*d)


@dataclass
class Library:
    code: str
    name: str
    address: str
    book_count: int
    closed: str
    fax: str
    homepage: str
    latitude: float
    longitude: float
    operating_time: str
    tel: str


@dataclass
class Book:
    isbn: str
    isbn13: str
    name: str
    publication_year: str
    publication_date: str
    authors: str
    publisher: str
    class_no: str
    image_url: str
    description: str


@dataclass
class PopularLoan:
    ranking: int
    name: str
    authors: str
    publisher: str
    publication_year: str
    isbn13: str
    vol: str
    class_no: str
    loan_count: int
    image_url: str
