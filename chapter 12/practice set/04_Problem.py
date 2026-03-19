try :

    a = int(input("enter the number:"))
    b= int(input("enter the second number:")) 
    print(a/b)
except ZeroDivisionError as z :
    print("Infinite")



