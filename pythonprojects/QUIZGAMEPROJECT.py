print("Welcome to my GK quiz !!!")
playing = input("do you want to play : ")

if playing.lower() != "yes":
    quit()

print("Okay lets play")
score = 0

answer=input("What Is Capital City of Austraila  :  ")
if answer.lower()=="canberra":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect")



answer=input("Which is the Longest River in the World  :  ")
if answer.lower()=="nile":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect")



answer=input("Who Is The G.O.A.T of football  :  ")
if answer.lower()=="messi":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect")



answer=input("What is The Capital City Of India  :  ")
if answer.lower()=="delhi":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect")



answer=input("What Is Powerhouse of the Cell  :  ")
if answer.lower()=="mitochondria":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect")

print("You got " + str(score)+ "Questions Correct")
print("You have got "+str((score/5)*100)+"%.")