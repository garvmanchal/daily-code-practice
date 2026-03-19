# try :
#     a = int(input("enter the number:"))
#     print(a)

# except Exception as e :
#     print(e)

# print("thnxxxx")

# we can handle specific errors

try :
    a = int(input("enter the number:"))
    print(a)

except ValueError as v :
    print("this is not an integer ,enter a number")
    print(v)

except ZeroDivisionError as z :
    print(z)

except Exception as e :
    print(e)

print("thnxxxx")
