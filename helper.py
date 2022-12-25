import spacy
from spacy.matcher import Matcher
from spylls.hunspell import Dictionary
import regex as rx
import re
from string import punctuation


# Instâncias usadas em outros arquivos .py

def getModelSpacy():
    return spacy.load("pt_core_news_sm")


def getSpellChecker(path):
    return Dictionary.from_zip(path)


def getMatcher(nlp, pattern, value, label, text):
    matcher = Matcher(nlp.vocab, validate=True)
    matcher.add(label, [[{pattern: value}]])
    return matcher


# Funções auxiliares para os pronomes

def countPronouns(nlp, text, pronouns):
    count = 0
    doc = nlp(text)
    for token in doc:
        if token.text in pronouns:
            count += 1
    return count


def getPronouns(person):
    pronouns = {
        "1s": ("eu", "me", "mim", "comigo"),
        "2s": ("tu", "te", "ti", "contigo"),
        "3s": ("ele", "ela", "lhe", "o", "a", "se", "consigo"),
        "1p": ("nós", "nos", "conosco"),
        "2p": ("vós", "vos", "convosco"),
        "3p": (
            "eles",
            "elas",
            "lhe",
            "os",
            "as",
            "se",
            "eles" "elas",
            "si",
            "consigo",
        ),
    }
    return pronouns[person]


# Funções para limpeza de texto

def removeExtraSpaces(text):
    text_without_extra_spaces = " ".join(text.split())
    return text_without_extra_spaces


def toLowercase(text):
    lower_text = text.lower()
    lower_text = removeExtraSpaces(lower_text)
    return lower_text


def removeUnicodeControlCharacters(text):
    text_without_unicodeChars = rx.sub(r"\p{C}", "", text)
    text_without_unicodeChars = removeExtraSpaces(text_without_unicodeChars)
    return text_without_unicodeChars


def remove_emojis(text):
    emoj = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002500-\U00002BEF"
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"
        "\u3030"
        "]+",
        re.UNICODE,
    )
    text_without_emojis = re.sub(emoj, "", text)
    text_without_emojis = removeExtraSpaces(text_without_emojis)
    return text_without_emojis


def removeHiperlink(text):
    text_without_hiperLink = re.sub(r"https?://\S+", "", text)
    text_without_hiperLink = removeExtraSpaces(text_without_hiperLink)
    return text_without_hiperLink


def removePunctuation(text):
    text_without_punctuation = re.sub(f"[{re.escape(punctuation)}]", "", text)
    text_without_punctuation = removeExtraSpaces(text_without_punctuation)
    return text_without_punctuation


def removeNumbers(text):
    text_without_numbers = re.sub(r"\b[0-9]+\b\s*", "", text)
    text_without_numbers = removeExtraSpaces(text_without_numbers)
    return text_without_numbers


def removeSymbolsBert(text):
    text_without_symbols_bert = text.replace("[CLS]", "")
    text_without_symbols_bert = text_without_symbols_bert.replace("[SEP]", "")
    text_without_symbols_bert = text_without_symbols_bert.replace("[PAD]", "")
    text_without_symbols_bert = text_without_symbols_bert.replace("[UNK]", "")
    text_without_symbols_bert = removeExtraSpaces(text_without_symbols_bert)
    return text_without_symbols_bert
