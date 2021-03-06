# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from . import BackendBase


class LanguageBackend(BackendBase):
    def check_word(self, word):
        ALL_ALPHANUM = re.compile('([0-9a-záéíóúüñ])', re.I)
        NON_ALPHANUM = re.compile('([^0-9a-záéíóúüñ])', re.I)

        TOO_MANY_VOWELS = re.compile('[aáeéiíoóuúü]{3}', re.I)
        TOO_MANY_CONSONANTS = re.compile('[bcdfghjklmnñpqrstvwxyz]{5}', re.I)
        SINGLE_LETTER_WORDS = re.compile('^[aeoóuy]$', re.I)

        #(L) If a string is longer than 20 characters, it is garbage
        if len(word) > 20:
            return None

        #(A) If a string’s ratio of alphanumeric characters to total
        #characters is less than 50%, the string is garbage
        if len(ALL_ALPHANUM.findall(word)) < len(word) / 2:
            return None

        #Remove word if all the letters in the word are non alphanumeric
        if len(NON_ALPHANUM.findall(word)) == len(word):
            return None

        #Removed words with too many consecutie vowels
        if TOO_MANY_VOWELS.findall(word):
            return None

        #Removed words with too many consecutie consonants
        if TOO_MANY_CONSONANTS.findall(word):
            return None

        #Only allow specific single letter words
        if len(word) == 1 and not SINGLE_LETTER_WORDS.findall(word):
            return None

        return word
