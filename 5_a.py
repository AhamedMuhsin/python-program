# Write a Python script to sort (ascending and descending) a dictionary by value.
import operator

d={1:"shaun",4:"blake",2:"name",3:"mike"}

print("Original Dictionary : ",d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1))
print("Dictionary in ascending order by value : \n",sorted_d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Dictionary in descending order by value : \n",sorted_d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1))
print("Dictionary in ascending order by key : \n",sorted_d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Dictionary in descending order by value : \n",sorted_d)
