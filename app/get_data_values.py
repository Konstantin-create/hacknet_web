import os


class Data:
    elements_path = f'{os.path.dirname(__file__)}/data/elements/'  # Path to elements

    header_text = open(f'{elements_path}/HEADER_TEXT', 'r').read()
    about_text = open(f'{elements_path}/ABOUT_TEXT', 'r').read()
