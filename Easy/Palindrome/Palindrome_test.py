import Palindrome
import pytest

#Ensures that the function returns a "True" when the user passes in a palindrome
def test_palindrome_true():
    assert Palindrome.palindrome("bib") == True

#Ensures that the function returns a "False" when the user passes in a non-palindrome
def test_palindrome_false():
    assert Palindrome.palindrome("dog") == False

#Ensures that the function returns a "True" when the user passes in a palindrome which includes non-alphanumerical characters
def test_palindrome_alphaNum():
    assert Palindrome.palindrome("race car") == True



