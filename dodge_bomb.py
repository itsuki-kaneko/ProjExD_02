import sys
import random
import pygame as pg



WIDTH, HEIGHT = 1600, 900
delta = {pg.K_UP: (0, -5), 
         pg.K_DOWN: (0, +5),  #key:移動量, value(ヨコ, タテ)
         pg.K_LEFT: (-5, 0),
         pg.K_RIGHT: (+5, 0)}  # 練習3 移動量辞書


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")  # 背景画像
    kk_img = pg.image.load("ex02/fig/3.png")  # こうかとんその3
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0) 
    kk_rct = kk_img.get_rect()  # 練習3 こうかとんrect
    kk_rct.center = 900, 400
    bomb_img = pg.Surface((20, 20))  # 練習1 爆弾surfaceを作る
    bomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_rect = bomb_img.get_rect()
    bomb_rect.centerx = random.randint(0, WIDTH)
    bomb_rect.centery = random.randint(0, HEIGHT)
    vx, vy = +5, +5  # 練習2 爆弾の速度

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, tpl in delta.items():  # 練習3 こうかとんの移動量
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]

        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bomb_rect.move_ip(vx, vy)  # 練習2 爆弾の移動
        screen.blit(bomb_img, bomb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


# docstringの書き方
# def hage(fuga, piyo):
#     """
#     ここに説明
#     ここに説明
#     """
#     pass


# トップレベルの空行は2行
# インデント内部の空行は1行

