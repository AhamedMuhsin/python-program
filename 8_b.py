# write a program to implement exception handling
def divideNum(a,b): 
    try:
        res=a/b
        print("division between a and b is ",res)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error invalid type!")
    except Exception as e:
        print("An error occurred: ", str(e))

divideNum(10,2)
divideNum("20",2)
divideNum(10,0) 