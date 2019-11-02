import unittest
from unittest.mock import mock_open, patch
from uncommonwords import get_words_from_file, count_uncommon_words

@patch(
    'builtins.open',
    new_callable=mock_open,
    read_data="These\nare some words."
)
class GetWordsFromFileTest(unittest.TestCase):

    def test_common_words_are_loaded_into_a_list(self, mock_with_open):
        common_words = get_words_from_file('words.txt')
        mock_with_open.assert_called_once_with('words.txt')
        self.assertEqual(common_words, ['these', 'are', 'some', 'words'])


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
