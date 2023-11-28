import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0, WIDTH)
    bb_rct.centery = random.randint(0, HEIGHT)
    vx, vy = +5, +5
    
    def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
        """
        オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
        引数　rct：こうかとんor爆弾surfaceのRect
        戻り値：横方向、縦方向にはみ出し判定（画面内：True, 画面外：False）
        """
    
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
        return yoko, tate
    
    clock = pg.time.Clock()
    tmr = 0
    kk_x, kk_y = 900, 400  # キャラクターの初期の位置
    kk_spd = 50  # 移動の速度
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        keys = pg.key.get_pressed()

        # 矢印キーで移動する
        if keys[pg.K_LEFT]:
            kk_x -= kk_spd
        if keys[pg.K_RIGHT]:
            kk_x += kk_spd
        if keys[pg.K_UP]:
            kk_y -= kk_spd
        if keys[pg.K_DOWN]:
            kk_y += kk_spd

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [kk_x, kk_y])
        bb_rct.centerx += vx
        bb_rct.centery += vy
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
