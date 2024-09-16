# Python program to display all the prime numbers within an interval
# lower = 1
# upper = 20

# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

name="ahamed"
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.swapcase())

# def facto(num):
#     if num == 0:
#         return 1
#     elif num==1:
#         return 1
#     else:
#         return num * facto(num - 1)
    
# num= int(input("Enter a number : "))
# print("factorial of",num,"is",facto(num))  # Output: 720
n=int(input())
f=1
for i in range(f,n+1):
    f=f*i
print(f)
