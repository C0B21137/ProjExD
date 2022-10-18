import tkinter as tk
import tkinter.messagebox as tkm

if __name__=="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん") #1

    can=tk.Canvas(root,width=1500,height=900,bg="black") #2
    can.pack()
    
    root.mainloop()