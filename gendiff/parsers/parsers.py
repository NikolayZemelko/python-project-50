import json
import yaml
from pathlib import Path


def json_loader(file):
    r = json.load(open(file))
    return dict() if r is None else r


def yaml_loader(file):
    r = yaml.safe_load(open(file))
    return dict() if r is None else r


def get_yaml_types():
    return ['.yaml', '.yml']


def get_json_types():
    return ['.json']


def parsed_files(f1, f2):

    yaml_types = get_yaml_types()
    json_types = get_json_types()
    files = []

    if isinstance(f1, str) and isinstance(f2, str):

        if Path(f1).suffix in yaml_types:
            file1 = yaml_loader(f1)
            file2 = yaml_loader(f2)

        elif Path(f1).suffix in json_types:
            file1 = json_loader(f1)
            file2 = json_loader(f2)

    elif isinstance(f1, dict) and isinstance(f2, dict):
        file1 = f1
        file2 = f2

    files.append(file1)
    files.append(file2)

    return files
