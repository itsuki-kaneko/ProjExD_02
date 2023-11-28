import sys
import random
import pygame as pg



WIDTH, HEIGHT = 1600, 900
delta = {pg.K_UP: (0, -5), 
         pg.K_DOWN: (0, +5),  #key:移動量, value(ヨコ, タテ)
         pg.K_LEFT: (-5, 0),
         pg.K_RIGHT: (+5, 0)}  # 練習3 移動量辞書


def check_bound(rect: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面外に出そうになるかどうかの判定
    引数:対象のrect 戻り値:真理値のタプル(ヨコ, タテ) 
    戻り値は画面内ならFalse、画面外ならTrue
    """
    yoko, tate = False, False
    if rect.left < 0 or WIDTH < rect.right:
        yoko = True
    if rect.top < 0 or HEIGHT < rect.bottom:
        tate = True
    return (yoko, tate)


def kokaton_rotate(kk_img: pg.Surface):  # 課題1:こうかとん画像を切り替えるための辞書を用意する関数
    """
    こうかとんの移動量のタプルとrotozoomした画像の辞書を返す
    引数:こうかとんの画像(Surface型)
    戻り値:移動量タプルとrotozoom画像の辞書
    """
    kk_imgs = {}
    kk_mv = [(0, +5), (+5, +5), (+5, 0), (+5, -5), (0, -5), (-5, -5), (-5, 0), (-5, +5), (0, 0)]  # 移動量のタプルのリスト
    angle = -90  # こうかとんの角度
    flip = True
    for k in kk_mv[:8]:
        if angle > 90:  # 角度が半周以上したら
            angle -= 180  # 角度を一度リセットして
            flip = False  # 左右反転
        kk = kk_img
        kk = pg.transform.flip(kk, flip, False)
        kk = pg.transform.rotozoom(kk, angle, 2.0)
        kk_imgs[k] = kk  # key:移動量タプル value:手を加えたこうかとんsurface
        angle += 45  #角度を45度回す
    kk_imgs[kk_mv[8]] = pg.transform.rotozoom(kk_img, 0, 2.0)  # 静止状態の画像を追加
    return kk_imgs


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")  # 背景画像
    kk_img = pg.image.load("ex02/fig/3.png")  # こうかとんその3
    kk_imgs = kokaton_rotate(kk_img)  # 課題1:こうかとん画像を切り替えるための辞書を用意する関数
    kk_rct = kk_img.get_rect()  # 練習3 こうかとんrect
    kk_rct.center = 900, 400
    bomb_img = pg.Surface((20, 20))  # 練習1 爆弾surfaceを作る
    bomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_boost = 1.2  # 課題2: 爆弾の加速度
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
        if kk_rct.colliderect(bomb_rect):
            kk_go = pg.image.load("ex02/fig/8.png")  # 課題3 ゲームオーバー画像のロード
            kk_go = pg.transform.rotozoom(kk_go, 0, 2.0)
            screen.blit(bg_img, [0, 0])
            screen.blit(kk_go, kk_rct)
            pg.display.update()  # 課題3 画面のアップデート(画像表示)
            clock.tick(1)  # 課題3 画像の表示時間を作る(1秒間)
            print("GAME OVER")
            return
        
        if (tmr+1) % 250 == 0 and (tmr+1) // 250 <= 10:  # 課題2: 時間カウントが250ごとに(5秒ごとに)1加速、最大10回
            vx *= bomb_boost  # vx, vyそれぞれにbomb_boostを掛けることでvx, vyの正負に関係なく加速するようにする
            vy *= bomb_boost
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, tpl in delta.items():  # 練習3 こうかとんの移動量
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]

        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (False, False):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_imgs[(sum_mv[0], sum_mv[1])], kk_rct)  # 課題1:kk_imgsがsum_mvにあうようにする
        bomb_rect.move_ip(vx, vy)  # 練習2 爆弾の移動
        yoko, tate = check_bound(bomb_rect)
        if yoko:
            vx *= -1
        if tate:
            vy *= -1
        screen.blit(bomb_img, bomb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


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

