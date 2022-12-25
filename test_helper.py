from helper import getModelSpacy, getSpellChecker
import unittest
import sys
sys.path.insert(
    0, '/home/thek/Desktop/LinguisticCluesTool-main/LinguisticCluesTool-main/sample/')


class TestUtils(unittest.TestCase):

    def test_getModelSpacy(self):
        '''Test case function for get model from spacy'''
        actual = str(type(getModelSpacy()))
        expected = "<class 'spacy.lang.pt.Portuguese'>"
        self.assertEqual(actual, expected)

    def test_getSpellChecker(self):
        '''Test case function for get dictionary'''
        actual = str(type(getSpellChecker(
            "/home/thek/Desktop/LinguisticCluesTool-main/LinguisticCluesTool-main/softmaker-hunspell-portuguese-br-101.sox")))
        expected = "<class 'spylls.hunspell.dictionary.Dictionary'>"
        self.assertEqual(actual, expected)
