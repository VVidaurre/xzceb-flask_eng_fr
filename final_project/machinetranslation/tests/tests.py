''' Unit Tests for Translatory.py'''
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    ''' Unit Tests for function english_to_french'''
    def test_translation(self):
        ''' Testing for translation of english text to french'''
        self.assertEqual(english_to_french("Small"),"Petite")
        self.assertEqual(english_to_french("Red"),"Rouge")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"),"Hello")

    def test_null_input(self):
        ''' Testing for null input'''
        self.assertIsNone(english_to_french(None),None)

class TestFrenchToEnglish(unittest.TestCase):
    ''' Unit Tests for function french_to_english'''
    def test_translation(self):
        ''' Testing for translations of french text to english'''
        self.assertEqual(french_to_english("Petite"),"Small")
        self.assertEqual(french_to_english("Rouge"),"Red")
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Hello"),"Bonjour")

    def test_null_input(self):
        ''' Testing for null input'''
        self.assertIsNone(french_to_english(None),None)

unittest.main()
