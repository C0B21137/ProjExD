import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):#ボタンを押したときの関数
    button=event.widget
    number=(button["text"])
    #tkm.showinfo({number},f"{number}のボタンが押されました。")
    entry.insert(tk.END,number)

def click_eq(event):#＝を押したときの関数
    eq=entry.get()
    res=eval(eq)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

def click_acl(event):
    entry.delete(0,tk.END)

root=tk.Tk()#ウィンドウを作る
root.title("calc")
root.geometry("700x550")

entry=tk.Entry(root,justify="right",width=10,font=("Times New Roma",40))#表示バー
entry.grid(row=0,column=4,columnspan=3)

c=0 #数字のボタン
for i in range(10):
    button_num=tk.Button(root,text=f"{9-i}",font=("",30),width=4,height=2)
    button_num.bind("<1>",button_click)
    button_num.grid(row=c+1,column=i%3)
    if i%3==2:
        c+=1

#　+ボタン
button_p=tk.Button(root,text="+",font=("",30),width=4,height=2)
button_p.bind("<1>",button_click)
button_p.grid(row=4,column=1)
#　＝ボタン
button_eq=tk.Button(root,text="=",font=("",30),width=4,height=2)
button_eq.bind("<1>",click_eq)
button_eq.grid(row=4,column=2)

s=["-","*","/","%"]
a=0
for i in s:
    button_s=tk.Button(root,text=i,font=("",30),width=4,height=2)
    button_s.bind("<1>",button_click)
    button_s.grid(row=1,column=4+a)
    a+=1

button_acl=tk.Button(root,text="AC",font=("",30),width=4,height=2)
button_acl.bind("<1>",click_acl)
button_acl.grid(row=0,column=0)

root.mainloop()