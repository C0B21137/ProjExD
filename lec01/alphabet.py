import random
import datetime
import copy
qw=10
fn=random.randint(1,9)
st=datetime.datetime.now()
def que():
    alp=[]
    i=0
    while i==10:
        a=chr(random.randint(65,91))
        if a in alp:
            i-=1
            continue
        else:
            alp.append(a)
            i+=1
            continue
    a_alp=copy.copy(alp)
    f_alp=[]
    for i in range(fn):
        if i>0:
            fw=random.randint(0,len(a_alp)-1)
        else:
            fw=0
        f_alp.append(a_alp[fw])
        a_alp.pop(fw)
    print(f"出題文字：{alp}\n欠損文字:{f_alp}\n表示文字:{a_alp}")
    return f_alp

def ans(f_alp):
    a=int(input("消えた文字の数は？"))
    ans_w=[]
    if a==len(f_alp):
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください。")
        for i in range(len(f_alp)):
            b=input(f"{i+1}文字目を入力してください。")
            ans_w.append(b)
        if set(ans_w)==set(f_alp):
            print("正解です！")
        else:
            print("不正解です。またチャレンジしてね")
        ed=datetime.datetime.now()
        print(f"{ed-st}秒かかったよ")
    else:
        ans(f_alp)

def main():
    a=que()
    ans(a)

main()