def rollie():
    score = 0
    roll = input("gamble???")
    die = 0

    while roll != 1:
        if roll != 1:
                import random
                random.randint(1,7)
                random = die
                print("you rolled a uhhhh " + str(die))
        
                if die != 7:
                    score +=10
                    print("ok ur score is now " + str(score))
                else:
                    score -=5
                    print("HAHA LOSER")
                    print("score is now uhh " + str(score))
        
                roll = input("gamblgamlbmalgmamglbmgamglbmgmalgmblgmglvb")
        

rollie()