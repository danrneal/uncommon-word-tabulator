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

        # He also notices that common words like "that" aren't in the output.
        self.assertNotIn('that', output)

    def test_invalid_number_of_arguments(self):
        # Abe tries a new txt file but forgets to delete the old txt file. A
        # helpful message appears.
        output = subprocess.check_output(
            'python uncommonwords.py common.txt alice.txt alice2.txt',
            stderr=subprocess.STDOUT,
            shell=True
        ).decode(sys.stdout.encoding)
        self.assertEqual(
            output.strip(),
            "Usage: uncommonwords.py common_words_file text_file"
        )

    def test_file_not_found(self):
        # Abe tries again but the new text file is not where it is expected
        # to be and he sees a message telling him as much
        output = subprocess.check_output(
            'python uncommonwords.py common.txt nonexistantfile',
            stderr=subprocess.STDOUT,
            shell=True
        ).decode(sys.stdout.encoding)
        self.assertIn("No such file or directory:", output)
