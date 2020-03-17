from functions.functions import *
import unittest


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.criptos = [
            ['1', 'abccripto1', 'ABC', '1000', '123%', '123%', '223344', '100000'],
            ['2', 'fcdcripto2', 'FCD', '2000', '222%', '222%', '456787', '200000'],
            ['3', 'esdcripto3', 'ESD', '3000', '333%', '333%', '909090', '300000']
        ]
        self.cotations = start_cotations(self.criptos)
        self.url = 'https://www.coinbase.com/price'
        self.criptos_lista = start_scrapping(self.url)

    
    def test_start_cotations_returns_dict(self):
        self.assertTrue(isinstance(self.cotations, dict))
    
    def test_start_cotations_returns_dict_correct_len(self):
        self.assertEqual(len(self.cotations['ABC']), 6)
    
    def test_start_scrap_returns_list(self):
        self.assertTrue(isinstance(self.criptos_lista, list))
    
    def test_start_scrap_returns_list_correct_len(self):
        self.assertEqual(len(self.criptos), 3)

    def test_get_about_critpo_returns_string(self):
        about = get_about_cripto('Bitcoin')
        self.assertTrue(isinstance(about, str))

if __name__ == '__main__':
    unittest.main()