#Loop - A construct that repeats itself.
#there are two types which are while and for

#while loops the code as long as it is true

#while loop will always run unless you change a condition

#def guessinggame():
    #correctans= 10
    #userguess= int(input("type a number to guess"))
    #attempts= 0

    #while userguess != correctans:
        #print("AWFUL")
        #attempts +=1
        #print("attempts: " + str(attempts))
        #userguess= int(input("do it again "))
    #print ("yay cool you did it")

#guessinggame()


def password():
    correctans= 217
    userguess= int(input("password"))
    attempts= 0

    while userguess != correctans or attempts != 4:
        print("AWFUL")
        attempts +=1
        print("attempts: " + str(attempts))
        userguess= int(input("do it again "))


