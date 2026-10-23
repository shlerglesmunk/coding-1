#You know the rules
#pick between rock paper or scissors
#rock beats scissors, scissors beats paper, paper beats rock
#pick the better weapon to win

def rpsorsomething():
    rounds= 3
    print("ok lets go")
    weapon= input("choose thy weapon ")
    while rounds != 0:
        import random
        if weapon == (random.randint(1,3):