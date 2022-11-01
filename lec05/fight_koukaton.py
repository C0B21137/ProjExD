import pygame as pg
import sys
from random import randint
import os


main_dir = os.path.split(os.path.abspath(__file__))[0]
MAX_SHOTS = 200 # 連続発射可能弾数


class Time: # 追加機能１　時間表示
    def __init__(self):
        self.update()
        self.ti=pg.time.Clock()
        self.ti.tick(0.2)

    def update(self):
        pg.display.update()


class Music: # 追加機能２　音楽
    def __init__(self,file):
        if not pg.mixer:
            return None
        file = os.path.join(main_dir, "data", file)
        try:
            sound = pg.mixer.Sound(file)
            return sound
        except pg.error:
            print("Warning, unable to load, %s" % file)
        return None


class Screen:
    def __init__(self,title,tpl,png):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode(tpl)
        self.rct=self.sfc.get_rect()
        self.bg_sfc=pg.image.load(png)
        self.bg_rct=self.bg_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bg_sfc,self.bg_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb:
    def __init__(self,col,r,v,scr_obj:Screen):
        self.sfc=pg.Surface((r*2,r*2))
        self.sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.sfc,(col),(r,r),10)
        self.rct=self.sfc.get_rect()
        self.rct.centerx=randint(0,scr_obj.rct.width)
        self.rct.centery=randint(0,scr_obj.rct.height)
        self.vx,self.vy=v

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx,self.vy)
        yoko,tate=check_bound(self.rct,scr.rct)
        self.vx*=yoko
        self.vy*=tate
        self.blit(scr) # scr.sfc.blit(self.sfc,self.rct)


class reborn: #追加機能３　再生成
    def __init__(self,bomb:Bomb,scr:Screen):
        yoko,tate=check_bound(bomb.rct,scr.rct)
        if yoko==-1 or tate==-1:
            bomb.vx*=yoko
            bomb.vy*=tate
            bomb.rct.move_ip(bomb.vx,bomb.vy)
            scr.sfc.blit(bomb.sfc,bomb.rct)


# class atk: ###こうかとんからビームを出すクラス
#     key_delta = {
#         pg.K_SPACE
#         }
s
#     def __init__(self,bir:Bird):
#         self.sfc=pg.surface((10,10))
#         self.sfc=set_colorkey=((0,0,0))
#         pg.draw.circle(self.sfc,(255,0,0),(10,10),10)
#         self.rct=self.sfc.get_rect()
#         self.rct.centerx=bir.rct.centerx
#         self.rct.centery=bir.rct.centery
#         self.vx,self.vy=+1,+1

#     def v(self):
#         self.vy+=1


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    time=Time() # 時間表示
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    if pg.mixer: # 音楽再生
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        # 練習4
        kkt.update(scr)

        # 練習7
        bkd.update(scr)

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
