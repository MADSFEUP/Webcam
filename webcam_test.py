import webcam
import unittest
import json


class WebcamTestCase(unittest.TestCase):

    def setUp(self):
        webcam.app.config['TESTING'] = True
        self.app = webcam.app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

    def test_api_channels(self):
        rv = self.app.get('/channels')
        assert is_json(rv.data) ##test if json
        data = json.loads(rv.data)
        assert is_array(data) ##test if array
        for x in range(0, len(data)):
            print data[x]
           ## assert hasattr(data[x], 'id')
           ## assert hasattr(data[x], 'url')

if __name__ == '__main__':
    unittest.main()


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True


def is_array(var):
    return isinstance(var, (list, tuple))