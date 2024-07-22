"""Write a function that takes a character (i.e. a string of length 1) and returns True 
if it is a vowel, False otherwise. """

alpha = input("Enter a character : ")

if (alpha=="a" or alpha=="e" or alpha=="i" or alpha=="o" or alpha=="u"): 
    print(alpha,"is a Vowel")
elif (alpha=="A" or alpha=="E" or alpha=="I" or alpha=="O" or alpha=="U"):
    print(alpha,"is a Vowel")
else:
    print(alpha,"is a Consonant")
