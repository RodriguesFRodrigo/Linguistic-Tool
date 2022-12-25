import os
import pandas as pd
import spacy
from spylls.hunspell import Dictionary
import sys
from metaInformation import (
    MetaInformation,
)
from tipsLinguistics import (
    TipsLinguistics,
)
from helper import *
from leia import SentimentIntensityAnalyzer


class App:
    def __init__(self, args):
        self.__typeDataset = args[1].lower()  # .txt, .csv, .tsv
        self.__datasetPath = args[2]
        self.__datasetName = args[3]
        self.__totalTextsDataset = int(args[4])
        self.__dictName = args[5]
        self.__columnWithTexts = args[6]
        self.__columnWithClassification = args[7]
        self._textsForProcessing = args[8]
        self.__nlp = spacy.load("pt_core_news_sm")
        self.__dictonary = Dictionary.from_zip(self.__dictName)
        self.__sentimentIntensityAnalyzer = SentimentIntensityAnalyzer()
        self.__metaInformation = MetaInformation()
        self.processTexts()
        self.__metaInformation.printMetaInformation()
        self.__tipslinguistics = TipsLinguistics(
            self.__metaInformation, self.__totalTextsDataset
        )

    def getTexts(self, df):
        texts = df.loc[
            df[self.__columnWithClassification]
            == self._textsForProcessing,
            self.__columnWithTexts,
        ]
        return texts

    def processTexts(self):

        if self.__typeDataset == "txt":
            for i in range(1, self.__totalTextsDataset):
                try:
                    pathFromFile = self.__datasetPath + "/" + str(i) + ".txt"
                    fileRead = open(pathFromFile, "r", encoding="utf-8")
                    text = fileRead.read()
                    self.getMetaInformation(text)
                    print(i)
                    i += 1
                except FileNotFoundError:
                    print("\t*** WARNING: Error reading file!")

        if self.__typeDataset == "xlsx":
            try:
                df = pd.read_excel(self.__datasetName)
                texts = self.getTexts(df)
                for text in texts:
                    self.getMetaInformation(text)
            except:
                print("\t**** WARNING: Error opening dataset!")
                raise

        if self.__typeDataset == "csv":
            try:
                df = pd.read_csv(self.__datasetName)
                texts = self.getTexts(df)
                i = 0
                for text in texts:
                    self.getMetaInformation(text)
                    print(i)
                    i += 1
            except:
                print("\t****WARNING: Error opening dataset!")
                raise

    def getMetaInformation(self, text):
        # Limpeza para todos os textos
        text = remove_emojis(text)
        text = removeUnicodeControlCharacters(text)
        # text = removeSymbolsBert(text)
        self.__metaInformation.setTokens(self.__nlp, text)
        self.__metaInformation.setTypes(self.__nlp, text)
        self.__metaInformation.setLinks(self.__nlp, text)
        self.__metaInformation.setUppercaseWords(self.__nlp, text)
        self.__metaInformation.setWords(self.__nlp, text)
        self.__metaInformation.setSentences(self.__nlp, text)
        self.__metaInformation.setChars(self.__nlp, text)
        self.__metaInformation.setPunctuationMarks(self.__nlp, text)
        self.__metaInformation.setVerbs(self.__nlp, text)
        self.__metaInformation.setVerbsAux(self.__nlp, text)
        self.__metaInformation.setNouns(self.__nlp, text)
        self.__metaInformation.setPropNouns(self.__nlp, text)
        self.__metaInformation.setAdj(self.__nlp, text)
        self.__metaInformation.setAdjDet(self.__nlp, text)
        self.__metaInformation.setAdjNun(self.__nlp, text)
        self.__metaInformation.setAdv(self.__nlp, text)
        self.__metaInformation.setPron(self.__nlp, text)
        self.__metaInformation.setStopWords(self.__nlp, text)
        self.__metaInformation.setModalverbs(self.__nlp, text)
        self.__metaInformation.setFirstPronounSingular(
            self.__nlp, text, getPronouns("1s"))
        self.__metaInformation.setFirstPronounPlural(
            self.__nlp, text, getPronouns("1p"))
        self.__metaInformation.setSecondPronounSingular(
            self.__nlp, text, getPronouns("2s"))
        self.__metaInformation.setSecondPronounPlural(
            self.__nlp, text, getPronouns("2p"))
        self.__metaInformation.setThirdPronounSingular(
            self.__nlp, text, getPronouns("3s"))
        self.__metaInformation.setThirdPronounPlural(
            self.__nlp, text, getPronouns("3p"))
        self.__metaInformation.setMisspelledWords(
            self.__nlp, self.__dictonary, text)
        self.__metaInformation.setPolarity(
            self.__sentimentIntensityAnalyzer, text)
        self.__metaInformation.setOwnNames(self.__nlp, text)
        self.__metaInformation.setQuestionMarks(self.__nlp, text)
        self.__metaInformation.setExclamationPoints(self.__nlp, text)


if __name__ == "__main__":
    main = App(sys.argv)
