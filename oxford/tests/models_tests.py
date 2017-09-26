from oxford.models import DictionaryEntry
from oxford.test import TestCase


class TestDictionaryEntry(TestCase):
    def test_initialize(self):
        entry = DictionaryEntry("foo", "foo bar definition")
        self.assertEqual(entry.word, "foo")
        self.assertEqual(entry.definition, "foo bar definition")

    def test_create_anagram(self):
        entry = DictionaryEntry("bca", "bca bar definition")
        self.assertEqual(entry.anagram, "abc")
