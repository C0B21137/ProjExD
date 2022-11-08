import tkinter as tk
import tkinter.messagebox as tkm

mx,my=28,385
move_l=1.0


def key_down(event): #5
    global key
    key=event.keysym

def key_up(event): #6
    global key
    key=""

def floor():
    global mx,my
    if mx<=28:
        mx=28
    elif 772<=mx:
        mx=772
    elif 385<=my:
        my=385

def chara_key():
    global mx,my,key
    if key=="Left":
        mx-=10
    if key=="Right":
        mx+=10
    floor()
    can.coords("tori",mx,my)
    root.after(100,chara_key)










if __name__ == "__main__":
    root=tk.Tk()
    root.title(f"こうかとんのアクション")

    can=tk.Canvas(root,width=800,height=480,bg="black") #2
    can.pack()
    can.update()
    width=can.winfo_width()
    height=can.winfo_height()
    

    background=tk.PhotoImage(file="fig/action.png")
    can.create_image(width/2,height/2,image=background,tag="bg")

    
    tori=tk.PhotoImage(file="fig/0.png")
    can.create_image(mx,my,image=tori,tag="tori")
    key="" #4

    root.bind("<KeyPress>",key_down) #5

    root.bind("<KeyRelease>",key_up) #6
    can.coords("tori",mx,my)
    chara_key()
    

    root.mainloop()