import tkinter as tk
import tkinter.messagebox as tkm
def button_click():
    tkm.showwarning("警告","ボタン押したらダメ言うたやろ")
print("hello world")
root=tk.Tk()
root.title("おためしか")
root.geometry("300x500")

label=tk.Label(root,
text="ラベルを書いてみた件",
font=("Times New Roman",20))
label.pack()

button=tk.Button(root,text="押すな",font=("Times New Roman",10),width=4,height=2,command=button_click())
button.pack()

entry=tk.Entry(width=30)
entry.insert(tk.END,"fugapiyo")
entry.pack()


root.mainloop()