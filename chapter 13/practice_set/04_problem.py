def divisible5(n):
    if n % 5 == 0:
        return True
    return False

a = [1,2,220,43,5,6,80,76]

f = list(filter(divisible5,a))
print(f)