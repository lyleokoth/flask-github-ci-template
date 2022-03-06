import app 
import unittest
import json


class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        app.app.testing = True
        self.app = app.app.test_client()


    def test_index(self):
        response = self.app.get('/')
        data = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert type(data) is dict


