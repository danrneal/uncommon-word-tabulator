import re


def get_words_from_file(filename):
    with open(filename) as f:
        return re.findall(r'\w+', f.read().lower())

def count_uncommon_words(common_words, text):
    uncommon_words = {}
    for word in text:
        if word not in common_words and word not in uncommon_words:
            uncommon_words[word] = 1
        elif word not in common_words:
            uncommon_words[word] += 1
    return uncommon_words
