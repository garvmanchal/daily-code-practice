# function and recursion 
# in recursion base condition is must

# fxn defination
# def avg():
#     a = int(input("enter first number: "))
#     b = int(input("enter second number: "))
#     c = int(input("enter third number: "))

#     average = (a + b + c)/3
#     print(average)

# # fxn call
# avg()


# def greet():
#     a = input("Enter your name :")
#     print("Have a good day,", a)

# greet()

# def greet(name,rollno):
#     print("Good morning", name, rollno)
#     return "Thanks for coming....."
 
# a = greet("Grv", 78)
# print(a)

# Recursion

# def factorial(n):
#     if n == 0 or n == 1 :
#         return 1
#     return n * factorial(n-1)

# n = int(input("enter the number :"))
# print(f"The factorial of {n} is {factorial(n)}")


# def greatest(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a,b,c = 1,2,3
# print(greatest(a,b,c))   


# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("enter temp in f: "))
# c = f_to_c(f)
# print(f"{round(c,2)} °C")


# def sum(n):
#     if n == 1 :
#         return 1
#     return sum(n-1) + n
    
# print(sum(4))

# n = int(input("enter the number: "))

# for i in range(1,n+1):
#     print("*" * (n))
#     n-=1
# print("")

# def pattern(n):
#    if n == 0:
#       return 
#    print("*" * n)
#    pattern(n-1)

# pattern(3)
   

# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("enter valur in inches: "))

# print(f"the corrosponding value in cms is {inch_to_cms(n)}")


# def remove(l,word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Grv" , "Harry" , "Rohan", "an"]

# print(remove(l,"an"))

def mul():
    n = int(input("enter the number: "))
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

mul()
