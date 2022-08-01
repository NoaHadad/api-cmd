import json
from typing import Optional
from dataclasses import dataclass

@dataclass
class DataFile:

    file_name: str

    def _get_data_from_file_decorator(func) -> Optional[str]:
        def wrapper(self, *args, **kwargs):
            try:
                with open(self.file_name, 'r') as json_file:
                    data = json.load(json_file)
                kwargs['data'] = data
            except FileNotFoundError:
                kwargs['data'] = {}
            return func(self, *args, **kwargs)
        return wrapper

    def _write_new_data(self, data: dict) -> None:
        with open(self.file_name, 'w') as json_file:
            json.dump(data, json_file)

    @_get_data_from_file_decorator
    def get(self, key: str, data=None) -> str:
        try:
            val = data[key]
            return val
        except KeyError:
            return f"Key `{key}` not found!"

    @_get_data_from_file_decorator
    def set(self, key: str, val: str, data=None) -> None:
        if data.get(key) != val:
            data[key] = val
            self._write_new_data(data)

    @_get_data_from_file_decorator
    def delete(self, key: str, data=None) -> Optional[str]:
        try:
            del data[key]
            self._write_new_data(data)
            return f"Key `{key}` was deleted!"
        except KeyError:
            return f"Key `{key}` not found!"