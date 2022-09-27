import random
import datetime
rnd=random.randint(0,3)
que=["サザエの旦那の名前は？","カツオの妹の名前は?","タラオはカツオから見てどんな関係？"]
ans=["ますお","マスオ","わかめ","ワカメ","おい","甥","甥っ子","おいっこ"]
st=datetime.datetime.now()
def Syutudai():
    q=print(f"問題:{que[rnd]}")
    ua=input(f"解答:")
    return ua

def Kaito(ua):
    if ua in ans:
        print("正解!")
    else:
        print("カスめ")

def main():
    ua=Syutudai()
    Kaito(ua)
    ed=datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかったな")

main()