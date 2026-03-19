# # global keyword : it changes the global variable
# # a = 56 
# # def fun():
# #     global a
# #     a = 3

# #     print(a)

# # fun()
# # print(a)

# # enumerate fxn
# l = [34,54,6,775,43,5]
# # index = 0
# # for item in l :
# #     print(f"the item number at index {index} is {item}")
# #     index +=1

# # this can be simplified using enumeratae fxn
# for index,item in enumerate(l):
#     print(f"the item number at index {index} is {item}")


# list comprehension

mylist = [1,2,3,4,6]

# squared_list = []
# for item in mylist:
#     squared_list.append(item*item)

squared_list = [i*i for i in mylist]

print(squared_list)


