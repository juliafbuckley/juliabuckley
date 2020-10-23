import unittest
import requests
import json

class TestReset(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:51045' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RESET_URL = SITE_URL + '/reset/'

    def test_put_reset_index(self):
        m = {}
        
        r = requests.put(self.RESET_URL, data=str(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SITE_URL + "/movies/45")
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['title'], 'To Die For (1995)')

    def test_put_reset_key(self):
        m = {}
        
        r = requests.put(self.RESET_URL+"/45", data=str(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SITE_URL + "/movies/45")
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['title'], 'To Die For (1995)') 
	

if __name__ == "__main__":
    unittest.main()

