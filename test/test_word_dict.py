import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.positive_words import positive_words
from utils.negative_words import negative_words
from utils.neutral_words import neutral_words

sample_sentences = [
    'there was a cockroach in my soup',
    'she gave a brilliant presentation',
    'Have you tried any new restaurants or cafes recently',
    'The player ran with the ball and scored a goal.',
    'I went to the fridge for water and came back with cake.',
    'The service was terrible and the food tasted awful.',
    'It’s not that he lacked the ability to succeed; rather, he refused to put in the effort required to even begin',
    'I ate a good sweet today in saturday market.',
    'The food tasted amazing, but the service was slow, and the atmosphere was just okay.',
    'i felt joyful after the exam',
    'The movie was not bad, but it wasn’t exactly good either',
    'The Actors did a great job with their acting ,but the movie was boring',
    'Have you tried any new restaurants or cafes recently',
    'An apple a day keeps the doctor away- if you throw it hard enough',
    'He was chalant and helped his friend',
    'the service was rude and the wait was too long',
    'The computer generated a list of random numbers',
    'The weather was horrible yesterday',
    'While the weather was pleasant, the traffic made our journey stressful.',
    'She received an award for her outstanding performance',
    'The trip was exciting, but the weather was terrible, and the hotel was decent.',
    'I hope it doesn’t rain tomorrow',
    'His presentation was impressive, though he spoke too fast, and the slides were fine.',
]


def positive_check(word):
    return word in positive_words


def negative_check(word):
    return word in negative_words


def neutral_check(word):
    return word in neutral_words


for sentence in sample_sentences:
    words = sentence.split()
    sentence_score = 0
    for test_word in words:
        is_positive = positive_check(test_word)
        is_negative = negative_check(test_word)
        is_neutral = neutral_check(test_word)
        score=0
        if is_positive:
            score+=1
        elif is_negative:
            score-=1
        sentence_score+=score
    print(f"Sentence: '{sentence}' | Score: {sentence_score}")
        