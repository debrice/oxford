import unittest
from oxford import create_app
from oxford.models import DictionaryEntry
from oxford import db


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_filename='test_config.py')

        with self.app.app_context():
            self.client = self.app.test_client()
            db.create_all()
            word_flow = DictionaryEntry("flow", "flow definition")
            word_wolf = DictionaryEntry("wolf", "wolf definition")
            db.session.add(word_flow)
            db.session.add(word_wolf)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
