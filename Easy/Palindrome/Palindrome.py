# Create a function that takes a string as a parameter and returns True if the string is a palindrome. The function should return False otherwise.

def palindrome(word: str):
    newString = ""

    for i in word:
        if (i.isalnum()):
            newString += i.upper()
    
    leftPointer = 0
    rightPointer = len(newString) - 1

    while leftPointer <= rightPointer:
        if newString[leftPointer] != newString[rightPointer]:
            return False
        else:
            leftPointer += 1
            rightPointer -= 1
    
    return True
    
            


    


    