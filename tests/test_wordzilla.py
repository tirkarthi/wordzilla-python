import argparse
import unittest
import wordzilla.wordzilla as wz
from wordzilla import check_word, get_meanings

parser = wz.parser

class WordzillaTest(unittest.TestCase):

    def setUp(self):
        self.all_pronouns_meanings_we = filter(
            lambda part: part[0] == 'Pronoun', get_meanings('we', 'pronoun'))
        self.all_noun_meanings_we = filter(
            lambda part: part[0] == 'Noun', get_meanings('we', 'pronoun'))

    @classmethod
    def tearDownClass(cls):
        pass

    def test_check_word(self):
        self.assertFalse(check_word('34we'))
        self.assertFalse(check_word('we-'))
        self.assertTrue(check_word('we'))
        self.assertTrue(check_word('wEer'))

    def test_get_meanings(self):
        self.failUnlessEqual(len(list(get_meanings('we'))), 4)
        self.failUnlessEqual(len(list(get_meanings('we', 'pronoun'))), 3)
        self.failUnlessEqual(len(self.all_pronouns_meanings_we), 3)
        self.failUnlessEqual(len(self.all_noun_meanings_we), 0)
        self.failUnlessEqual(len(list(get_meanings())), 5)
        self.failUnlessEqual(len(list(get_meanings('wEer'))), 1)
        self.failUnlessEqual(len(list(get_meanings('wEerw'))), 0)


class WordzillaOptionParseTest(unittest.TestCase):

    def setUp(self):
        self.commandline_args_with_color = ['-c']
        self.commandline_args_without_color = ['-n', '5']
        self.commandline_args_with_number_of_meanings = ['-c', '-n', '10']
        self.commandline_args_without_number_of_meanings = ['-c', ]
        self.commandline_args_with_part_of_speech = ['-c', '-p', 'pronoun']
        self.commandline_args_without_part_of_speech = ['-c']

    def test_option_parser(self):
        options = parser.parse_args(self.commandline_args_with_color)
        self.assertTrue(options.colored_output)

        options = parser.parse_args(self.commandline_args_without_color)
        self.assertFalse(options.colored_output)

        options = parser.parse_args(
            self.commandline_args_with_number_of_meanings)
        self.failUnlessEqual(options.number_of_meanings, 10)

        options = parser.parse_args(
            self.commandline_args_without_number_of_meanings)
        self.failUnlessEqual(options.number_of_meanings, 5)

        options = parser.parse_args(self.commandline_args_with_part_of_speech)
        self.failUnlessEqual(options.part_of_speech, 'pronoun')

        options = parser.parse_args(
            self.commandline_args_without_part_of_speech)
        self.failUnlessEqual(options.part_of_speech, 'default_part_of_speech')

if __name__ == "__main__":
    unittest.main()
