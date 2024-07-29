"""Take a list, say for example this one: 
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
and write a program that prints out all the elements of the list that are less than 5. """

l=[]
for i in range(10):
    num=int(input("Enter elements of list : "))
    l.append(num)

print("list elements ")
for i in l:
    print(i,end=" ")

print("\nnumbers less than 5 are ")

for i in l:
    if i<5:
        print(i)
