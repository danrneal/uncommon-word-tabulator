import unittest
from unittest.mock import mock_open, patch
from uncommonwords import (
    get_words_from_file, count_uncommon_words, sort_and_format_output,
    tabulate_words
)


@patch(
    'builtins.open',
    new_callable=mock_open,
    read_data="These\nare some words, aren't they?"
)
class GetWordsFromFileTest(unittest.TestCase):

    def test_common_words_are_loaded_into_a_list(self, mock_with_open):
        common_words = get_words_from_file('words.txt')
        mock_with_open.assert_called_once_with('words.txt')
        self.assertEqual(
            common_words,
            ['these', 'are', 'some', 'words', "aren't", 'they']
        )


class CountUncommonWordsTest(unittest.TestCase):

    def test_uncommon_words_are_properly_counted(self):
        common_words = ["common", "words"]
        text = ["some", "words", "are", "common", "some", "words", "are", "not"]
        uncommon_words = count_uncommon_words(common_words, text)
        self.assertEqual(uncommon_words, {
            "some": 2,
            "are": 2,
            "not": 1
        })


class SortAndFormatOutputTest(unittest.TestCase):

    def test_words_are_sorted_and_formatted(self):
        uncommon_words = {
            'some': 1,
            'very': 5,
            'uncommon': 2,
            'words': 3
        }
        output = sort_and_format_output(uncommon_words)
        self.assertEqual(
            output,
            "Very:      5\nWords:     3\nUncommon:  2\nSome:      1")


@patch('builtins.print')
@patch('uncommonwords.sort_and_format_output')
@patch('uncommonwords.count_uncommon_words')
@patch('uncommonwords.get_words_from_file')
class TabulateWordsTest(unittest.TestCase):

    @patch('uncommonwords.sys.argv', ['', 'common.txt', 'alice.txt'])
    def test_correct_output_is_printed(
        self, mock_get_words_from_file, mock_count_uncommon_words,
        mock_sort_and_format_output, mock_print
    ):
        common_words = ["common", "words"]
        text = ["some", "words", "are", "common", "some", "words", "are", "not"]
        mock_get_words_from_file.side_effect = [common_words, text]
        uncommon_words = {
            "some": 2,
            "are": 2,
            "not": 1
        }
        mock_count_uncommon_words.return_value = uncommon_words
        output = "Some:  2\nAre:   2\nNot:   1"
        mock_sort_and_format_output.return_value = output

        tabulate_words()

        mock_get_words_from_file.assert_called_with('alice.txt')
        mock_count_uncommon_words.assert_called_once_with(common_words, text)
        mock_sort_and_format_output.assert_called_once_with(uncommon_words)
        mock_print.assert_called_once_with(output)
