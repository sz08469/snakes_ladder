import tkinter as tk
from PIL import ImageTk,Image
import random
from collections import deque



root=tk.Tk()
#creating a frame
root.geometry("5000x5000") 
root.title(" THE SNAKE AND LADDER GAME!!")

Frame1=tk.Frame(root,width=4000,height=4000,relief="raised")
Frame1.place(x=0,y=0)

image1=ImageTk.PhotoImage(Image.open("Downloads/snake1.png"))
label=tk.Label(Frame1,image=image1)
label.place(x=0,y=0)

def startgame():
    global im
    global button1,button2
    #buttons for player1 and player2
    #player1
    button1.place(x=800,y=400)
    #player2
    button2.place(x=800,y=500)
    #exitbutton
    button3=tk.Button(root,text="EXIT", height=1,width=15,fg="red",bg="pink",font=("Cursive",15,"bold"),activebackground="blue",command=root.destroy)
    button3.place(x=800,y=600)
    #dicebutton
    im=Image.open("Downloads/dice.png")
    im=im.resize((65,65))
    im=ImageTk.PhotoImage(im)
    button3=tk.Button(root,image=im,height=100,width=200)
    button3.place(x=800,y=250)
def reset_players():
    global player1,player2
    global pos1, pos2
    player1.place(x=0,y=510)
    player2.place(x=0,y=510)
    pos1=0
    pos2=0
def load_dice_images():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for i in names:
        im=Image.open("Downloads/"+i)
        im=im.resize((65,65))
        im=ImageTk.PhotoImage(im)
        Dice.append(im)
def check_Ladder(turn):
    global pos1, pos2
    global ladders
    again_turn=0
    if turn==1:
        if pos1 in ladders:
            pos1=ladders[pos1]
            a=min_dice_throws(pos1)
            b=("The minimum number of throws is "+str(a)+" which player1 needs at position "+str(pos1)+" to win the game.")
            # create a label widget with some text
            msg_label = tk.Label(root, text=b)
            msg_label.pack()
            msg_label.bind("<Button-1>", destroy_label)
            again_turn=1
    else:
        if pos2 in ladders:
            pos2=ladders[pos2]
            a=min_dice_throws(pos2)
            b=("The minimum number of throws is "+str(a)+" which player2 needs at position "+str(pos2)+" to win the game.")
            # create a label widget with some text
            msg_label = tk.Label(root, text=b)
            msg_label.pack()
            msg_label.bind("<Button-1>", destroy_label)
            again_turn=1
    return again_turn
def check_snake(turn):
    global pos1, pos2
    global snake
  
    if turn==1:
        if pos1 in snake:
            pos1=snake[pos1]
            a=min_dice_throws(pos1)
            b=("The minimum number of throws is "+str(a)+" which player1 needs at position "+str(pos1)+" to win the game.")
            # create a label widget with some text
            msg_label = tk.Label(root, text=b)
            msg_label.pack()
            msg_label.bind("<Button-1>", destroy_label)
            

    else:
        if pos2 in snake:
            pos2=snake[pos2]
            a=min_dice_throws(pos2)
            b=("The minimum number of throws is "+str(a)+" which player2 needs at position ",pos2," to win the game.")
            # create a label widget with some text
            msg_label = tk.Label(root, text=b)
            msg_label.pack()
            msg_label.bind("<Button-1>", destroy_label)

