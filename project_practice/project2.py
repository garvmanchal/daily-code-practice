import random

number = random.randint(1,10)
your_choice = -1
guesses = 0

while your_choice != number:
    your_choice = int(input("Enter your number: "))
    guesses +=1
    if your_choice > number :
        print("Lower Number PLease")
    elif your_choice < number:
        print("Higher Number Please")
    else :
        print("You guessed it correctly !!")
    
print(f"You have guessed the number {number} correctly in {guesses} attempts")