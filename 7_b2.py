#  Implement the concept of inheritance using python 
# multilevel inheritance 
class Room:
    def __init__(self, l,b,h):
        self.len=l
        self.bre=b
        self.hei=h

class Area(Room):
    def __init__(self, l, b,h):
        super().__init__(l, b,h)
        self.area=l*b

class Volume(Area):
    def __init__(self, l, b, h):
        super().__init__(l,b,h)
        self.vol=self.area*h

len=int(input("Enter the length of room : "))
bre=int(input("Enter the breadth of room : "))
hei=int(input("Enter the height of room : "))
v = Volume(len,bre,hei)
print("Area of room is : ",v.area)
print("Volume of room is : ",v.vol)  # Output: Area of room is :
