import re
import sys


def get_words_from_file(filename):
    try:
        with open(filename) as f:
            words = re.findall(r"[\w']+", f.read().lower())
            while "'" in words:
                words.remove("'")
            return words
    except FileNotFoundError as err:
        print(err, file=sys.stderr)
        sys.exit()


def count_uncommon_words(common_words, text):
    uncommon_words = {}
    for word in text:
        if word not in common_words and word not in uncommon_words:
            uncommon_words[word] = 1
        elif word not in common_words:
            uncommon_words[word] += 1
    return uncommon_words


def sort_and_format_output(uncommon_words):
    line_length = (((
        len(max(uncommon_words, key=len)) + 2 +
        len(str(max(uncommon_words.values())))
    ) // 4) + 1) * 4
    sorted_uncommon_words = sorted(
        uncommon_words.items(),
        key=lambda kv: kv[1],
        reverse=True
    )
    output = ''
    for word, occurrences in sorted_uncommon_words:
        num_spaces = line_length - len(word) - len(str(occurrences)) - 1
        output += f"{word.capitalize()}:{' ' * num_spaces}{occurrences}\n"
    output = output[:-1]
    return output


def tabulate_words():
    if len(sys.argv) != 3:
        print(
            f"Usage: {sys.argv[0]} common_words_file text_file",
            file=sys.stderr
        )
    else:
        common_words = get_words_from_file(sys.argv[1])
        text = get_words_from_file(sys.argv[2])
        uncommon_words = count_uncommon_words(common_words, text)
        output = sort_and_format_output(uncommon_words)
        print(output)


if __name__ == '__main__':
    tabulate_words()
