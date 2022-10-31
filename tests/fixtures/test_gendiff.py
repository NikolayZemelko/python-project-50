from gendiff.scripts.gendiff import generate_diff
import pytest

@pytest.fixture
def files():
    return [
    {
      "host": "hexlet.io",
      "timeout": 50,
      "proxy": "123.234.53.22",
      "follow": "false"
    },
    {
      "timeout": 20,
      "verbose": "true",
      "host": "hexlet.io"
    }
]

def test_if_first_file_empty(files):
    file1 = dict()
    file2 = files[1]

    assert generate_diff(file1, file2) == """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""
