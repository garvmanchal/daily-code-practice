# Super() :  Super is used to access method and constructor of the parent class from the child class


class Employee :
    def __init__(self):
        print("This is the constructor of employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("This is the constructor of programmer ")
    b = 2



class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("This is the constructor of manager")
    c = 3

o= Employee()
print(o.a)

o= Programmer()
print(o.a , o.b)

o= Manager()
print(o.a , o.b , o.c)
