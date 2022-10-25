import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc=pg.display.set_mode((1600,900))

    bg_sfc=pg.image.load("fig/pg_bg.jpg")
    bg_rect=bg_sfc.get_rect()

    tori_sfc=pg.image.load("fig/6.png")
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400

    clock=pg.time.Clock()
    
    while True:
        scrn_sfc.blit(bg_sfc,bg_rect)
        scrn_sfc.blit(tori_sfc,tori_rct)
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