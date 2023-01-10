import pytest
from scripts.generate_diff import gendiff


@pytest.fixture
def file1_json_flat():
  return 'tests/fixtures/file1-flat.json'


@pytest.fixture
def file2_json_flat():
  return 'tests/fixtures/file2-flat.json'


@pytest.fixture
def file1_yaml_flat():
  return 'tests/fixtures/file1-flat.yaml'


@pytest.fixture
def file2_yaml_flat():
  return 'tests/fixtures/file2-flat.yaml'


@pytest.fixture
def file1_json_tree():
  return 'tests/fixtures/file1-tree.json'


@pytest.fixture
def file2_json_tree():
  return 'tests/fixtures/file2-tree.json'


@pytest.fixture
def file1_plus_file2_flatten():
  with open('tests/fixtures/expected/file1_plus_file2_flatten.txt') as f:
    return f.read()


@pytest.fixture
def file1_plus_file2_tree():
  with open('tests/fixtures/expected/file1_plus_file2_tree.txt') as f:
    return f.read()


def test_file1_plus_file2_flatten_json_diff(file1_json_flat, file2_json_flat, file1_plus_file2_flatten):
  assert file1_plus_file2_flatten == gendiff(file1_json_flat, file2_json_flat)


def test_file1_plus_file2_flatten_yaml_diff(file1_yaml_flat, file2_yaml_flat, file1_plus_file2_flatten):
  assert file1_plus_file2_flatten == gendiff(file1_yaml_flat, file2_yaml_flat)


def test_file1_plus_file2_tree_json_diff(file1_json_tree, file2_json_tree, file1_plus_file2_tree):
  assert file1_plus_file2_tree == gendiff(file1_json_tree, file2_json_tree)