import os
import zipfile

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

resources_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
resources_files = os.listdir(resources_folder)
archive_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'arch.zip')


def test_zip():
    with zipfile.ZipFile('./resources/arch.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in resources_files:
            add_file = os.path.join(resources_folder, file)
            zf.write(add_file, arcname=file)

    with zipfile.ZipFile(archive_file) as zf:
        assert len(resources_files) == len(zf.infolist())
        for file in resources_files:
            inform = zf.getinfo(file)
            assert file == inform.filename




