"""Define a procedure histogram() that takes a list of integers and prints a 
histogram to the screen. For example, histogram([4, 9, 7]) should print the 
following: 
**** 
********* 
******* """

def histogram(list):
    for i in range(len(list)):
        print(list[i] * "*")

l=[]
for i in range(3):
    num=int(input("Enter three number : "))
    l.append(num)

histogram(l)
