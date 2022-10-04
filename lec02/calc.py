import tkinter as tk
import tkinter.messagebox as tkm
from tkinter.tix import COLUMN

def button_click(event):
    button=event.widget
    number=(button["text"])
    #tkm.showinfo({number},f"{number}のボタンが押されました。")
    entry.insert(tk.END,number)

root=tk.Tk()
root.title("calc")
root.geometry("300x600")

entry=tk.Entry(root,justify="right",width=10,font=("Times New Roma",40))
entry.grid(row=0,column=0,columnspan=3)

c=0
for i in range(10):
    button=tk.Button(root,text=f"{9-i}",font=("",30),width=4,height=2)
    button.bind=("<1>",button_click)
    button.grid(row=c+1,column=i%3)
    if i%3==2:
        c+=1
button=tk.Button(root,text="+",font=("",30),width=4,height=2)
button.bind("<1>",button_click)
button.grid(row=4,column=1)

root.mainloop()