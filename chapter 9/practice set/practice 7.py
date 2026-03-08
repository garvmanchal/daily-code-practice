
with open("log.txt") as f :
    lines = f.readlines()


lineno = 1
for line in lines:
   if "python" in line :
       print(f"python is present. line no:{lineno}")
       break
   lineno +=1
   
else :
    print("no")
