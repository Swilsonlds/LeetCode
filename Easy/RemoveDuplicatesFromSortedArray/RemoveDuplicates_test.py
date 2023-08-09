import RemoveDuplicates
import pytest

def test1():
    assert RemoveDuplicates.remove_duplicates([1,1,2,2,3,3,4,4,5,5]) == 5

def test2():
    assert RemoveDuplicates.remove_duplicates([1,2,3,3,4,5,6,6,6,6,7]) == 7

def test3():
    assert RemoveDuplicates.remove_duplicates([1]) == 1