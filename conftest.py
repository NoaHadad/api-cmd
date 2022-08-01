import pytest
import json
import os

from data_file import DataFile

FILE_NAME = 'test.json'

@pytest.fixture
def data_file_instance():
    pytest.file_name = FILE_NAME
    with open(pytest.file_name, 'w') as f:
        json.dump({'key':'val'},f)
    data_file_instance = DataFile(pytest.file_name)
    yield data_file_instance
    os.remove(pytest.file_name)