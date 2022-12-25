class TipsLinguistics:
    def __init__(self, metaInformation, totalTexts):
        self.__avgNumberOfTokens = self.avgNumberOfTokens(
            metaInformation, totalTexts)
        self.__avgNumberOfTypes = self.avgNumberOfTypes(
            metaInformation, totalTexts)
        self.__avgNumberOfLinks = self.avgNumberOfLinks(
            metaInformation, totalTexts)
        self.__avgNumberOfCapitalLetters = self.avgNumberOfCapitalLetters(
            metaInformation, totalTexts)
        self.__avgSizeWords = self.avgSizeWords(metaInformation)
        self.__avgNumberOfSentences = self.avgNumberOfSentences(
            metaInformation, totalTexts)
        self.__avgNumberOfSentencesInWords = self.avgNumberOfSentencesInWords(
            metaInformation)
        self.__avgNumberOfVerbs = self.avgNumberOfVerbs(
            metaInformation, totalTexts)
        self.__avgNumberOfNouns = self.avgNumberOfNouns(
            metaInformation, totalTexts)
        self.__avgNumberOfAdjectives = self.avgNumberOfAdjectives(
            metaInformation, totalTexts)
        self.__avgNumberOfAdverbs = self.avgNumberOfAdverbs(
            metaInformation, totalTexts)
        self.__avgNumberOfPronouns = self.avgNumberOfPronouns(
            metaInformation, totalTexts)
        self.__avgNumberOfSW = self.avgNumberOfSW(metaInformation, totalTexts)
        self.__avgNumberOfModalVerbs = self.avgNumberOfModalVerbs(
            metaInformation, totalTexts)
        self.__avgMisspelledWords = self.avgMisspelledWords(metaInformation)
        self.__pausality = self.pausality(metaInformation)
        self.__emotiveness = self.emotiveness(metaInformation)
        self.__nonImmediacy = self.nonImmediacy(metaInformation, totalTexts)
        self.__diversity = self.diversity(metaInformation)
        self.__avgQuestionMarks = self.questionMarks(
            metaInformation, totalTexts)
        self.__avgExclamationPoints = self.exclamationPoints(
            metaInformation, totalTexts)
        self.__avgOwnNames = self.ownNames(metaInformation, totalTexts)
        self.__avgTextsPositive = self.positiveContent(
            metaInformation, totalTexts)
        self.__avgTextsNegative = self.negativeContent(
            metaInformation, totalTexts)
        self.__selfReference = self.selfReference(metaInformation, totalTexts)
        self.__groupReference = self.groupReference(
            metaInformation, totalTexts)
        self.__anotherReference = self.anotherReference(
            metaInformation, totalTexts)

    def avgNumberOfTokens(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfTokens = metaInformation.getTokens() / totalTexts
            print(
                "****Avg number of tokens per text: {:.4f}".format(self.__avgNumberOfTokens))
            return self.__avgNumberOfTokens
        except ZeroDivisionError:
            print("****Avg number of tokens per text: 0.0000")

    def avgNumberOfTypes(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfTypes = metaInformation.getTypes() / totalTexts
            print(
                "****Avg number of types per text: {:.4f}".format(self.__avgNumberOfTypes))
            return self.__avgNumberOfTypes
        except ZeroDivisionError:
            print("****Avg number of types per text: 0.0000")

    def avgNumberOfLinks(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfLinks = metaInformation.getLinks() / totalTexts
            print(
                "****Avg number of links per text: {:.4f}".format(self.__avgNumberOfLinks))
            return self.__avgNumberOfLinks
        except ZeroDivisionError:
            print("****Avg number of links per text: 0.0000")

    def avgNumberOfCapitalLetters(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfCapitalLetters = metaInformation.getUpper() / totalTexts
            print(
                "****Avg number of capital letters: {:.4f}".format(self.__avgNumberOfCapitalLetters))
            return self.__avgNumberOfCapitalLetters
        except ZeroDivisionError:
            print("****Avg number of capital letters: 0.0000")

    def avgSizeWords(self, metaInformation):
        try:
            self.__avgSizeWords = metaInformation.getCharacters()/metaInformation.getWords()
            print(
                "****Avg size of words (in characters): {:.4f}".format(self.__avgSizeWords))
            return self.__avgSizeWords
        except ZeroDivisionError:
            print("****Avg size of words (in characters): 0.0000")

    def avgNumberOfSentences(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfSentences = metaInformation.getSentences()/totalTexts
            print(
                "****Avg number of sentences per text: {:.4f}".format(self.__avgNumberOfSentences))
            return self.__avgNumberOfSentences
        except ZeroDivisionError:
            print("****Avg number of sentences per text: 0.0000")

    def avgNumberOfSentencesInWords(self, metaInformation):
        try:
            self.__avgNumberOfSentencesInWords = metaInformation.getWords() / \
                metaInformation.getSentences()
            print(
                "****Avg number of sentences (in words): {:.4f}".format(self.__avgNumberOfSentencesInWords))
            return self.__avgNumberOfSentencesInWords
        except ZeroDivisionError:
            print("****Avg number of sentences (in words): 0.0000")

    def avgNumberOfVerbs(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfVerbs = (
                (metaInformation.getVerbs()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg number of verbs (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgNumberOfVerbs))
            return self.__avgNumberOfVerbs
        except ZeroDivisionError:
            print("****Avg number of verbs (norm. by the avg number of tokens): 0.0000")

    def avgNumberOfNouns(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfNouns = (
                (metaInformation.getNouns()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg number of nouns (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgNumberOfNouns))
            return self.__avgNumberOfNouns
        except ZeroDivisionError:
            print("****Avg number of nouns (norm. by the avg number of tokens): 0.0000")

    def avgNumberOfAdjectives(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfAdjectives = (
                (metaInformation.getAdjectives()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg number of adjectives (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgNumberOfAdjectives))
            return self.__avgNumberOfAdjectives
        except ZeroDivisionError:
            print(
                "****Avg number of adjectives (norm. by the avg number of tokens): 0.0000")

    def avgNumberOfAdverbs(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfAdverbs = (
                (metaInformation.getAdverbs()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg number of adverbs (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgNumberOfAdverbs))
            return self.__avgNumberOfAdverbs
        except ZeroDivisionError:
            print("****Avg number of adverbs (norm. by the avg number of tokens): 0.0000")

    def avgNumberOfPronouns(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfPronouns = (
                (metaInformation.getPronouns()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg number of pronouns (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgNumberOfPronouns))
            return self.__avgNumberOfPronouns
        except ZeroDivisionError:
            print(
                "****Avg number of pronouns (norm. by the avg number of tokens): 0.0000")

    def avgNumberOfSW(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfSW = (
                (metaInformation.getStopWords()/totalTexts)/self.__avgNumberOfTokens)*100
            print(
                "****Avg number of stop words (norm. by the avg number of tokens): {:.4f}".format(self.__avgNumberOfSW))
            return self.__avgNumberOfSW
        except ZeroDivisionError:
            print(
                "****Avg number of stop words (norm. by the avg number of tokens): 0.0000")

    def avgNumberOfModalVerbs(self, metaInformation, totalTexts):
        try:
            self.__avgNumberOfModalVerbs = (
                (metaInformation.getModalVerbs()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg number of modal verbs (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgNumberOfModalVerbs))
            return self.__avgNumberOfModalVerbs
        except ZeroDivisionError:
            print(
                "****Avg number of modal verbs (norm. by the avg number of tokens): 0.0000")

    def avgMisspelledWords(self, metaInformation):
        try:
            self.__avgMisspelledWords = ((metaInformation.getMisspelledWords(
            )/metaInformation.getWords())/self.__avgNumberOfTokens)*100
            print(
                "****Avg misspelled words per text: {:.4f}".format(self.__avgMisspelledWords))
            return self.__avgMisspelledWords
        except ZeroDivisionError:
            print(
                "****Avg number of misspelled words (norm. by the avg number of tokens): 0.0000")

    def pausality(self, metaInformation):
        try:
            self.__pausality = metaInformation.getPunctuation()/metaInformation.getSentences()
            print(
                "****Avg Pausality per text: {:.4f}".format(self.__pausality))
            return self.__pausality
        except ZeroDivisionError:
            print("****Avg Pausality per text:: 0.0000")

    def emotiveness(self, metaInformation):
        try:
            self.__emotiveness = (metaInformation.getAdjectives(
            )+metaInformation.getAdverbs())/(metaInformation.getNouns()+metaInformation.getVerbs())
            print(
                "****Avg Emotiveness per text: {:.4f}".format(self.__emotiveness))
            return self.__emotiveness
        except ZeroDivisionError:
            print("****Avg Emotiveness per text: 0.0000")

    def nonImmediacy(self, metaInformation, totalTexts):
        try:
            self.__nonImmediacy = (metaInformation.getFirstPronounSingular(
            )+metaInformation.getSecondPronounSingular())/totalTexts
            print(
                "****Avg Non-immediacy per text: {:.4f}".format(self.__nonImmediacy))
            return self.__nonImmediacy
        except ZeroDivisionError:
            print("****Avg Non-immediacy per text: 0.0000")

    def diversity(self, metaInformation):
        try:
            self.__diversity = metaInformation.getTypes() / metaInformation.getWords()
            print(
                "****Avg diversity per text: {:.4f}".format(self.__diversity))
            return self.__diversity
        except ZeroDivisionError:
            print("****Avg diversity per text: 0.0000")

    def questionMarks(self, metaInformation, totalTexts):
        try:
            self.__avgQuestionMarks = (
                (metaInformation.getQuestionMarks()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg question marks (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgQuestionMarks))
            return self.__avgQuestionMarks
        except ZeroDivisionError:
            print("****Avg question marks (norm. by the avg number of tokens): 0.0000")

    def exclamationPoints(self, metaInformation, totalTexts):
        try:
            self.__avgExclamationPoints = (
                (metaInformation.getExclamationPoints()/totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg exclamation points (norm. by the avg number of tokens): {:.4f}".format(
                self.__avgExclamationPoints))
            return self.__avgExclamationPoints
        except ZeroDivisionError:
            print(
                "****Avg exclamation points (norm. by the avg number of tokens): 0.0000")

    def ownNames(self, metaInformation, totalTexts):
        try:
            self.__avgOwnNames = (
                (metaInformation.getOwnNames() / totalTexts)/self.__avgNumberOfTokens)*100
            print(
                "****Avg own names (norm. by the avg number of tokens): {:.4f}".format(self.__avgOwnNames))
            return self.__avgOwnNames
        except ZeroDivisionError:
            print("****Avg own names (norm. by the avg number of tokens): 0.0000")

    def positiveContent(self, metaInformation, totalTexts):
        try:
            self.__avgTextsPositive = metaInformation.getPositiveContent() / totalTexts
            print(
                "****Avg number of positive texts: {:.4f}".format(self.__avgTextsPositive))
            return self.__avgTextsPositive
        except ZeroDivisionError:
            print("****Avg number of positive texts: 0.0000")

    def negativeContent(self, metaInformation, totalTexts):
        try:
            self.__avgTextsNegative = metaInformation.getNegativeContent() / totalTexts
            print(
                "****Avg number of negative texts: {:.4f}".format(self.__avgTextsNegative))
            return self.__avgTextsNegative
        except ZeroDivisionError:
            print("****Avg number of negative texts: 0.0000")

    def selfReference(self, metaInformation, totalTexts):
        try:
            self.__selfReference = ((metaInformation.getFirstPronounSingular(
            ) / totalTexts)/self.__avgNumberOfTokens)*100
            print(
                "****Avg self reference per text (norm. by the avg number of tokens): {:.4f}".format(self.__selfReference))
        except ZeroDivisionError:
            print(
                "****Avg self reference per text (norm. by the avg number of tokens: 0.0000")

    def groupReference(self, metaInformation, totalTexts):
        try:
            self.__groupReference = ((metaInformation.getFirstPronounPlural(
            ) / totalTexts)/self.__avgNumberOfTokens)*100
            print(
                "****Avg group reference per text (norm. by the avg number of tokens): {:.4f}".format(self.__groupReference))
        except ZeroDivisionError:
            print(
                "****Avg group reference per text (norm. by the avg number of tokens: 0.0000")

    def anotherReference(self, metaInformation, totalTexts):
        try:
            self.__anotherReference = (((metaInformation.getThirdPronounSingular(
            )+metaInformation.getThirdPronounPlural()) / totalTexts)/self.__avgNumberOfTokens)*100
            print("****Avg another reference per text (norm. by the avg number of tokens): {:.4f}".format(
                self.__anotherReference))
        except ZeroDivisionError:
            print(
                "****Avg another reference per text (norm. by the avg number of tokens: 0.0000")
