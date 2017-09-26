# -*- coding: utf-8 -*-
"""
    Dictionary
    ~~~~~~~~~~
    Abstraction layer between the API and the db models.
"""
from oxford.models import DictionaryEntry
from oxford import db
from sqlalchemy import and_


class Dictionary(object):
    @classmethod
    def search(cls, word):
        """search for a given word"""
        entry = DictionaryEntry.query.filter_by(word=word).first()
        if entry:
            return {
                "word": entry.word,
                "definition": entry.definition,
                "anagrams": [
                    anagram.word
                    for anagram in Dictionary.get_anagrams(entry.word)
                ]
            }

    @classmethod
    def get_anagrams(cls, word):
        """get the corresponding anagrams definition for a given word"""
        anagram = ''.join(sorted(word)).lower()
        return DictionaryEntry.query.filter(and_(
            DictionaryEntry.anagram == anagram,
            DictionaryEntry.word != word
        )).all()

    @classmethod
    def load(cls, words):
        """Loads an array of string of word definitions"""
        entries = set()

        for line in words:
            [word, separator, definition] = line.partition("  ")

            # word definition should be lowercase
            word = word.lower()

            # prevent inserting the same definition twice
            if(word in entries):
                continue
            entries.add(word)

            entry = DictionaryEntry(word, definition)
            db.session.add(entry)
        db.session.commit()
