import json


def edit_content(new_data: dict):
    """Function to edit content config file"""

    json.dump(new_data, open('app/data/content.json', 'w'))


def get_content() -> dict:
    """Function to get content from config file"""

    return json.load(open('app/data/content.json', 'r'))
