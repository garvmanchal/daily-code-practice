# conditional expression : if/elif/else

# a = int(input("enter your age: "))
# if (a>=18):
#     print("you are not minor")

# else:
#     print("you are minor ")

# find the greatest of four numbers entered by users
# l = []

# for i in range(1,5):
#     i = int(input(f"enter the number {i}: "))
#     l.append(i)

# print(l)

# greatest= l[0]
# for x in l:
#     if x > greatest:
#         greatest = x
    
# print("greatest number is :", greatest)

marks = []
for i in range(1,4):
    i = int(input(f"enter the marks of subject {i} : "))
    marks.append(i)
print(marks)

total = 0
for x in marks :
    total = total + x

percentage =  (total * 100) / (len(marks)*100)
print(percentage)