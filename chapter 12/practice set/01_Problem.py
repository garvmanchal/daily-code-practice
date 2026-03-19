
# try :
#     with(
#         open("file1.txt") as f1 ,
#         open("file2.txt") as f2 ,
#         open("file3.txt") as f3 
#     ):
#         print(f1.read())
#         print(f2.read())
#         print(f3.read())
# except FileNotFoundError :
#     print("file not found")

# except Exception as e:
#     print(e)

# print("thnxx")


# files = ["file1.txt" , "file2.txt", "file3.txt"]

# for file in files:
#     try :
#         with open(file) as f:
#             print(f"{file} opened")
#     except FileNotFoundError:
#         print(f"{file} not found")
   