import pytest
import sys

@pytest.mark.skip(reason ="this is good")
def test_demo_1():
    print("this is test1")

@pytest.mark.skipif(sys.version_info < (3,6),reason="good")
def test_demo_2():
    print("this is test1")
