import pytest
from click.testing import CliRunner
from key_value import cli

runner = CliRunner()

def test__set__happy_flow():
  result = runner.invoke(cli, ['set-value', '--key', 'key', '--value', 'val', '--file', pytest.file_name])
  assert result.exit_code == 0

def test__set__missing_options():
  result = runner.invoke(cli, ['set-value', '--value', 'val', '--file', pytest.file_name])
  assert result.exit_code == 2
  result = runner.invoke(cli, ['set-value', '--key', 'key', '--file', pytest.file_name])
  assert result.exit_code == 2
  result = runner.invoke(cli, ['set-value', '--key', 'key', '--value', 'val'])
  assert result.exit_code == 2

def test__get__happy_flow(data_file_instance):
  result = runner.invoke(cli, ['get-value', '--key', 'key', '--file', pytest.file_name])
  assert result.exit_code == 0
  assert result.output == 'val\n'

def test__get__key_not_found():
  result = runner.invoke(cli, ['get-value', '--key', 'key1', '--file', pytest.file_name])
  assert result.exit_code == 0
  assert result.output == 'Key `key1` not found!\n'

def test__get__missing_options():
  result = runner.invoke(cli, ['get-value','--key', 'key1'])
  assert result.exit_code == 2
  result = runner.invoke(cli, ['get-value', '--file', pytest.file_name])
  assert result.exit_code == 2

def test__delete__happy_flow(data_file_instance):
  result = runner.invoke(cli, ['delete-value', '--key', 'key', '--file', pytest.file_name])
  assert result.exit_code == 0
  assert result.output == 'Key `key` was deleted!\n'

def test__delete__key_not_found():
  result = runner.invoke(cli, ['delete-value', '--key', 'key1', '--file', pytest.file_name])
  assert result.exit_code == 0
  assert result.output == 'Key `key1` not found!\n'

def test__delete__missing_options():
  result = runner.invoke(cli, ['delete-value','--key', 'key1'])
  assert result.exit_code == 2
  result = runner.invoke(cli, ['delete-value', '--file', pytest.file_name])
  assert result.exit_code == 2