import unittest
from string_sorted import ginortS

class TestGinortS(unittest.TestCase):

    def test_lowercase_sorted(self):
        # Test that lowercase letters are sorted alphabetically
        string = "hello"
        expected = "ehllo"
        self.assertEqual(ginortS(string), expected)

    def test_uppercase_sorted(self):
        # Test uppercase letters sorted alphabetically 
        string = "BCA"
        expected = "ABC"
        self.assertEqual(ginortS(string), expected)

    def test_odd_digits_sorted(self):
        # Test odd digits sorted ascending
        string = "7531648"
        expected = "1357"
        self.assertEqual(ginortS(string), expected)

    def test_even_digits_sorted(self):
        # Test even digits sorted ascending
        string = "24681037"
        expected = "2046"
        self.assertEqual(ginortS(string), expected)

    def test_mixed_input(self):
        # Test case with lowercase, uppercase, and digits
        string = "AbC7531648d"
        expected = "AbCd1357"
        self.assertEqual(ginortS(string), expected)
