import unittest
from metaInformation import MetaInformation
from helper import *


class TestUtils(unittest.TestCase):

    def test_setTokens(self):
        '''Test case function for set tokens'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setTokens(getModelSpacy(
        ), "Renata Fan sofre com corte no Jogo Aberto, reúne equipe e confirma desfecho na Band.")
        expected = 17
        self.assertEqual(actual, expected)

    def test_setTypes(self):
        '''Test case function for set types (unique words)'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setTypes(getModelSpacy(
        ), "Renata Fan sofre com corte no Jogo Aberto, reúne equipe e confirma desfecho na Band. Renata Fan sofre com corte no Jogo Aberto, reúne equipe e confirma desfecho na Band.")
        expected = 17
        self.assertEqual(actual, expected)

    def test_setLinks(self):
        '''Test case function for set links (URL)'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setLinks(
            getModelSpacy(), "Confira em: https://ge.globo.com/")
        expected = 1
        self.assertEqual(actual, expected)

    def test_setUpper(self):
        '''Test case function for uppercase words'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setUppercaseWords(
            getModelSpacy(), "THE ROCK é maior que VIN")
        expected = 3
        self.assertEqual(actual, expected)

    # def test_setWords

    def test_setSentences(self):
        '''Test case function for sentences'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setSentences(
            getModelSpacy(), "THE ROCK é maior que VIN. Contudo, VIN é mais forte!")
        expected = 2
        self.assertEqual(actual, expected)

    def test_setCharacters(self):
        '''Test case function for characters'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setChars(
            getModelSpacy(), "THE ROCK é maior que VIN. Contudo, VIN é mais forte!")
        expected = 42
        self.assertEqual(actual, expected)

    def test_setPunctuationMarks(self):
        '''Test case function for punctuation marks'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setPunctuationMarks(
            getModelSpacy(), "THE ROCK é maior que VIN. Contudo, VIN é mais forte!")
        expected = 3
        self.assertEqual(actual, expected)

    def test_setVerbs(self):
        '''Test case function for verbs'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setVerbs(
            getModelSpacy(), "Ele deu uma caneta e caiu")
        expected = 2
        self.assertEqual(actual, expected)

    def test_setAuxVerbs(self):
        '''Test case function for aux verbs'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setVerbsAux(getModelSpacy(
        ), "O Andriell podia ter estado a ler um livro. O Pablo acabou por ter de começar a ler o livro. Este livro deve poder começar a ser lido pelos alunos")
        expected = 2
        self.assertEqual(actual, expected)

    def test_setNouns(self):
        '''Test case function for nouns'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setNouns(
            getModelSpacy(), "Ela é minha convidada.")
        expected = 1
        self.assertEqual(actual, expected)

    def test_setPropNouns(self):
        '''Test case function for prop nouns'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setPropNouns(
            getModelSpacy(), "Juliana é minha convidada")
        expected = 1
        self.assertEqual(actual, expected)

    def test_setAdj(self):
        '''Test case function for adjectives'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setAdj(getModelSpacy(), "Moça bonita.")
        expected = 1
        self.assertEqual(actual, expected)

    def test_setAdj(self):
        '''Test case function for adverbs'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setAdv(
            getModelSpacy(), "Sempre trabalhou muito.")
        expected = 2
        self.assertEqual(actual, expected)

    def test_setStopWords(self):
        '''Test case function for stop words'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setStopWords(
            getModelSpacy(), "Era essa.")
        expected = 2
        self.assertEqual(actual, expected)

    def test_setFirstPronounSingular(self):
        '''Test case function for first Pronoun Singular'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setFirstPronounSingular(
            getModelSpacy(), "eu estou com fome!",  ("eu", "me", "mim", "comigo"))
        expected = 1
        self.assertEqual(actual, expected)

    def test_setMisspelledWords(self):
        '''Test case function for misspelledwords'''
        self.metaInformation = MetaInformation()
        actual = self.metaInformation.setMisspelledWords(getModelSpacy(), getSpellChecker(
            "/home/thek/Desktop/LinguisticCluesTool-main/LinguisticCluesTool-main/softmaker-hunspell-portuguese-br-101.sox"), "Caza asul")
        expected = 2
        self.assertEqual(actual, expected)