def roll_dice():
    global Dice
    global turn
    global pos1, pos2
    global button1,button2
    r=random.randint(1,10000) % 6 + 1
    dice=tk.Button(root,image=Dice[r-1],height=100,width=200)
    dice.place(x=800,y=250)
    #after throwing the dice we will move the player:
    if turn==1:
        if pos1+r<=100:
            pos1=pos1+r
            a=min_dice_throws(pos1)
            b=("The minimum number of throws is "+str(a)+" which player1 needs at position "+str(pos1)+" to win the game.")
            # create a label widget with some text
            msg_label = tk.Label(root, text=b)
            msg_label.pack()
            msg_label.bind("<Button-1>", destroy_label)
            #again_turn=1
        a=check_Ladder(turn)
        check_snake(turn)
        move_coin(turn,pos1)
        if r!=6 and a!=1:
            turn=2
            button1.configure(state="disabled")
            button2.configure(state="normal")
    else:
        if pos2+r<=100:
            pos2=pos2+r
            a=min_dice_throws(pos2)
            b=("The minimum number of throws is "+str(a)+" which player2 needs at position "+str(pos2)+" to win the game.")
            # create a label widget with some text
            msg_label = tk.Label(root, text=b)
            msg_label.pack()
            msg_label.bind("<Button-1>", destroy_label)
        a=check_Ladder(turn)
        check_snake(turn)
        move_coin(turn,pos2)
        if r!=6 and a!=1:
            turn=1
            button1.configure(state="normal")
            button2.configure(state="disabled")
    is_winner()
def is_winner():
    global pos1,pos2
    if pos1==100:
        a="PLAYER_1 WINS YOHOO!!"
        b=tk.Label(root,text=a,height=2,width=20,bg="red",font=("cursive",20,"bold"))
        b.place(x=400,y=100)
        b.bind("<Button-1>", destroy_label)
        reset_players()
    elif pos2==100:
        a="PLAYER_2 WINS YOHOO!!"
        b=tk.Label(root,text=a,height=2,width=20,bg="red",font=("cursive",20,"bold"))
        b.place(x=400,y=100)
        b.bind("<Button-1>", destroy_label)
        reset_players()
        
def move_coin(turn,r):
    global player1,player2
    global Index
    if turn==1:
        player1.place(x=Index[r][0],y=Index[r][1])
    else:
        player2.place(x=Index[r][0],y=Index[r][1])
def min_dice_throws(start):
    # Initialize a queue to store the positions
    queue = deque()
    queue.append(start)

    # Initialize a dictionary to store the distances from the start position
    distances = {start: 0}

    # Start the BFS algorithm
    while queue:
        current = queue.popleft()
        if current == 100:
            return distances[current]
        for i in range(1, 7):
            next_position = current + i
            if next_position in ladders:
                next_position = ladders[next_position]
            elif next_position in snake:
                next_position = snake[next_position]
            if next_position not in distances:
                distances[next_position] = distances[current] + 1
                queue.append(next_position)

    # If it's not possible to reach the end position
    return -1
    

#to store x and y co=ordinates of a given number
Index={}
def get_Index():
    global player1,player2
    Num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    #starting value of y:
    row=15
    i=0
    #for accessing rows(10 rows)
    for x in range(1,11):
        #starting value of x
        col=0 
        #for accessing columns(10 columns)
        for y in range(1,11):
            tuple1=(col,row)
            Index[Num[i]]=tuple1
            col=col+57
            i+=1
        row=row+55
    print(Index)
def destroy_label(event):
    event.widget.destroy()
#snakes
snake={28:10,37:3,47:16,75:32,94:71,96:42}
#ladders
ladders={4:56,12:50,14:55,22:58,41:79,54:88}
#players buttons:
#player1
button1=tk.Button(root,text="PLAYER 1", height=2,width=15,fg="black",bg="yellow",font=("Cursive",15,"bold"),activebackground="blue",command=roll_dice)
#player2
button2=tk.Button(root,text="PLAYER 2", height=2,width=15,fg="black",bg="orange",font=("Cursive",15,"bold"),activebackground="blue",command=roll_dice)

#initial positions of players:
pos1=None
pos2=None
#to load dice images
Dice=[]
#who is playing default(player 1)
turn=1

#player1 on the game
player1=tk.Canvas(root,width=40,height=40)
player1.create_oval(10,10,40,40,fill="yellow")
#player2 on the game
player2=tk.Canvas(root,width=40,height=40)
player2.create_oval(10,10,40,40,fill="orange")
turn=1

get_Index()
reset_players()
load_dice_images()
startgame()
root.mainloop()
