from dataclasses import dataclass
from dataclasses import fields


def map_dict_to_entity(clazz, data, mapping):
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

    @staticmethod
    def read(data):
        mapping = {
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
        }

        return map_dict_to_entity(Library, data, mapping)


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

    @staticmethod
    def read(data):
        mapping = {
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
        }

        return map_dict_to_entity(Book, data, mapping)
