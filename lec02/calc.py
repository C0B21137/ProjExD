import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right
def button_click(event):
    button=event.widget
    number=int(button["text"])
    #tkm.showinfo({number},f"{number}のボタンが押されました。")
    entry.insert(tk.END,number)

root=tk.Tk()
root.title("calc")
root.geometry("300x600")

entry=tk.Entry(root,justify="right",width=10,font=("Times New Roma",40))
entry.grid(columnspan=3)

c=0
for i in range(10):
    button=tk.Button(root,text=9-i,font=("Times New Roman",30),width=4,height=2)
    button.bind=("<1>",button_click)
    button.grid(row=c+1,column=i%3)
    if i%3==2:
        c+=1


root.mainloop()