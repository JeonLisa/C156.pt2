from tkinter import *
from PIL import Image,ImageTk
import random
root=Tk()
root.title("The Endless Dice Game")
root.geometry("500x500")
root.configure(background="Purple")
img=ImageTk.PhotoImage(Image.open("dice.jpg"))
label_player_1=Label(root,text="Player1",bg="Violet",fg="black")
label_player_2=Label(root,text="PLayer2",bg="Violet",fg="black")
label_player_1.place(relx=0.3,rely=0.2,anchor=CENTER)
label_player_2.place(relx=0.7,rely=0.2,anchor=CENTER)
label_score_1=Label(root,bg="Violet",fg="black")
label_score_2=Label(root,bg="Violet",fg="black")
label_score_1.place(relx=0.3,rely=0.3,anchor=CENTER)
label_score_2.place(relx=0.7,rely=0.3,anchor=CENTER)
label_random_num=Label(root,bg="Violet",fg="black")
label_random_num.place(relx=0.5,rely=0.8,anchor=CENTER)
player1_score=0
def player1():
    global player1_score
    random_num1=random.randint(1,6)
    label_random_num["text"]="player 1 dice random number"+str(random_num1)
    player1_score=player1_score+random_num1
    label_score_1["text"]=str(player1_score)
player2_score=0
def player2():
    global player2_score
    random_num2=random.randint(1,6)
    label_random_num["text"]="player 2 dice random number"+str(random_num2)
    player2_score=player2_score+random_num2
    label_score_2["text"]=str(player2_score)
button_1=Button(root,command=player1,image=img)
button_1.place(relx=0.3,rely=0.5,anchor=CENTER)
button_2=Button(root,command=player2,image=img)
button_2.place(relx=0.7,rely=0.5,anchor=CENTER)
root.mainloop()