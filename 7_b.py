#  Implement the concept of inheritance using python 
# single inheritance 
class Room:
    def __init__(self, l,b):
        self.len=l
        self.bre=b

class Area(Room):
    def __init__(self, l, b):
        super().__init__(l, b)
        self.area=l*b

len=int(input("Enter the length of room : "))
breadth=int(input("Enter the breadth of room : "))
a = Area(len,breadth)
print("Area of room is : ",a.area)  # Output: Area of room is :