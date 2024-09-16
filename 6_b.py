# Write a Python program to append text to a file and display the text. 
f=open("test.txt","r")
print(f.read())
f.close()

f=open("test.txt","a")
f.write("\nThanks for appending in this text file")
f.close()

f=open("test.txt","r")
print(f.read())
f.close()
