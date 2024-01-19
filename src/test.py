import unittest
import requests
import os

class TestApi(unittest.TestCase):
    base_url = 'http://localhost:5000'  # Assurez-vous d'ajuster le port si nécessaire

    def test_toupper_endpoint(self):
        response = requests.get(self.base_url + '/toupper?text=hello')
        self.assertEqual(response.text, "HELLO")

    def test_date_endpoint(self):
        response = requests.get(self.base_url + '/date')
        # On vérifie que la date est au format jj/mm/aaaa
        self.assertRegex(response.text, r'\d{2}/\d{2}/\d{4}')
        

    def test_version_endpoint(self):
        response = requests.get(self.base_url + '/version')
        with open(os.path.join(os.path.dirname(__file__), 'version')) as file:
            file_content = file.read()
        self.assertEqual(response.text, file_content)
    def test_endpoint1(self):
        response = requests.get(self.base_url + '/endpoint1')
        self.assertEqual(response.text, "Ceci est l'endspoint bidon 1")
        # Ajoutez ici des assertions pour vérifier la réponse de l'endpoint 1

    def test_endpoint2(self):
        response = requests.get(self.base_url + '/endpoint2')
        self.assertEqual(response.text, "Ceci est l'endpoint bidon 2")
        # Ajoutez ici des assertions pour vérifier la réponse de l'endpoint 2

if __name__ == '__main__':
    unittest.main()
