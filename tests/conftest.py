from importlib.resources import read_text

import pytest

from data4library.client import Client


def read_fixture(name):
    return read_text('tests.fixtures', name)


@pytest.fixture
def client():
    return Client('fake-key')
