import pygame as pg
import sys
from random import randint
import time
import tkinter as tk
import tkinter.messagebox as tkm

a=0
def check_bound(obj_rect,scr_rect):
    """
    obj_rect:こうかとんor 爆弾のrect
    scr_rct:スクリーンrect
    """
    yoko,tate=+1,+1
    if obj_rect.left<scr_rect.left or scr_rect.right<obj_rect.right:
        yoko=-1
    if obj_rect.top<scr_rect.top or scr_rect.bottom<obj_rect.bottom:
        tate=-1

    return yoko,tate

def main():
    global a
    root=tk.Tk()
    root.withdraw()
    start=time.time()
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc=pg.display.set_mode((1600,900))
    scrn_rct=scrn_sfc.get_rect()

    bg_sfc=pg.image.load("fig/pg_bg.jpg")
    bg_rect=bg_sfc.get_rect()

    tori_sfc=pg.image.load("fig/6.png")
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400

    bomb_sfc=pg.Surface((20,20)) #空のsurface
    bomb_sfc.set_colorkey((0,0,0)) #黒い部分の透過
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10) #赤い球の描画
    bomb_rect=bomb_sfc.get_rect()
    bomb_rect.centerx=randint(0,scrn_rct.width)
    bomb_rect.centery=randint(0,scrn_rct.height)

    bomb_sfc2=pg.Surface((20,20)) #空のsurface
    bomb_sfc2.set_colorkey((0,0,0)) #黒い部分の透過
    pg.draw.circle(bomb_sfc2,(0,0,255),(10,10),20) #黒い玉の描画
    bomb_rect2=bomb_sfc2.get_rect()
    bomb_rect2.centerx=randint(0,scrn_rct.width)
    bomb_rect2.centery=randint(0,scrn_rct.height)

    vx,vy=+1,+1
    fx,fy=+2,+2
    clock=pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc,bg_rect)
        
        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]: #こうかとんの縦座標を＋１
            tori_rct.centery-=1
        if key_states[pg.K_DOWN]:
            tori_rct.centery+=1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx-=1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx+=1
        yoko,tate=check_bound(tori_rct,scrn_rct)
        if yoko==-1 :
            if key_states[pg.K_LEFT]:
                tori_rct.centerx+=1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx-=1
        if tate==-1:
            if key_states[pg.K_UP]: #こうかとんの縦座標を＋１
                tori_rct.centery+=1
            if key_states[pg.K_DOWN]:
                tori_rct.centery-=1
        scrn_sfc.blit(tori_sfc,tori_rct)

        yoko,tate=check_bound(bomb_rect,scrn_rct)
        if yoko==-1 or tate==-1: #赤い球が壁にぶつかったら位置をランダムで再生成
            bomb_rect.centerx=randint(0,scrn_rct.width)
            bomb_rect.centery=randint(0,scrn_rct.height)
        vx*=yoko
        vy*=tate
        bomb_rect.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rect)

        yoko,tate=check_bound(bomb_rect2,scrn_rct)
        if yoko==-1 or tate==-1: #黒い球が壁にぶつかったら位置をランダムで再生成
            bomb_rect2.centerx=randint(0,scrn_rct.width)
            bomb_rect2.centery=randint(0,scrn_rct.height)
        fx*=yoko
        fy*=tate
        bomb_rect2.move_ip(fx,fy)
        scrn_sfc.blit(bomb_sfc2,bomb_rect2)

        if tori_rct.colliderect(bomb_rect):
            end=time.time()
            tkm.showinfo("終わり",f"{end-start:.3f}秒")
            return

        if tori_rct.colliderect(bomb_rect2):
            end=time.time()
            tkm.showinfo("終わり",f"{end-start:.3f}秒")
            return

        pg.display.update()
        clock.tick(1000)

        for event in pg.event.get():
            if event.type==pg.QUIT:
                return

if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()