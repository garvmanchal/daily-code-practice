from functools import reduce
# a = ["grv" , "rohan" , "shubham"]

# final1 = "-".join(a)
# final2 = "::".join(a)
# final3 = "/".join(a)
# print(final1)
# print(final2)
# print(final3)


# # format method
# a = "{} is a good {}".format("grv" , "boy")
# print(a)

# Map Filter Reduce

# map example
l = [1,2,4,3,6,7,9]

# sq = lambda x : x*x

# sqlist = map(sq,l)
# print(list(sqlist))

# filer example
def even(n):
    if n % 2 == 0 :
        return True
    return False

onlyEven= filter(even ,l)
print(list(onlyEven))

# reduce example

def sum(a,b):
    return a + b

mul = lambda x,y : x * y
print(reduce(sum,l)) 
print(reduce(mul,l)) 

'''
1  2  3  4 
\  /
  3   3   4           sequential computation 
  \   / 
    6   4
    \   /
      10 
   thats how reduce work in the above fxn
'''