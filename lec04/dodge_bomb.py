import pygame as pg
import sys
from random import randint

def main():
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
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10) #円の描画
    bomb_rect=bomb_sfc.get_rect()
    bomb_rect.centerx=randint(0,scrn_rct.width)
    bomb_rect.centery=randint(0,scrn_rct.height)

    vx,vy=+1,+1
    clock=pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc,bg_rect)
        scrn_sfc.blit(tori_sfc,tori_rct)
        bomb_rect.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rect)
        pg.display.update()
        clock.tick(1000)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
        
        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]: #こうかとんの縦座標を＋１
            tori_rct.centery-=1
        if key_states[pg.K_DOWN]:
            tori_rct.centery+=1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx-=1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx+=1
        


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()