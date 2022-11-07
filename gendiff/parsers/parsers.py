import json
import yaml
from pathlib import Path


def get_yaml_types():
    return ['.yaml', '.yml']


def get_json_types():
    return ['.json']


def loader(file1, file2):

    yaml_types = get_yaml_types()
    json_types = get_json_types()

    if Path(file1).suffix in yaml_types:

        r1 = yaml.safe_load(open(file1)) or dict()
        r2 = yaml.safe_load(open(file2)) or dict()

    elif Path(file1).suffix in json_types:

        r1 = json.load(open(file1)) or dict()
        r2 = json.load(open(file2)) or dict()

    return [r1, r2]


def parsed_files(f1, f2):

    files = []

    if isinstance(f1, str) and isinstance(f2, str):

        files.append(loader(f1, f2))

    elif isinstance(f1, dict) and isinstance(f2, dict):
        files.append(f1)
        files.append(f2)

    return files
