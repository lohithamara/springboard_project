import sys
import os
import multitasking
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.negative_words import negative_words
from utils.positive_words import positive_words
def score_paragraph(paragraph):
    """
    Analyze score for given paragraph.
    :param paragraph:
    :return:
    """
    paragraph_score=0
    sentences=paragraph.split(".")
    for i,sentence in enumerate(sentences):
        sentence_score=score_sentence(sentence)
        # TODO: replace print with storage
        # print(f"Sentence {i} , Score is {sentence_score}")
        paragraph_score+=sentence_score
    return paragraph_score

def score_sentence(sentence):
    """
    Analyze score for given sentence.
    :param sentence: Sentence to be analyzed
    :return: sentiment score for the sentence
    """
    sentence_score=0
    words=sentence.split()
    for i,word in enumerate(words):
        word_score=analyze_word(word)
        sentence_score+=word_score
    return sentence_score

def analyze_word(word):
    """
    Analyze score for given word.
    :param word: word to be analyzed
    :return: sentiment score for the word
    """
    is_negative=negative_check(word)
    is_positive=positive_check(word)
    if is_positive:
        return 1
    if is_negative:
        return -1
    return 0

def positive_check(word):
    return word in positive_words


def negative_check(word):
    return word in negative_words