import pytest

def test_ginortS():
    assert ginortS('Sorting1234') == 'ginortS1324'
    assert ginortS('Test1234') == 'estT1324'
    assert ginortS('HelloWorld1234') == 'deHllloorW1324'
    assert ginortS('') == ''