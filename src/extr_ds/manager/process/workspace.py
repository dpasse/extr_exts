from typing import Any, Dict

import os
import json


WORKSPACE = os.getcwd()

def load_config() -> Dict[str, Any]:
    with open(os.path.join(WORKSPACE, 'extr-config.json'), 'r', encoding='utf-8') as config_file:
        return json.loads(config_file.read())

def save_config(config: Dict[str, Any]) -> None:
    with open(os.path.join(WORKSPACE, 'extr-config.json'), 'w', encoding='utf-8') as config_file:
        config_file.write(
            json.dumps(config, indent=2)
        )

def create_source_file():
    config = load_config()
    file_path = os.path.join(WORKSPACE, '1', config['source'])
    with open(file_path, 'w', encoding='utf-8') as source_file:
        source_file.write('')

def create_labels_file():
    src = """from typing import Dict, List, Tuple
import re

from extr.regexes import RegEx, RegExLabel
from extr.relations import RegExRelationLabelBuilder


## ENTITIES
kb: Dict[str, List[str]]= {}
entity_patterns: List[RegExLabel] = []

## RELATIONS
relation_patterns: List[RegExLabel] = []

## ie. ('PERSON', 'ORG', 'NO_RELATION')
relation_defaults: List[Tuple[str, str, str]] = []
"""

    file_path = os.path.join(WORKSPACE, 'labels.py')
    with open(file_path, 'w', encoding='utf-8') as labels_file:
        labels_file.write(src)

def create_utils_file():
    src = """from typing import List


def sentence_tokenizer(text: str) -> List[List[str]]:
    return [
        text.split(' ')
    ]

def transform_text(text: str) -> str:
    return text
"""

    file_path = os.path.join(WORKSPACE, 'utils.py')
    with open(file_path, 'w', encoding='utf-8') as utils_file:
        utils_file.write(src)

def init() -> None:
    save_config({
        'source': 'source.txt',
        'split': {
            'amount': 25
        },
        'annotations': {
            'enable-html': True,
            'filter-redactions': True,
        }
    })

    directories = ['1', '2', '3', '4']

    for folder in directories:
        directory = os.path.join(WORKSPACE, folder)
        if not os.path.exists(directory):
            os.mkdir(directory)

    create_source_file()
    create_labels_file()
    create_utils_file()

def clean() -> None:
    files = [
        os.path.join(WORKSPACE, '4', 'ents.txt'),
        os.path.join(WORKSPACE, '4', 'ents-redacted.txt'),
        os.path.join(WORKSPACE, '4', 'rels.txt'),
    ]

    for file in files:
        if os.path.exists(file):
            os.remove(file)
