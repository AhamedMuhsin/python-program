"""A pangram is a sentence that contains all the letters of the English alphabet at least 
once, for example: The quick brown fox jumps over the lazy dog. Your task here 
is to write a function to check a sentence to see if it is a pangram or not. """

import re

def isPangram(insent):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_count=0
    if(len(insent)<26):
        return False;
    else:
        insent = insent.lower()
    for i in range(len(alphabet)):
        if(alphabet[i] in insent):
            alpha_count+=1
    if alpha_count==26:
        return True
    else:
        return False

insent=input("Enter a sentence : ")    
if(isPangram(insent)):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram")
    