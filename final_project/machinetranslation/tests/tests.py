import unittest
from translator import englishToFrench, frenchToEnglish
class TranslatorTest(unittest.TestCase):
    def test_english_to_french(self):
        text = englishToFrench('hello')
        self.assertEqual('Bonjour', text)
    
    def test_french_to_english(self):
        text = frenchToEnglish('bonjour')
        self.assertEqual('Hello', text)

    def test_null_french_to_english(self):
        text = frenchToEnglish('')
        self.assertNotEqual('bonjour', text)

    def test_null_english_to_french(self):
        text = englishToFrench('')
        self.assertNotEqual('hello', text)
        
if __name__ == '__main__':
    unittest.main()