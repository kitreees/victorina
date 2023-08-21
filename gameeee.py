import pygame, sys, time

pygame.init()

width = 1280
height = 720
FPS = 60

clock = pygame.time.Clock()
pygame.display.set_caption('Викторина')
sc = pygame.display.set_mode((width, height), pygame.RESIZABLE)
bg = pygame.image.load('for game/bg.jpg')
kursor = pygame.image.load('for game/kursor.png')

kpop = pygame.image.load('for game/k-pop.jpg')
kpop_rect = kpop.get_rect()
kpop_rect.x = 30
kpop_rect.y = 230
anime = pygame.image.load('for game/anime.jpg')
anime_rect = anime.get_rect()
anime_rect.x = 670
anime_rect.y = 230
# kpop1 = pygame.image.load('for game/k-pop1.jpg')
# anime1 = pygame.image.load('for game/anime1.jpg')
text = pygame.image.load('for game/text1.png')

main_screen = True
kpop_screen = False
anime_screen = False
kpop_q1 = False
anime_q1 = False
kpop_q2 = False
anime_q2 = False
kpop_q3 = False
anime_q3 = False

# bg_k = pygame.image.load('for game/bg_k.jpg')
# bg_a = pygame.image.load('for game/bg_a.jpg')

kpop_q1_img = pygame.image.load('for game/gidle.png')
kpop_q2_img = pygame.image.load('for game/enha.jpg')
kpop_q3_img = pygame.image.load('for game/g-idle.png')

txt = pygame.image.load('for game/txt.png')
txt_rect = txt.get_rect()
txt_rect.x = 90
txt_rect.y = 580

bts = pygame.image.load('for game/bts.png')
bts_rect = bts.get_rect()
bts_rect.x = 680
bts_rect.y = 580

twice = pygame.image.load('for game/twice.png')
twice_rect = twice.get_rect()
twice_rect.x = 90
twice_rect.y = 440

gidle = pygame.image.load('for game/(g)i-dle.png')
gidle_rect = gidle.get_rect()
gidle_rect.x = 680
gidle_rect.y = 440

enhypen = pygame.image.load('for game/enhypen.png')
enhypen_rect = enhypen.get_rect()
enhypen_rect.x = 680
enhypen_rect.y = 440

nmixx = pygame.image.load('for game/nmixx.png')
nmixx_rect = nmixx.get_rect()
nmixx_rect.x = 90
nmixx_rect.y = 440

yena = pygame.image.load('for game/yena.png')
yena_rect = yena.get_rect()
yena_rect.x = 680
yena_rect.y = 580

itzy = pygame.image.load('for game/itzy.png')
itzy_rect = itzy.get_rect()
itzy_rect.x = 90
itzy_rect.y = 580

sc0 = pygame.image.load('for game/0.png')
sc10 = pygame.image.load('for game/10.png')
sc20 = pygame.image.load('for game/20.png')


lose1k = False
lose2k = False
lose3k = False


# font = pygame.font.Font(None, 36)


def Kpop():
    global bg
    bg = pygame.image.load('for game/dudu.jpg')


def Anime():
    global bg
    bg = pygame.image.load('for game/bg_a.jpg')


def f_sc():
    global bg
    bg = pygame.image.load('for game/dddd.jpg')
    sc.blit(bg, (0, 0))


def kpop_q1_f():
    sc.blit(bg, (0, 0))
    sc.blit(kpop_q1_img, (350, 50))
    sc.blit(txt, txt_rect)
    sc.blit(bts, bts_rect)
    sc.blit(twice, twice_rect)
    sc.blit(gidle, gidle_rect)


def kpop_q2_f():
    sc.blit(bg, (0, 0))
    sc.blit(kpop_q2_img, (350, 50))
    sc.blit(txt, txt_rect)
    sc.blit(bts, bts_rect)
    sc.blit(twice, twice_rect)
    sc.blit(gidle, gidle_rect)

