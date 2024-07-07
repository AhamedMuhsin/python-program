import math
def armstrongNumber(n):
    rem=0
    res=0
    while (n!=0):
        rem=n%10
        res=res+(rem*rem*rem)
        n=math.floor(n/10)
    return res

def palindrome(name):
    return name==name[::-1]
    

num=int(input("Enter a number : "))
arm=armstrongNumber(num)
if arm==num:
    print(num,"is a armstrong number")
else:
    print(num,"is not an armstrong number")
name=input("Enter a name : ")
pal=palindrome(name)
if pal:
    print(name,"is a palindrome")
else:
    print(name,"is not a palindrome")