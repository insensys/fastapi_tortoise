import pytest
from src.services.request import get_invoices


def test_api():
    url = get_invoices()
    print(url)
    assert isinstance(url, str) and url