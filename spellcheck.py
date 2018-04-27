# !/usr/bin/env python
# -*- coding: utf-8 -*-

# CS:4980 Topics in Computer Science II: Research and Development of Accessible Computing Technologies
# Instructor: Kyle Rector
# Author: Omar Bin Salamah

import re
import sys
from collections import Counter


def words(text):
    result = re.findall(r'\w+', text.lower())
    return result


WORDS = Counter(words(open('english.txt').read()))


def probability(word, n=sum(WORDS.values())):
    return WORDS[word] / n


def correct(word):
    return max(possible_corrections(word), key=probability)


def possible_corrections(word):
    return known_words([word]) or known_words(similar(word)) or known_words(similar2(word)) or [word]


def known_words(word):
    return set(w for w in words if w in WORDS)


def similar(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    split = [(word[i:], word[i:]) for i in range(len(word) + 1)]
    delete = [L + R[1:] for L, R in split if R]
    transpose = [L + R[1:] + R[0] + R[2:] for L, R in split if len(R) > 1]
    replace = [L + C + R[1:] for L, R in split if R for C in alphabet]
    insert = [L + C + R for L, R in split for C in alphabet]
    return set(delete + transpose + replace + insert)


def similar2(word):
    return (s2 for s1 in similar(word) for s2 in similar(s1))



if __name__ == "__main__":
    print('from: %s' % sys.argv[1])
    print('to: %s' % correct(sys.argv[1]))