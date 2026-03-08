import random

def game():
    print("You are playing the game....")
    score =random.randint(1,45)
    
    with open("hi-score.txt") as f :
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else :
           hiscore = 0

    print(f"Your socre :{score}")
    if score>hiscore or hiscore == "" :
      with open("hi-score.txt" ,"w") as f :
        f.write(str(score))     
        

    return score


game()



