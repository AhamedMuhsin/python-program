"""Write a program that takes two lists and returns True if they have at least one 
common member."""
def common_member(list1, list2):
    result=False
    for i in list1:
        for j in list2:
            if i==j:
                print("\n")
                print(i,end=" ")
                result=True
                return result

l1=[]
l2=[]
for i in range(5):
    num=int(input("Enter the element of list1 : "))
    l1.append(num)

print("list1 elements is ")
for i in l1:
    print(i,end=" ")

print("\n")

for i in range(5):
    num=int(input("Enter the element of list2 : "))
    l2.append(num)

print("list2 elements is ")
for i in l2:
    print(i,end=" ")

print(common_member(l1,l2))
