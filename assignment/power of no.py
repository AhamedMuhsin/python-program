base=int(input("Enter the base : "))
power=int(input("Enter the power : "))

p=1
for i in range(1,power+1):
    p=p*base

print("Power of number",base ,"raise to",power,"is :",p)