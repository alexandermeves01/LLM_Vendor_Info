import pytest
import ginortS
def test_ginortS():
    assert ginortS("aBc123") == "acB132"
    assert ginortS("A1b2C3") == "bAC132"
    assert ginortS("abcABC123") == "abcABC132"
    assert ginortS("") == ""
    assert ginortS("54321") == "13524"  # New test case