def kpop_q3_f():
    sc.blit(bg, (0, 0))
    sc.blit(kpop_q3_img, (350, 50))
    sc.blit(txt, txt_rect)
    sc.blit(bts, bts_rect)
    sc.blit(twice, twice_rect)
    sc.blit(gidle, gidle_rect)


def finish():
    # global bg
    # bg = pygame.image.load('for game/bg.jpg')
    #
    # fontScore = pygame.font.Font('for game/scootchover-sans.ttf', 18)
    # showScore = fontScore.render(f'Score: {score}', 1, pygame.Color('white'))
    #
    # sc.blit(bg, (0, 0))
    # sc.blit(showScore, (0, 0))
    #
    # time.sleep(2)

    pygame.quit()
    sys.exit()


def main():
    global main_screen, kpop_screen, anime_screen, kpop_q1, anime_q1, kpop_q2, anime_q2, kpop_q3, anime_q3, score, lose1k, lose2k
    score = 0
    x = 0
    y = 0

    while True:
        pygame.mouse.set_visible(False)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finish()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN and main_screen:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(kpop_rect):
                        main_screen = False
                        kpop_q1 = True
                        anime_screen = False
                        Kpop()
                    elif tap.colliderect(anime_rect):
                        main_screen = False
                        kpop_q1 = False
                        anime_screen = True
                        Anime()
            elif event.type == pygame.MOUSEBUTTONDOWN and kpop_q1:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(gidle_rect):
                        kpop_q1 = False
                        score += 10
                        kpop_q2 = True
                    elif tap.colliderect(twice_rect):
                        kpop_q1 = False
                        kpop_q2 = False
                        lose1k = True
                        f_sc()
                    elif tap.colliderect(bts_rect):
                        kpop_q1 = False
                        kpop_q2 = False
                        lose1k = True
                        f_sc()
                    elif tap.colliderect(txt_rect):
                        kpop_q1 = False
                        kpop_q2 = False
                        lose1k = True
                        f_sc()
            elif event.type == pygame.MOUSEBUTTONDOWN and kpop_q2:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(gidle_rect):
                        score += 10
                        kpop_q2 = False
                        kpop_q3 = True
                    elif tap.colliderect(twice_rect):
                        kpop_q2 = False
                        kpop_q3 = False
                        lose1k = True
                        f_sc()
                    elif tap.colliderect(bts_rect):
                        kpop_q2 = False
                        kpop_q3 = False
                        lose1k = True
                        f_sc()
                    elif tap.colliderect(txt_rect):
                        kpop_q2 = False
                        kpop_q3 = False
                        lose1k = True
                        f_sc()
            elif event.type == pygame.MOUSEBUTTONDOWN and kpop_q3:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(gidle_rect):
                        score += 1
                        kpop_q3 = False
                        kpop_q4 = True
                    elif tap.colliderect(twice_rect):
                        kpop_q3 = False
                        kpop_q4 = False
                        lose2k = True
                        f_sc()
                    elif tap.colliderect(bts_rect):
                        kpop_q3 = False
                        kpop_q4 = False
                        lose2k = True
                        f_sc()
                    elif tap.colliderect(txt_rect):
                        kpop_q3 = False
                        kpop_q4 = False
                        lose2k = True
                        f_sc()

        if main_screen:
            sc.blit(bg, (0, 0))
            sc.blit(text, (350, 70))
            sc.blit(kpop, kpop_rect)
            sc.blit(anime, anime_rect)
        #
        # if kpop_screen:
        #     sc.blit(bg, (0, 0))
        #     kpop_q1 = True

        if anime_screen:
            sc.blit(bg, (0, 0))
            anime_q1 = True

        if lose1k:
            f_sc()
            sc.blit(sc0, (350, 70))

        if lose2k:
            f_sc()
            sc.blit(sc10, (350, 70))

        if lose3k:
            f_sc()
            sc.blit(sc20, (350, 70))

        if kpop_q1:
            kpop_q1_f()

        if kpop_q2:
            kpop_q2_f()

        if kpop_q3:
            kpop_q3_f()

        sc.blit(kursor, (x, y))

        clock.tick(FPS)
        pygame.display.update()


main()