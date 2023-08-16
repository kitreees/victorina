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

# bg_k = pygame.image.load('for game/bg_k.jpg')
# bg_a = pygame.image.load('for game/bg_a.jpg')

kpop_q1_img = pygame.image.load('for game/gidle.png')

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

score = 0
lose = False

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
    global main_screen, kpop_screen, anime_screen, kpop_q1, anime_q1, kpop_q2, anime_q2, score, lose
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(kpop_rect):
                        main_screen = False
                        kpop_screen = True
                        anime_screen = False
                        Kpop()
                    elif tap.colliderect(anime_rect):
                        main_screen = False
                        kpop_screen = False
                        anime_screen = True
                        Anime()


        if main_screen:
            sc.blit(bg, (0, 0))
            sc.blit(text, (350, 70))
            sc.blit(kpop, kpop_rect)
            sc.blit(anime, anime_rect)


        if kpop_screen:
            sc.blit(bg, (0, 0))
            kpop_q1 = True


        if anime_screen:
            sc.blit(bg, (0, 0))
            anime_q1 = True


        if kpop_q1:
            sc.blit(kpop_q1_img, (350, 50))
            sc.blit(txt, txt_rect)
            sc.blit(bts, bts_rect)
            sc.blit(twice, twice_rect)
            sc.blit(gidle, gidle_rect)
            if tap.colliderect(gidle_rect):
                score += 1
                kpop_q2 = True
            elif tap.colliderect(twice_rect):
                lose = True
            elif tap.colliderect(bts_rect):
                lose = True
            elif tap.colliderect(txt_rect):
                lose = True

        if kpop_q2:
            sc.blit(bg, (0, 0))
            sc.blit(kpop_q1_img, (350, 50))

        if lose and f_sc():
            sc.blit(bg, (0, 0))


        sc.blit(kursor, (x, y))

        clock.tick(FPS)
        pygame.display.update()



main()
