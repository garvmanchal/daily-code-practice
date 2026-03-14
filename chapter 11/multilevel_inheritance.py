class Employee :
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)  # gives the output
# print(o.b)  # through error cause employee has no b attribute

o = Programmer()
print(o.a)  # gives the output
print(o.b)  # gives the output cause both are inheritily connected

o = Manager()
print(o.a)
print(o.b)
print(o.c)  # all these gives output cause these are connected by multilevel inheritance