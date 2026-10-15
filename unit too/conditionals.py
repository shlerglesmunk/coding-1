#conditional if/else - keywords that give instructions based on conditions

#else is always the last option

#def college():
 #   grade= int(input("type in your grade"))
  #  if grade > 90:
   #     templeUApp()
    #else:
     #   ccpApp()

# choicelet = input("picketh one" )

#if choicelet == '1':
#    calculate_add()

#elif choicelet == '2':
#    calculate_sub()

#elif choicelet == '3':
#    calculate_multi()

#elif choicelet == '4':
#    calculate_divide()

#else:
#    print("bro")

#def calculate_add():
#    print("addition")
#    numberOnes = int(input())
#    numberTwos = int(input())
#    print(numberOnes + numberTwos)


#def calculate_sub():
#    print("subtraction")
#    numberOnes = int(input())
#    numberTwos = int(input())
#    print(numberOnes - numberTwos)

#def calculate_multi():
#    print("multiplication")
#    numberOnes = int(input())
#    numberTwos = int(input())
#    print(numberOnes * numberTwos)


#def calculate_divide():
#    print("division")
#    numberOnes = int(input())
#    numberTwos = int(input())
#    print(numberOnes % numberTwos)


age = int(input("type inyour age: " ))

if age < 8:
    print("dude where are your parents man - 8.00")

elif age > 8 and age < 21:
    print("you are WAY too lucky your life has not prolonged enough for me to pay you more. now gimme 12 dollar")

elif age > 21 and age < 61:
    print("olllldiiiiiieee - 20 dollar")

elif age > 61:
    print("dude its ok i know youre in retirement this one is on the house")

else:
    print("GET OUT")