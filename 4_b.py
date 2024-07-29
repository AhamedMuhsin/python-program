"""Write a Python program to print a specified list after removing the 0th, 2nd, 4th 
and 5th elements. """
l=[]
for i in range(10):
    num=int(input("Enter the element of list : "))
    l.append(num)

print("list elements \n",l)
print("list elements after removing")
l=[x for (i,x) in enumerate(l) if i%2!=0 ]
print(l)
