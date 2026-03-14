# Inheritance & More on OOPs

class Employee :
    company ="ITC"
    name = "Grv"
    salary = 90000
    def show(self):
        print(f"The name is {self.name} and his salary is {self.salary}")

class Coder :
   language = "Pyhton"
   def printlanguage(self):
      print(f"out of all the languages here is your language:{self.language}")

class Programmer(Employee,Coder):
  company ="ITC Infotech"
  def showLanguage(self):
    print(f"The name is {self.company} and He is good with {self.language} language")

a = Employee()
b = Programmer()
b.show()
b.printlanguage()
b.showLanguage()

print(a.company , b.company)
