# Define a function that computes the length of a given list or string.  

def length(arg):
    res=len(arg)
    return res

l=[]
for i in range(7):
    num=int(input("Enter element of list : "))
    l.append(num)
print("length of list is : ",length(l))

sent=input("Enter a string : ")
print("length of string is : ",length(sent))
