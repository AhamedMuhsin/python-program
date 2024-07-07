import math

def reverseNumber(n):
    rem=0
    rev=0
    while (n!=0):
        rem=n%10
        rev=rev*10+rem
        n=math.trunc(n/10)
    return rev

num=int(input("Enter a number : "))
r=reverseNumber(num)
print("reverse of a number",num,"is",r)
