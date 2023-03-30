#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        len_sentence = len(sentence)
        first_word = None
    else:
        len_sentence = len(sentence)
        first_word = sentence[0]
    tuple_sentence = (len_sentence, first_word)

    return tuple_sentence
