# Create a function that takes a string as a parameter and returns True if the string is a palindrome. The function should return False otherwise.

def palindrome(word: str) -> bool:
    newString = ""

    # This adds all alphanumerical characters from the word variable to to the newString variable
    # and converts them to uppercase characters
    for i in word:
        if (i.isalnum()):
            newString += i.upper()
    
    # The below variables will help us to iterate through the newString variable
    # and determine whether or not it is a palindrome
    leftPointer = 0
    rightPointer = len(newString) - 1

    # The left pointer begins at index 0, and the right pointer begins at the last
    # index of the string. If the values at each index are different, the function will return False.
    # if the values at each index are equal, the left pointer will move one index to the right, and 
    # the right index will move one to the left
    while leftPointer <= rightPointer:
        if newString[leftPointer] != newString[rightPointer]:
            return False
        else:
            leftPointer += 1
            rightPointer -= 1
    
    return True
    
            


    


    