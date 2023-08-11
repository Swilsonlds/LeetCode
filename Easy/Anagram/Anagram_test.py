import pytest
import Anagram

def test_anagram_true():
    assert Anagram.anagram("god", "dog")

def test_anagram_false():
    assert Anagram.anagram("bog", "dog")
