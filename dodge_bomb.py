import sys
import random
import pygame as pg



WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")  # 背景画像
    kk_img = pg.image.load("ex02/fig/3.png")  # こうかとんその3
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0) 
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

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
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

