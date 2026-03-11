# OOPS
# class Employee :
    
#     lang = "Py"   #class attributes
#     salary = 1200000 #class attributes

# grv = Employee()
# grv.name = "Garv" #object attribute
# print(grv.name, grv.salary , grv.lang)

# harry = Employee()
# harry.name = "harry" #object / instance attribute
# print(harry.name ,harry.lang , harry.salary)

# class Employee :
    
#     lang = "Python"  
#     salary = 1200000

#     def getinfo(self):
#         print(f"The language is {self.lang} .The salary is {self.salary}")

#     @staticmethod
#     def greet(self):
#         print("Good morning")

# garv = Employee()
# garv.greet()
# garv.getinfo()

# class Employee :
#     def __init__(self,name,company,salary): # dunder method which is automatically called 
#         self.name = name 
#         self.company = company
#         self.salary = salary
#         print(f"My name is {self.name} and i am working in {self.company} and my monthly salary is {self.salary}")

#     @staticmethod
#     def greet():
#         print("Good Morning")
        
# Employee.greet()
# emp = Employee("Garv", "Google" , 1200000 )

# Practice set

# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
        
# p = Programmer("Garv" ,2000000, 126102)
# print(p.name,p.salary,p.pin )

# class Calculator :
#     def __init__(self , n):
#         self.n = n 
#     def square(self):
#         print(f"the square is {self.n * self.n}")

#     def cube(self):
#         print(f"the square is {self.n * self.n * self.n}")

#     def squareroot(self):
#         print(f"the square is {self.n**1/2}")


# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()
        
class Demo :
    a = 4 

o = Demo ()