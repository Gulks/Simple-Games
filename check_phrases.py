import re
from time import sleep

def reverse(a):
    """Reverses the phrase.
    
    Excludes all the symbols except for the letters and 
    makes them in lower case."""

    a = re.sub("[^A-Za-z]", "", a)
    a = a.lower()
    return a[::-1]


def is_palindrome(a):
    return a == reverse(a)


phrase = input("Enter a phrase and I'll check if it is a palindrome: ")
phrase = re.sub("[^A-Za-z]", "", phrase)
phrase = phrase.lower()

if (is_palindrome(phrase)):  
    sleep(1)
    print("Yes, your phrase is a palindrome.")
else:
    sleep(1)
    print("No, your phrase isn't a palindrome.")
