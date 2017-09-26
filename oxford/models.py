# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~
    The db models composing the Oxford dictionary.
"""
from oxford import db


class DictionaryEntry(db.Model):
    word = db.Column(db.String(256), primary_key=True)
    definition = db.Column(db.Text)

    # the anagram is queryable so it's an index
    anagram = db.Column(db.String(256), index=True)

    def __init__(self, word, definition):
        self.word = unicode(word)
        self.definition = unicode(definition)

        # we sort the letters so we can quickly search for anagrams
        # "wolf" and "flow" and "fowl" will all become "flow"
        self.anagram = ''.join(sorted(unicode(word))).lower()
