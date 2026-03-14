# class method : A class method is a method which is bound to class and not the object of the class 
# it will always gives the class attribute not the the object attribute, so we use cls instead of self
# class Employee :
#     a = 10 
#     @classmethod
#     def show(cls):
#         print(f"the class attribute value of a is {cls.a}")
    
# e = Employee()
# e.a = 78

#property decorators
class Employee:
    a = 10 
    @classmethod
    def show(cls):
        print(f"the class attribute value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}{self.lname}"
        
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    
e = Employee()
e.a = 78
e.name = "grvv Manchal"
print(e.fname,e.lname)
e.show()
