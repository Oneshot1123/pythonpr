import random

top_range= input("Type a Number : ")
if top_range.isdigit():
    top_range=int(top_range)

    if top_range<=0:
         print("Please Type A Number Greater Than 0 Next Time ")
         quit()

else:
    print("Please Enter A Number Next Time")
    quit()
    
number_guess = random.randrange(0,top_range)
guesses=0

while True:
    guesses +=1
    guesser=input("Make Your Guess : ")
    if guesser.isdigit():
        guesser=int(guesser)

    else:
        print("Please Type A Positive Number Next Time : ")
        continue

    if guesser == number_guess:
        print("You Got It Right")
        break
    else:
        if guesser > number_guess:
            print('You Were Above The Random Number')
        else:
            print("You Were Below The Random Number") 

print("You Took " + str(guesses) + " Guesses " ) 