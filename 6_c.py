# Write a Python program to read last n lines of a file. 
f=open("test.txt","r")
n=1
k=f.readlines()
print(k[-n:])
f.close()
