import pytest
from files.sample1 import sum

def test_sum():
    b=sum()
    assert b == 50