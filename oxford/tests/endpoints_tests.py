from oxford.test import TestCase
import json


class TestEndpointsAPI(TestCase):
    def test_return_400_when_word_is_missing(self):
        rv = self.client.get('/')

        response = json.loads(rv.data)

        self.assertEqual(rv.status_code, 400)
        self.assertEqual(
            response['message'],
            'the argument "word" is required'
        )

    def test_return_404_when_word_is_not_found(self):
        rv = self.client.get('/?word=sdlkfskfjsldkjf')

        response = json.loads(rv.data)

        self.assertEqual(rv.status_code, 404)
        self.assertEqual(
            response['message'],
            'word "sdlkfskfjsldkjf" not found'
        )

    def test_return_200_definition_when_match(self):
        rv = self.client.get('/?word=flow')

        response = json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(response['word'], 'flow')
        self.assertEqual(response['definition'], 'flow definition')
        self.assertEqual(response['anagrams'], ['wolf'])

    def test_case_insensitive(self):
        rv = self.client.get('/?word=fLOw')

        response = json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(response['word'], 'flow')
        self.assertEqual(response['definition'], 'flow definition')
        self.assertEqual(response['anagrams'], ['wolf'])

    def test_case_trim_word(self):
        rv = self.client.get('/?word= flow  ')

        response = json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(response['word'], 'flow')
        self.assertEqual(response['definition'], 'flow definition')
        self.assertEqual(response['anagrams'], ['wolf'])
