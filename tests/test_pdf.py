import pypdf
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources', 'docs-pytest-org-en-latest.pdf'))


def test_number_of_pages():
    reader = pypdf.PdfReader(pdf_path)
    number_of_pages = len(reader.pages)

    assert number_of_pages == 412


def test_text_on_main_page():
    reader = pypdf.PdfReader(pdf_path)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    assert 'pytest Documentation' in text


