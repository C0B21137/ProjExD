import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def key_down(event): #5
    global key
    key=event.keysym

def key_up(event): #6
    global key
    key=""

def main_proc(): #7
    global cx,cy
    if key=="Up":
        cy-=20
    if key=="Down":
        cy+=20
    if key=="Left":
        cx-=20
    if key=="Right":
        cx+=20
    can.coords("tori",cx,cy)
    root.after(100,main_proc)

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

    root.bind("<KeyRelease>",key_up) #6
    
    can.coords("tori",cx,cy) #7
    main_proc()
    root.mainloop()