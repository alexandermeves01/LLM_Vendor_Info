import unittest
from String_Sorted import ginortS
import unittest
from String_Sorted import ginortS

class TestGinortS(unittest.TestCase):

    def test_lower_sorted(self):
        result = ginortS('hello')
        self.assertEqual(result, 'ehllo')
    
    def test_upper_sorted(self):
        result = ginortS('BAC')
        self.assertEqual(result, 'ABC')

    def test_odd_sorted(self):
        result = ginortS('13579')
        self.assertEqual(result, '13579')

    def test_even_sorted(self):
        result = ginortS('2468')
        self.assertEqual(result, '2468')

    def test_mixed_sorted(self):
        result = ginortS('Hello137World2')
        self.assertEqual(result, 'ehllo1379W2dlor')


        expected = "ehllo"
        self.assertEqual(ginortS(string), expected)

    def test_uppercase_sorted(self):
        string = "BAC"
        expected = "ABC"
        self.assertEqual(ginortS(string), expected)

    def test_odd_digits_sorted(self):
        string = "13579"
        expected = "13579"
        self.assertEqual(ginortS(string), expected)

    def test_even_digits_sorted(self):
        string = "2468"
        expected = "2468"
        self.assertEqual(ginortS(string), expected)

    def test_mixed_case_digits_sorted(self):
        string = "h3e5ll7o9"
        expected = "ehllo3579"
        self.assertEqual(ginortS(string), expected)


    def test_lowercase_sorted(self):