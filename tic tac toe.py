from tkinter import * #Imports Tkinter
import sys #Imports sys, used to end the program later

from tkinter import messagebox
import random as r
root=Tk() #Declares root as the tkinter main window
#top =  #Creates the toplevel window
master=Tk()
entry1 = Entry(master,bg="papaya whip",width=10,font=('arial',24,'bold'),relief="sunken",bd=3) #Username entry
entry2 = Entry(master,bg="papaya whip",width=10,font=('arial',24,'bold'),relief="sunken",bd=3) #Password entry
button1 = Button(master,width=6,font=('arial',24,'bold'),relief="sunken",bd=3,text="Login", command=lambda:command1()) #Login button
button2 = Button(master,width=6,font=('arial',24,'bold'),relief="sunken",bd=3,text="Cancel", command=lambda:command2()) #Cancel button
lbl=Label(master,text="UserName",font=('arial',24,'bold'),bg="papaya whip",width=10,relief="sunken",bd=3)
lbl2=Label(master,text="Pass",font=('arial',24,'bold'),bg="papaya whip",width=10,relief="sunken",bd=3)
lbl3=Label(master,text="Please enter your default credential to play this game",font=('arial',24,'bold'),bg="papaya whip",width=50,relief="sunken",bd=3)
def command1():
    if entry1.get() == "user" and entry2.get() == "pass": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        master.destroy() #Removes the toplevel window

def command2():
    master.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script

def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
def rule():
        messagebox.showinfo("Rule", "The game is played on a grid that's 3 squares by 3 squares.")
        messagebox.showinfo("Rule", "You are X, your friend (or the computer in this case) is O. ...")
        messagebox.showinfo("Rule", "The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
        messagebox.showinfo("Rule", "The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
def about():
        messagebox.showinfo("About","Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os, is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. It is a solved game with a forced draw assuming best play from both players.")
def Quit():
        msg = messagebox.askquestion("Quit", "Do you want to quit ??")
        if msg == 'yes' :
           root.destroy()
           sys.exit()
        else :
            messagebox.showinfo('Returning','Return to your game')


###############   Main Program #################
master.title("Welcome to login page")
entry1.grid(row=100,column=8,columnspan=5) #These pack the elements, this includes the items for the main window
entry2.grid(row=150,column=8,columnspan=5)
button1.grid(row=200,column=7,columnspan=5)
button2.grid(row=250,column=7,columnspan=5)

lbl.grid(row=100,column=6,columnspan=5)
lbl2.grid(row=150,column=6,columnspan=5)
lbl3.grid(row=1,column=6,columnspan=5)
root.title("Tic-Tac-Toe by Sadique , Akash and Subodh")   #Title given
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]

for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
B1 = Button( text = "Game Rule", command = rule,font=('arial',20,'bold'))
B2 = Button( text = "About", command = about,font=('arial',20,'bold'))
B3 = Button( text = "Quit", command = Quit,font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
B1.grid(row=0,column=7,columnspan=5)
B2.grid(row=0,column=12,columnspan=6)
B3.grid(row=0,column=22,columnspan=6)



root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window
