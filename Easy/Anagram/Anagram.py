# Create a function that receives two strings as arguments. The function will return "True"
# if the strings are anagrams, and "False" if they aren't

def anagram(t: str, s: str) -> bool:
    if len(t) != len(s):
        return False
    

    tCount, sCount = {}, {} # letter -> number of occurrences in respective string

    # This loop iterates through both strings and maps each letter encountered to the number of times it
    # appears in the string
    for i in range(len(t)):
        tCount[t[i]] = 1 + tCount.get(t[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    # This loop checks to see if each letter occurs the same number of times in each string.
    for i in sCount:
        if tCount[i] != sCount[i]:
            return False
        
    return True

