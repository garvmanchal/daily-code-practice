from functools import reduce
l = [1,2, 220,43 ,532,643, 806]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,l))