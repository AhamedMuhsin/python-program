#Design a class that store the information of student and display the same 
class Student:
    def __init__(self, name, age, rollno, marks):
        self.name = name
        self.age = age
        self.marks=marks
        self.rollno = rollno
    def display(self):
            print("My Name is ",self.name)
            print("My Age is ",self.age)
            print("My Roll No is ",self.rollno)
            print("My Marks is ",self.marks)

name=input("Enter you name : ")
age=int(input("Enter your age : "))
rollno=int(input("Enter your roll no : "))
marks = int(input("Enter your marks : "))
s = Student(name,age,rollno,marks)
s.display() 