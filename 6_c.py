# Write a Python program to read last n lines of a file. 
f=open("test.txt","r")
n=4
print(f.readline(n))
f.close()
