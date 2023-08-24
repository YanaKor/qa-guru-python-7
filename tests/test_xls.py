import xlrd
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

xls_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources', 'file_example_XLS_10.xls'))


def test_xls_file():

    book = xlrd.open_workbook(xls_path)
    num_sheets = book.nsheets
    sheets = book.sheet_names()

    assert num_sheets == 1
    assert sheets == ['Sheet1']
