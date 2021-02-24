import json
import unittest

from app import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_flask(self):
        response = self.app.get("/")
        self.assertEqual(json.loads(
            response.data.decode("utf-8")), {"hello": "Flask!"})

    def test_content_type_hello_flask(self):
        response = self.app.get("/")
        self.assertIn(response.content_type, "application/json")

    def test_forum(self):
        response = self.app.get("/forum")
        self.assertEqual(response.status, "404 NOT FOUND")

    def test_login(self):
        body_json = {"data": {"username": "admin", "password": "flask"}}
        response = self.app.post("/login", json=body_json)
        self.assertEqual(
            json.loads(response.data.decode("utf-8")),
            {'menssagem': 'sucesso!'})
