import pytest
import json

def get_data(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def test_set(data_file_instance):
    def run_test(key, val):
        data_file_instance.set(key, val)
        data = get_data(pytest.file_name)
        assert data[key] == val
    run_test('key','val1')
    run_test('key1','val1')


def test_get(data_file_instance):
    assert data_file_instance.get('key') == 'val'
    assert data_file_instance.get('key1') == 'Key `key1` not found!'


def test_delete(data_file_instance):
    assert data_file_instance.delete('key') == 'Key `key` was deleted!'
    data = get_data(pytest.file_name)
    assert data.get('key') == None
    assert data_file_instance.delete('key') == 'Key `key` not found!'