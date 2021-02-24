import json
import unittest

from app import app


class TestHome(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.response = self.app.get("/")

    def test_hello_flask(self):
        self.assertEqual(json.loads(
            self.response.data.decode("utf-8")), {"hello": "Flask!"})

    def test_content_type(self):
        self.assertIn(self.response.content_type, "application/json")
