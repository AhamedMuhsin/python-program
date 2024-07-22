# Write a program to generate the Fibonacci series. 

series = int(input("Enter a number till print the series : "))

n1, n2 = 0, 1
count = 0

if series <= 0:
   print("Please enter a positive integer")
elif series == 1:
   print("Fibonacci sequence upto", series, ":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < series:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
