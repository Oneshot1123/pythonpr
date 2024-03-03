import random

user_guess = 0
comp_guess = 0

options=["rock","paper","scissors"]

while True:
    user_inp=input("Please Enter Your Option ie Rock , Paper, Scissors or Q to Quit : ").lower()
    if user_inp == "q":
        break

    if user_inp not in options:
        continue

    number=random.randrange(0,2)
    # 0 = rock , 1= paper , 2=scissors
    pick_comp=options[number]
    print("Computer Picked " , pick_comp ,"." )

    if user_inp == "rock" and pick_comp == "scissors":
        print("user won")
        user_guess +=1

    elif user_inp == "paper" and pick_comp == "rock":
        print("user won")
        user_guess +=1

    elif user_inp == "scissors" and pick_comp == "paper":
        print("user won")
        user_guess +=1

    elif user_inp == "scissors" and pick_comp == "scissors":
        print("Nobody Won It Was A Draw")
    
    elif user_inp == "paper" and pick_comp == "paper":
        print("Nobody Won It Was A Draw")
    
    elif user_inp == "rock" and pick_comp == "rock":
        print("Nobody Won It Was A Draw")

    else:
        print("You Lost!!!")
        comp_guess +=1
        
print("You Won ",user_guess,"Times.")
print("Computer won ", comp_guess,"Times")
print("Adios Amigos")