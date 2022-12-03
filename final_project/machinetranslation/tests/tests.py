import unittest
import translator as tr

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(tr.english_to_french(' '),'au revoir')
        self.assertEqual(tr.english_to_french('Hello'),'Bonjour')
        
        
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(tr.french_to_english(' '),'goodbye')
        self.assertEqual(tr.french_to_english('Bonjour'),'Hello')
        
unittest.main()