import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event): #5
    global key
    key=event.keysym


if __name__=="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん") #1

    can=tk.Canvas(root,width=1500,height=900,bg="black") #2
    can.pack()

    tori=tk.PhotoImage(file="fig/5.png") #3
    cx,cy=300,400
    can.create_image(cx,cy,image=tori,tag="tori")

    key="" #4

    root.bind("<KeyPress>",key_down) #5

    root.mainloop()