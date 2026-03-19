# New Features of python

# this is a way to define the variable is int or str or any other
# n :int = 5

# name : str = "garv"

# def office(employee_name : str , employee_salary : int) :
#     return f"{employee_name} and my salary is {employee_salary}"

# print(office("Garv" , 9000000))


# from typing import List , Tuple , Dict, Union

# # list of int
# numbers : List[int] = [1,2,4,5]

# # tuple of a str and int
# person : Tuple[str,int] = ("grv" , 19)

# # dict with a str and int values 
# scores : Dict[str,int] = {"Grv":19 , "Raj" : 22}

# # union type for variables that can hold multiple types
# identifier : Union[int,str] = "ID64F"

# Match Case

# def https_status(status):
#     match status :
#         case 200 :
#             return "ok"
#         case 404 :
#             return "Not found"
#         case 500 :
#             return "Internal Server Error"
#         case _:
#             return "unknown status"
        
# print(https_status(500))

# merge dict
# dict1 = {"a" :1 , "b" :4}
# dict2 = {"c" :6, "d" :9}

# merged = dict1 | dict2
# print(merged)

# Now we can open multiple files with the help of with statement

# with (
#     open("file1.txt") as f1 ,
#     open("file2.txt") as f2
# ):
#     pass

