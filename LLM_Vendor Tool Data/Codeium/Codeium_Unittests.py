import unittest


class TestGinorts(unittest.TestCase):
    def test_lower_case_only(self):
        """
        Test if the function returns the input string in lower case.
        """
        result = ginorts("abcde")
        self.assertEqual(result, "abcde")

    def test_upper_case_only(self):
        result = ginorts("ABCDE")
        self.assertEqual(result, "ABCDE")

    def test_odd_digits_only(self):
        result = ginorts("13579")
        self.assertEqual(result, "13579")

    def test_even_digits_only(self):
        result = ginorts("24680")
        self.assertEqual(result, "02468")

    def test_mixed_input(self):
        result = ginorts("a1B2c3D4")
        self.assertEqual(result, "abcd1234")

if __name__ == '__main__':
    unittest.main()