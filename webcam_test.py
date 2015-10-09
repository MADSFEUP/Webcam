import webcam
import unittest

class WebcamTestCase(unittest.TestCase):

    def setUp(self):
        webcam.app.config['TESTING'] = True
        self.app = webcam.app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()
