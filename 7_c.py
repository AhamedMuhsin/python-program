"""
Create a class called Numbers, which has a single class attribute called 
MULTIPLIER, and a constructor which takes the parameters x and y (these should 
all be numbers). 
i. Write a method called add which returns the sum of the attributes x and y. 
ii. Write a class method called multiply, which takes a single number 
parameter a and returns the product of a and MULTIPLIER. 
iii. Write a static method called subtract, which takes two number parameters, b 
and c, and returns b - c. 
iv. Write a method called value which returns a tuple containing the values of x 
and y. Make this method into a property, and write a setter and a deleter for 
manipulating the values of x and y. 
"""
class Numbers:
    MULTIPLIER=3
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    @classmethod
    def multiply(cls,a):
        return cls.MULTIPLIER*a
    @staticmethod
    def subtract(b,c):
        return b-c

t=Numbers(2,4)
print(t.add())
print(t.multiply(2))
print(Numbers.subtract(4,3))