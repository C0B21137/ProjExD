import random
import tkinter as tk
import tkinter.messagebox as tkm

def make_maze(yoko, tate):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = []
    for y in range(tate):
        maze_lst.append([0]*yoko)
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[y][yoko-1] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            maze_lst[y][x] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            if x > 2: rnd = random.randint(0, 2)
            else:     rnd = random.randint(0, 3)
            maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

    return maze_lst

def show_maze(canvas, maze_lst):
    color = ["white", "gray"]
    for y in range(len(maze_lst)):
        for x in range(len(maze_lst[y])):
            canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, 
                                    fill=color[maze_lst[y][x]])

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