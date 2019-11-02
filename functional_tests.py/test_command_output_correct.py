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
