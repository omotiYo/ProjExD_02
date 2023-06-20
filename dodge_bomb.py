import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

#練習３
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT:(+5, 0)
}

def check_bound(rect: pg.Rect): #練習４
    """
    こうかとんRect、爆弾Rectが画面外 or 画面内かを判定する関数
    引数:こうかとんRect or 爆弾Rect
    戻り値：横方向・縦方向の真理値タプル(True:画面内/Faise:画面外)
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  #横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom: #縦方向判定
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    #練習３
    kk_rct = kk_img.get_rect() #こうかとんのrectを生成
    kk_rct.center = 900, 400

    clock = pg.time.Clock()

    bk_img = pg.Surface((20, 20)) #練習１
    pg.draw.circle(bk_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bk_rect = bk_img.get_rect()
    bk_rect.center = x, y

    vx, vy = +5, +5 #練習２

    bk_img.set_colorkey((0, 0, 0))
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        #練習３
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        #練習４
        if check_bound(kk_rct) != (True, True): #こうかとん
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bk_rect.move_ip(vx, vy) #練習２

        yoko, tate = check_bound(bk_rect)
        if not yoko: #横方向に画面外だったら
            vx *= -1
        if not tate:
            vy *= -1
            
        screen.blit(bk_img, bk_rect) #練習１、爆弾の表示

        pg.display.update()
        tmr += 1
        clock.tick(50) 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()