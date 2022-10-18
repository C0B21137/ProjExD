import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm #8

def key_down(event): #5
    global key
    key=event.keysym

def key_up(event): #6
    global key
    key=""

def main_proc(): #7 #11
    global mx,my
    global cx,cy
    if key=="Up":
        my-=1
    if key=="Down":
        my+=1
    if key=="Left":
        mx-=1
    if key=="Right":
        mx+=1
    cx,cy=mx*100,my*100
    can.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__=="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん") #1

    can=tk.Canvas(root,width=1500,height=900,bg="black") #2
    can.pack()

    maze_list=mm.make_maze(15,9) #9
    mm.show_maze(can,maze_list) #10

    tori=tk.PhotoImage(file="fig/5.png") #3
    mx,my=1.5,1.5#11
    cx,cy=mx*100,my*100
    can.create_image(cx,cy,image=tori,tag="tori")

    key="" #4

    root.bind("<KeyPress>",key_down) #5

    root.bind("<KeyRelease>",key_up) #6
    
    can.coords("tori",cx,cy) #7
    main_proc()

    root.mainloop()