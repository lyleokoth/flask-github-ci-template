import app 
import unittest


class MyTestCase(unittest.TestCase):
    

    def setUp(self) -> None:
        app.app.testing = True
        self.app = app.app.test_client()


    def test_index(self):
        response = self.app.get('/')
        assert response.status_code == 200

