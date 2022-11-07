from gendiff.scripts.gendiff import generate_diff
import pytest
import json
from gendiff.parsers.parsers import json_loader, yaml_loader


@pytest.fixture
def json_files():
    file1 = json_loader('gendiff/files/file1.json')
    file2 = json_loader('gendiff/files/file2.json')
    return [file1, file2]


@pytest.fixture
def yaml_files():
    file1 = yaml_loader('gendiff/files/file3.yml')
    file2 = yaml_loader('gendiff/files/file4.yaml')
    return [file1, file2]


def test_if_first_json_file_empty(json_files):
    file1 = dict()
    file2 = json_files[1]

    assert generate_diff(file1, file2) == """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""


def test_if_second_json_file_empty(json_files):
    file1 = json_files[0]
    file2 = dict()

    assert generate_diff(file1, file2) == """{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""


def test_if_first_yaml_file_empty(yaml_files):
    file1 = dict()
    file2 = yaml_files[1]

    assert generate_diff(file1, file2) == """{
  + host: hexlet.io
  + timeout: 20
  + verbose: True
}"""


def test_if_second_yaml_file_empty(yaml_files):
    file1 = yaml_files[0]
    file2 = dict()

    assert generate_diff(file1, file2) == """{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""
