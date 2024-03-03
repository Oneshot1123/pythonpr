from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.geometry("790x500")
# Giving the Background Color
root.configure(background="#0368bd")


def disableAllButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def scoreClearer():
    e_player1.delete(0, END)
    e_player2.delete(0, END)


def check():
    # Creating a variable called "winner" to suppose that nobody has won the game yet
    global winner
    winner = False

    # Checking if X wins the game
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="#46ff00")
        b2.config(bg="#46ff00")
        b3.config(bg="#46ff00")
        # Winner = True means that he won the game which is True
        winner = True
        # Fetching the value from the Entry box in the form of Float
        n = float(player1_var.get())
        # Creating a variable and asking it to the increase the value of Entry box by 1 If X wins the game
        score = (n+1)
        # Setting the score to the Entry Boxes
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b6.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="#46ff00")
        b8.config(bg="#46ff00")
        b9.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="#46ff00")
        b4.config(bg="#46ff00")
        b7.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b8.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="#46ff00")
        b6.config(bg="#46ff00")
        b9.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b9.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b7.config(bg="#46ff00")
        winner = True
        n = float(player1_var.get())
        score = (n+1)
        player1_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! X wins!!")
        disableAllButtons()

    # Checking if 0 wins the game
    elif b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0":
        b1.config(bg="#46ff00")
        b2.config(bg="#46ff00")
        b3.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0":
        b4.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b6.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0":
        b7.config(bg="#46ff00")
        b8.config(bg="#46ff00")
        b9.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0":
        b1.config(bg="#46ff00")
        b4.config(bg="#46ff00")
        b7.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0":
        b2.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b8.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0":
        b3.config(bg="#46ff00")
        b6.config(bg="#46ff00")
        b9.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0":
        b1.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b9.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    elif b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0":
        b3.config(bg="#46ff00")
        b5.config(bg="#46ff00")
        b7.config(bg="#46ff00")
        winner = True
        n = float(player2_var.get())
        score = (n+1)
        player2_var.set(score)
        messagebox.showinfo("Tic Tac Toe", "Congratulations!! 0 wins!!")
        disableAllButtons()

    # Checking If It's a Tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!. Play Again")
        disableAllButtons()


# X is going to starts the game First which is True
clicked = True
count = 0


def b_click(b):
    global clicked, count

    # If all buttons are empty, and if a person clicked the button, the first button he clicked will be "X"
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        # clicked = False means that now it's "0" turn
        clicked = False
        count += 1
        check()
    # If a button is empty, and if a second person clicked that button, then the button will appear as "0"
    elif b["text"] == " " and clicked == False:
        b["text"] = "0"
        # clicked = True means that now it's "X" turn
        clicked = True
        count += 1
        check()
    else:
        messagebox.showerror("Tic Tac Toe", "This Box is already filled. \nSelect another box.")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # Building Buttons
    b1 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b1.grid(row=0, column=0)

    b2 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b2.grid(row=0, column=1)

    b3 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b3))
    b3.grid(row=0, column=2)

    b4 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b4.grid(row=1, column=0)

    b5 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b5.grid(row=1, column=1)

    b6 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b6))
    b6.grid(row=1, column=2)

    b7 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b7.grid(row=2, column=0)

    b8 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b8.grid(row=2, column=1)

    b9 = Button(left_frame, text=" ", font="Cooper 20 bold", height=2, width=5, bg="SystemButtonFace",
                command=lambda: b_click(b9))
    b9.grid(row=2, column=2)


# Frames Top, Main, Right, Left
l_title = Label(root, text="Tic Tac Toe", font="Cooper 30 bold", justify=CENTER, fg="black", bg="#0368bd")
l_title.grid(row=0, column=0, pady=10)

main_frame = Frame(root, bg="#0773c4", relief=RIDGE, bd=15, pady=20, padx=20)
main_frame.grid(row=1, column=0, padx=20)

left_frame = Frame(main_frame, bg="#004f90", relief=RIDGE, bd=10, pady=20, padx=20)
left_frame.pack(side=LEFT, padx=10)

right_frame = Frame(main_frame, bg="#004f90", relief=RIDGE,  bd=10, pady=10, padx=10)
right_frame.pack(side=RIGHT, padx=10)

right_frame1 = Frame(right_frame, bg="#004f90", relief=RIDGE, bd=8, pady=10, padx=10)
right_frame1.grid(row=0, column=0, pady=5)

right_frame2 = Frame(right_frame, bg="#004f90", relief=RIDGE, bd=8, pady=10, padx=10)
right_frame2.grid(row=1, column=0, pady=5)


#  **^^  RIGHT FRAME-1  ^^**  #
# Labels for the Entry Boxes
l_player1 = Label(right_frame1, text="Player X:", font="Cooper 15 bold", bg="#004f90", padx=2, pady=2)
l_player1.grid(row=0, column=0, sticky=W, padx=5)

l_player2 = Label(right_frame1, text="Player 0:", font="Cooper 15 bold", bg="#004f90", padx=2, pady=2)
l_player2.grid(row=1, column=0, sticky=W, padx=5)


# Setting the variable name for the Entry Boxes
player1_var = IntVar()
player1_var.set(0)

player2_var = IntVar()
player2_var.set(0)


# Entry boxes for scores
e_player1 = Entry(right_frame1, textvariable=player1_var, font="Cooper 15 bold", width=10)
e_player1.grid(row=0, column=1)

e_player2 = Entry(right_frame1, textvariable=player2_var, font="Cooper 15 bold", width=10)
e_player2.grid(row=1, column=1)


# #  **^^  RIGHT FRAME-2  ^^**  #
# Buttons to reset and Clear Score
b_reset = Button(right_frame2, text="Reset", font="Cooper 15 bold", height=1, width=15, bg="#00fff0", bd=5,
                 command=reset)
b_reset.grid(row=0, column=0, pady=10)

b_clear = Button(right_frame2, text="Clear Score", font="Cooper 15 bold", height=1, width=15, bg="#00fff0", bd=5,
                 command=scoreClearer)
b_clear.grid(row=1, column=0)


reset()
root.mainloop()

