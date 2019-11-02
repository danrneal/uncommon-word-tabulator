import re


def get_words_from_file(filename):
    with open(filename) as f:
        return re.findall(r'\w+', f.read().lower())
