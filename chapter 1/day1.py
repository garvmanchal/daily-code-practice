# # import pyjokes

# # print("printing jokes....")
# # joke = pyjokes.get_joke()
# # print(joke)


# print('''
# No man is an island,
# Entire of itself,
# Every man is a piece of the continent,
# A part of the main.
# If a clod be washed away by the sea,
# Europe is the less.
# As well as if a promontory were.
# As well as if a manor of thy friend’s
# Or of thine own were:
# Any man’s death diminishes me,
# Because I am involved in mankind,
# And therefore never send to know for whom the bell tolls;
# It tolls for thee.''')



# for i in range(1,11):
#     print(f"5 X {i} = {5*i}")

# import pyttsx3

# engine = pyttsx3.init()
# engine.say("i am here for rebuilding skill")
# engine.runAndWait()

import os 

# from where we are going to fetch the data
directory_path = "/"  

# make a list of the data
content = os.listdir(directory_path)

#printing the item in the content
for item in content:
    print(item)


