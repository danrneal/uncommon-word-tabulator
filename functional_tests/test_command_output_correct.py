import subprocess
import sys
import unittest


class OutputTest(unittest.TestCase):

    def test_cli_takes_txt_file_and_delivers_correct_tabulation(self):
        # Abe wants to know how many times a the word 'Alice' appears in
        # alice.txt. He types the appropriate command and discovers the
        # answer in the output.
        output = subprocess.check_output(
            'python uncommonwords.py common.txt alice.txt',
            stderr=subprocess.STDOUT,
            shell=True
        ).decode(sys.stdout.encoding)
        self.assertIn('Alice:           386', output)

    def test_invalid_number_of_arguments(self):
        # Abe tries a new txt file but forgets to delete the old txt file. A
        # helpful message appears.
        output = subprocess.check_output(
            'python uncommonwords.py common.txt alice.txt alice2.txt',
            stderr=subprocess.STDOUT,
            shell=True
        ).decode(sys.stdout.encoding)
        self.assertEqual(
            output,
            "usage: uncommonwords common_words_file text_file"
        )
