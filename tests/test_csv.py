import csv
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'new_csv.csv')


def test_write_info_to_csv_file():
    with open(csv_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

        assert os.path.exists(csv_file)


def test_open_csv_file():
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile)
        rows = []
        for row in csvreader:
            if len(row) > 0:
               rows.append(row)

    assert len(rows) == 2

