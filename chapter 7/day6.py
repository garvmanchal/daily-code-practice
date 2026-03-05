# loops

# list = ["garv", 45 , "harry" , True]

# i = 0

# while(i<len(list)):
#     print(list[i])
#     i+=1


# l = [1 ,4 ,6 ,234 ,6, 762]

# for i in l :
#     print(i)

# l = [1,4,5]

# for item in l :
#     print(item)
# else:
#     print("i am out of the loop")


# for i in range(78):
#     if (i == 3):
#       break
#     print(i)
    
# for i in range(78):
#     if (i == 3):
#       continue
#     print(i)

# n = int(input("enter the number :"))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

# l = ["harry" , "Soham" , "Sachin" , "Rahul"]

# for name in l :
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# n = int(input("enter the number :"))
# i = 1

# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i+=1


# n = int(input("enter the number: "))

# for i in range(2,n):
#     if (n % i) == 0:
#         print("its not a prime")
#         break
# else:
#         print("its a prime")


# n = int(input("enter the number :"))
# i = 1
# sum = 0
# while(i<=n):
#     sum+=i
#     i+=1

# print(sum)


# n = int(input("enter the number :"))
# fact = 1

# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# n = int(input("enter the number:"))
# for i in range(1 , n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     print("*" * i , end = "")
#     print("")

# n = int(input("enter the number:"))
# for i in range(1, n+1):
#     if (i == 1 or i ==n):
#         print("*" * n , end="")
#     else:
        # print("*" , end="")  # end is used for avoiding new line in python
#         print(" "* (n-2), end="")
#         print("*" , end="")
#     print("")


n = int(input("enter the number:"))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")