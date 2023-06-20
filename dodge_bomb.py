import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

# 練習３
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT:(+5, 0)
}


def check_bound(rect: pg.Rect): # 練習４
    """
    こうかとんRect、爆弾Rectが画面外 or 画面内かを判定する関数
    引数:こうかとんRect or 爆弾Rect
    戻り値：横方向・縦方向の真理値タプル(True:画面内/Faise:画面外)
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom: # 縦方向判定
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")

    kk_img_sad = pg.image.load("ex02/fig/8.png")
    kk_img_sad = pg.transform.rotozoom(kk_img_sad, 0, 20)

    kk_imgf = pg.transform.flip(kk_img, True, False) # 反転させた鳥

    # 演習１
    kk_img1 = pg.transform.rotozoom(kk_imgf, 0, 2.0) # 右押された時の鳥
    kk_img2 = pg.transform.rotozoom(kk_imgf,- 45, 2.0) # 右下押された時の鳥
    kk_img3 = pg.transform.rotozoom(kk_imgf, -90, 2.0) # 下押された時の鳥
    kk_img4 = pg.transform.rotozoom(kk_img, 45, 2.0) # 左下押された時の鳥
    kk_img5 = pg.transform.rotozoom(kk_img, 0, 2.0) # 左押された時の鳥
    kk_img6 = pg.transform.rotozoom(kk_img, -45, 2.0) # 左上押された時の鳥
    kk_img7 = pg.transform.rotozoom(kk_imgf, 90, 2.0) # 上押された時の鳥
    kk_img8 = pg.transform.rotozoom(kk_imgf, 45, 2.0) # 右上押された時の鳥

    # 練習３
    kk_rct = kk_img.get_rect() # こうかとんのrectを生成
    kk_rct.center = 900, 400

    clock = pg.time.Clock()

    # 練習１
    bk_img = pg.Surface((20, 20)) 

    pg.draw.circle(bk_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bk_rect = bk_img.get_rect()
    bk_rect.center = x, y

    # 練習２
    vx, vy = +5, +5 

    bk_img.set_colorkey((0, 0, 0))
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        # 練習５
        if kk_rct.colliderect(bk_rect):
            return # ゲームオーバー
            
        # 練習３
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        # 練習４
        if check_bound(kk_rct) != (True, True): # こうかとん
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img1, kk_rct)

        # 練習２
        bk_rect.move_ip(vx, vy) 

        # 練習４
        yoko, tate = check_bound(bk_rect)
        if not yoko: # 横方向に画面外だったら
            vx *= -1
        if not tate:
            vy *= -1

        # 練習１
        screen.blit(bk_img, bk_rect) # 爆弾の表示

        pg.display.update()
        tmr += 1
        clock.tick(50) 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()