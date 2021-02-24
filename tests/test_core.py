import json
import unittest

from app import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_flask(self):
        response = self.app.get("/")
        self.assertEqual(json.loads(response.data.decode("utf-8")), {"hello": "Flask!"})


if __name__ == "__main__":
    unittest.main()
