def facto(f):
    if(f==0):
        return 0
    elif(f==1):
        return 1
    else:
        return (f*facto(f-1))
    
num=int(input("Enter a number : "))
fac=facto(num)
print("factorial of",num,"is",fac)