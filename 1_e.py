"""Write a function to check the input value is Armstrong and also write the 
function for Palindrome. """

import math
def armstrongNumber(n):
    rem=0
    res=0
    while (n!=0):
        rem=n%10
        res=res+(rem*rem*rem)
        n=math.floor(n/10)
    return res

def palindrome(n):
    rem=0
    res=0
    while (n>0):
        rem=n%10
        res=res*10+rem
        n=math.trunc(n/10)
    return res
    
num=int(input("Enter a number : "))
arm=armstrongNumber(num)
if arm==num:
    print(num,"is a armstrong number")
else:
    print(num,"is not an armstrong number")
pal=palindrome(num)
if pal==num:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")