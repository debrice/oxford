from oxford.test import TestCase
from oxford.dictionary import Dictionary


class TestDictionary(TestCase):
    def test_search_return_definition(self):
        with self.app.app_context():
            definition = Dictionary.search("wolf")

            self.assertEqual(definition['word'], 'wolf')
            self.assertEqual(definition['definition'], 'wolf definition')

    def test_search_return_anagram(self):
        with self.app.app_context():
            definition = Dictionary.search("wolf")
            self.assertEqual(definition['anagrams'], ['flow'])

    def test_search_return_none_when_not_found(self):
        with self.app.app_context():
            definition = Dictionary.search("word_not_found")
            self.assertEqual(definition, None)

    def test_dictionary_loads_data(self):
        with self.app.app_context():
            Dictionary.load([
                "Test  -n foo bar baz",
                "Test  -n foo bar baz",
                "ttes  -n foo bar biz"
            ])

            definition = Dictionary.search("test")

            self.assertEqual(definition, {
                "word": "test",
                "definition": "-n foo bar baz",
                "anagrams": ["ttes"],
            })
