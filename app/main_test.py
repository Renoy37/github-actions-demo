import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_reverse_string(self):
        response = self.app.get('/reverse')
        data = response.get_json()
        self.assertEqual(data['reversed_string'], 'olleh')

    def test_check_palindrome(self):
        response = self.app.get('/palindrome')
        data = response.get_json()
        self.assertTrue(data['is_palindrome'])

if __name__ == '__main__':
    unittest.main()
