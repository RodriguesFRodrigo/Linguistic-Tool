from helper import *


class MetaInformation:
    def __init__(self):
        self.__tokens = 0
        self.__types = []
        self.__links = 0
        self.__capital_words = 0
        self.__words = 0
        self.__sentences = 0
        self.__characters = 0
        self.__punctuation_marks = 0
        self.__verbs = 0
        self.__nouns = 0
        self.__adjectives = 0
        self.__adverbs = 0
        self.__pronouns = 0
        self.__stopWords = 0
        self.__modal_verbs = 0
        self.__first_pronoun_singular = 0
        self.__first_pronoun_plural = 0
        self.__second_pronoun_singular = 0
        self.__second_pronoun_plural = 0
        self.__third_pronoun_singular = 0
        self.__third_pronoun_plural = 0
        self.__misspelledWords = 0
        self.__negative_content = 0
        self.__positive_content = 0
        self.__own_names = 0
        self.__exclamation_points = 0
        self.__question_marks = 0

    def setTokens(self, nlp, text):
        self.__tokens += len(nlp(text))
        return self.__tokens

    def setTypes(self, nlp, text):
        text = removeHiperlink(text)
        text = removeNumbers(text)
        text = toLowercase(text)
        doc = nlp(text)
        for token in doc:
            token = token.text
            if token not in self.__types:
                self.__types.append(token)
        return len(self.__types)

    def setLinks(self, nlp, text):
        text = toLowercase(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "LIKE_URL", True, "likeURL", text)
        self.__links += len(matcher(doc))
        return self.__links

    def setUppercaseWords(self, nlp, text):
        text = removeNumbers(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "IS_UPPER", True, "isUpper", text)
        self.__capital_words += len(matcher(doc))
        return self.__capital_words

    def setWords(self, nlp, text):
        text = removeNumbers(text)
        text = removePunctuation(text)
        self.__words += len(nlp(text))
        return self.__words

    def setSentences(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        self.__sentences += len(list(doc.sents))
        return self.__sentences

    def setChars(self, nlp, text):
        text = toLowercase(text)
        text = removeExtraSpaces(text)
        doc = nlp(text)
        amountCharacters = [len(token.text) for token in doc]
        self.__characters += sum(amountCharacters)
        return self.__characters

    def setPunctuationMarks(self, nlp, text):
        text = toLowercase(text)
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "IS_PUNCT", True, "isPunct", text)
        self.__punctuation_marks += len(matcher(doc))
        return self.__punctuation_marks

    def setVerbs(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "VERB", "isVerb", text)
        self.__verbs += len(matcher(doc))
        return self.__verbs

    def setVerbsAux(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "AUX", "isAux", text)
        self.__verbs += len(matcher(doc))
        return self.__verbs

    def setNouns(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "NOUN", "isNoun", text)
        self.__nouns += len(matcher(doc))
        return self.__nouns

    def setPropNouns(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "PROPN", "isNoun", text)
        self.__nouns += len(matcher(doc))
        return self.__nouns

    def setAdj(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "ADJ", "isAdj", text)
        self.__adjectives += len(matcher(doc))
        return self.__adjectives

    def setAdjDet(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "DET", "isPos", text)
        self.__adjectives += len(matcher(doc))
        return self.__adjectives

    def setAdjNun(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "NUM", "isNum", text)
        self.__adjectives += len(matcher(doc))
        return self.__adjectives

    def setAdv(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "ADV", "isAdv", text)
        self.__adverbs += len(matcher(doc))
        return self.__adverbs

    def setPron(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "PRON", "isPron", text)
        self.__pronouns += len(matcher(doc))
        return self.__pronouns

    def setStopWords(self, nlp, text):
        text = toLowercase(text)
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "IS_STOP", True, "isStop", text)
        self.__stopWords += len(matcher(doc))
        return self.__stopWords

    def setModalverbs(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "AUX", "isModalVerbs", text)
        self.__modal_verbs += len(matcher(doc))
        return self.__modal_verbs

    def setFirstPronounSingular(self, nlp, text, pronouns):
        text = toLowercase(text)
        self.__first_pronoun_singular += countPronouns(nlp, text, pronouns)
        return self.__first_pronoun_singular

    def setFirstPronounPlural(self, nlp, text, pronouns):
        text = toLowercase(text)
        self.__first_pronoun_plural += countPronouns(nlp, text, pronouns)
        return self.__first_pronoun_plural

    def setSecondPronounSingular(self, nlp, text, pronouns):
        text = toLowercase(text)
        self.__second_pronoun_singular += countPronouns(nlp, text, pronouns)
        return self.__second_pronoun_singular

    def setSecondPronounPlural(self, nlp, text, pronouns):
        text = toLowercase(text)
        self.__second_pronoun_plural += countPronouns(nlp, text, pronouns)
        return self.__second_pronoun_plural

    def setThirdPronounSingular(self, nlp, text, pronouns):
        text = toLowercase(text)
        self.__third_pronoun_singular += countPronouns(nlp, text, pronouns)
        return self.__third_pronoun_singular

    def setThirdPronounPlural(self, nlp, text, pronouns):
        text = toLowercase(text)
        self.__third_pronoun_plural += countPronouns(nlp, text, pronouns)
        return self.__third_pronoun_plural

    def setMisspelledWords(self, nlp, dictionary, text):
        text = removeHiperlink(text)
        text = removeNumbers(text)
        doc = nlp(text)
        list_misspelled_words = [
            token.text for token in doc if dictionary.lookup(token.text) == False]
        self.__misspelledWords += len(list_misspelled_words)
        return self.__misspelledWords

    def setPolarity(self, sentimentIntensityAnalyzer, text):
        text = removeExtraSpaces(text)
        dict_result_polarity = sentimentIntensityAnalyzer.polarity_scores(text)
        if dict_result_polarity["compound"] >= 0.05:
            self.__positive_content += 1
        if dict_result_polarity["compound"] <= -0.05:
            self.__negative_content += 1

    def setOwnNames(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "POS", "PROPN", "isPropNames", text)
        self.__own_names += len(matcher(doc))
        return self.__own_names

    def setExclamationPoints(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "ORTH", "!", "isExclamationPoints", text)
        self.__exclamation_points += len(matcher(doc))
        return self.__exclamation_points

    def setQuestionMarks(self, nlp, text):
        text = removeExtraSpaces(text)
        doc = nlp(text)
        matcher = getMatcher(nlp, "ORTH", "?", "isQuestionMarks", text)
        self.__question_marks += len(matcher(doc))
        return self.__question_marks

    def getTokens(self):
        return self.__tokens

    def getTypes(self):
        return len(self.__types)

    def getLinks(self):
        return self.__links

    def getUpper(self):
        return self.__capital_words

    def getWords(self):
        return self.__words

    def getSentences(self):
        return self.__sentences

    def getCharacters(self):
        return self.__characters

    def getPunctuation(self):
        return self.__punctuation_marks

    def getVerbs(self):
        return self.__verbs

    def getNouns(self):
        return self.__nouns

    def getAdjectives(self):
        return self.__adjectives

    def getAdverbs(self):
        return self.__adverbs

    def getPronouns(self):
        return self.__pronouns

    def getStopWords(self):
        return self.__stopWords

    def getModalVerbs(self):
        return self.__modal_verbs

    def getFirstPronounSingular(self):
        return self.__first_pronoun_singular

    def getFirstPronounPlural(self):
        return self.__first_pronoun_plural

    def getSecondPronounSingular(self):
        return self.__second_pronoun_singular

    def getSecondPronounPlural(self):
        return self.__second_pronoun_plural

    def getThirdPronounSingular(self):
        return self.__third_pronoun_singular

    def getThirdPronounPlural(self):
        return self.__third_pronoun_plural

    def getMisspelledWords(self):
        return self.__misspelledWords

    def getPositiveContent(self):
        return self.__positive_content

    def getNegativeContent(self):
        return self.__negative_content

    def getOwnNames(self):
        return self.__own_names

    def getExclamationPoints(self):
        return self.__exclamation_points

    def getQuestionMarks(self):
        return self.__question_marks

    def printMetaInformation(self):
        print("--- Total number of tokens: {}".format(self.getTokens()))
        print("--- Total number of types: {}".format(self.getTypes()))
        print("--- Total number of links: {}".format(self.getLinks()))
        print("--- Total number of capital letters: {}".format(self.getUpper()))
        print("--- Total number of words number without punctuation: {}".format(self.getWords()))
        print("--- Total number of sentences: {}".format(self.getSentences()))
        print("--- Total number of chars: {}".format(self.getCharacters()))
        print("--- Total number of punctuation marks: {}".format(self.getPunctuation()))
        print("--- Total number of verbs: {}".format(self.getVerbs()))
        print("--- Total number of nouns: {}".format(self.getNouns()))
        print("--- Total number of adjectives: {}".format(self.getAdjectives()))
        print("--- Total number of adverbs: {}".format(self.getAdverbs()))
        print("--- Total number of pronouns: {}".format(self.getPronouns()))
        print("--- Total number of stop words: {}".format(self.getStopWords()))
        print("--- Total number of modal verbs: {}".format(self.getModalVerbs()))
        print("--- Total number of first pronoun in singular: {}".format(self.getFirstPronounSingular()))
        print("--- Total number of first pronoun in plural: {}".format(self.getFirstPronounPlural()))
        print("--- Total number of second pronoun in singular: {}".format(self.getSecondPronounSingular()))
        print("--- Total number of second pronoun in plural: {}".format(self.getFirstPronounPlural()))
        print("--- Total number of third pronoun in singular: {}".format(self.getThirdPronounSingular()))
        print("--- Total number of third pronoun in plural: {}".format(self.getThirdPronounPlural()))
        print("--- Total number of misspelled words: {}".format(self.getMisspelledWords()))
        print("--- Total number of positive content: {}".format(self.getPositiveContent()))
        print("--- Total number of negative content: {}".format(self.getNegativeContent()))
        print("--- Total number of question marks: {}".format(self.getQuestionMarks()))
        print("--- Total number of exclamation points: {}".format(self.getExclamationPoints()))
        print("--- Total number of own names: {}".format(self.getOwnNames()))
