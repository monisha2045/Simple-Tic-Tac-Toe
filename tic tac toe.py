from tkinter import *
import tkinter.messagebox as mb

tk = Tk()
tk.title("TIC-TAC-TOE")
p1 = StringVar()
p2 = StringVar()
p1_turn = True
flag = 0

l1 = Label(tk,text="Player 1 : (X)",font= "Times 12 bold",fg="black")
l1.grid(row=0,column=0)
player1 = Entry(tk,textvariable=p1,bd=5)
player1.grid(row=0,column=1)

l2 = Label(tk,text="Player 2 : (O)",font= "Times 12 bold",fg="black")
l2.grid(row=1,column=0)
player2 = Entry(tk,textvariable=p2,bd=5)
player2.grid(row=1,column=1)

def btn_click(button):
    global p1_turn,flag
    if button["text"] == "" and p1_turn:
        button["text"]="X"
        p1_turn = False
        check_winner()
        flag += 1
        
    elif button["text"] == "" and not p1_turn:
        button["text"] = "O"
        p1_turn = True
        check_winner()
        flag += 1
        
    else:
        mb.showinfo("TIC-TAC-TOE","Grid is already filled")
        
        
def check_winner():
    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or
        b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
        b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
        b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
        b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" or
        b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
        b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
        b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        mb.showinfo("TIC-TAC-TOE",p1.get()+" WINS") 
        disable()   
        
    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
        b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
        b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
        b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
        b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" or
        b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
        b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
        b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" ):
        mb.showinfo("TIC-TAC-TOE",p2.get()+" WINS")  
        disable()
        
    elif flag == 8:
        mb.showinfo("TIC-TAC-TOE","It is Tie")
        disable()
        
def disable():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)
        
def restart_button():
    global flag,p1_turn
    flag = 0
    p1_turn = True
    player1.delete(0,END)
    player2.delete(0,END)
    b1["text"] = b2["text"] = b3["text"] = b4["text"] = b5["text"] = b6["text"] = b7["text"] = b8["text"] = b9["text"] = ""
    b1.configure(state=NORMAL)
    b2.configure(state=NORMAL)
    b3.configure(state=NORMAL)
    b4.configure(state=NORMAL)
    b5.configure(state=NORMAL)
    b6.configure(state=NORMAL)
    b7.configure(state=NORMAL)
    b8.configure(state=NORMAL)
    b9.configure(state=NORMAL)
    



restart = Button(tk,text="Restart",font= "Times 12 bold",bg = "brown",fg = "white")
restart.grid(row=1,column=2)
restart.config(command = lambda:restart_button())

b1 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b1))
b1.grid(row=2,column=0)
b2 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b2))
b2.grid(row=2,column=1)
b3 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b3))
b3.grid(row=2,column=2)
b4 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b4))
b4.grid(row=3,column=0)
b5 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b5))
b5.grid(row=3,column=1)
b6 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b6))
b6.grid(row=3,column=2)
b7 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b7))
b7.grid(row=4,column=0)
b8 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b8))
b8.grid(row=4,column=1)
b9 = Button(tk,text="",font="Times 20 bold",bg = "black",fg = "white",height = 4,width = 8,command=lambda:btn_click(b9))
b9.grid(row=4,column=2)

tk.mainloop()