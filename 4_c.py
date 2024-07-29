"""Write a Python program to clone or copy a list """
l=[]
for i in range(10):
    num=int(input("Enter the element of list : "))
    l.append(num)

print("original list\n",l)
copylist=l
print("after copying \n",copylist)
