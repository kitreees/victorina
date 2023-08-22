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
kpop_q4 = False
anime_q4 = False
kpop_q5 = False
anime_q5 = False

# bg_k = pygame.image.load('for game/bg_k.jpg')
# bg_a = pygame.image.load('for game/bg_a.jpg')

kpop_q1_img = pygame.image.load('for game/gidle.png')
kpop_q2_img = pygame.image.load('for game/enha.jpg')
kpop_q3_img = pygame.image.load('for game/le serafime.jpg')
kpop_q4_img = pygame.image.load('for game/seventeen.png')
kpop_q5_img = pygame.image.load('for game/purple kiss.png')

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

exo = pygame.image.load('for game/exo.png')
exo_rect = exo.get_rect()
exo_rect.x = 680
exo_rect.y = 440

aespa = pygame.image.load('for game/aespa.png')
aespa_rect = aespa.get_rect()
aespa_rect.x = 90
aespa_rect.y = 440

leserafim = pygame.image.load('for game/leserafim.png')
leserafim_rect = leserafim.get_rect()
leserafim_rect.x = 680
leserafim_rect.y = 580

everglow = pygame.image.load('for game/everglow.png')
everglow_rect = everglow.get_rect()
everglow_rect.x = 90
everglow_rect.y = 580

svt = pygame.image.load('for game/svt.png')
svt_rect = svt.get_rect()
svt_rect.x = 680
svt_rect.y = 440

triples = pygame.image.load('for game/triple s.png')
triples_rect = triples.get_rect()
triples_rect.x = 90
triples_rect.y = 440

xg = pygame.image.load('for game/xg.png')
xg_rect = xg.get_rect()
xg_rect.x = 680
xg_rect.y = 580

mave = pygame.image.load('for game/mave.png')
mave_rect = mave.get_rect()
mave_rect.x = 90
mave_rect.y = 580

stayc = pygame.image.load('for game/stayc.png')
stayc_rect = stayc.get_rect()
stayc_rect.x = 680
stayc_rect.y = 440

kepler = pygame.image.load('for game/kepler.png')
kepler_rect = kepler.get_rect()
kepler_rect.x = 90
kepler_rect.y = 440

ive = pygame.image.load('for game/ive.png')
ive_rect = ive.get_rect()
ive_rect.x = 680
ive_rect.y = 580

purple_kiss = pygame.image.load('for game/pk.png')
purple_kiss_rect = purple_kiss.get_rect()
purple_kiss_rect.x = 90
purple_kiss_rect.y = 580

sc0 = pygame.image.load('for game/0.png')
sc10 = pygame.image.load('for game/10.png')
sc20 = pygame.image.load('for game/20.png')
sc30 = pygame.image.load('for game/30.png')
sc40 = pygame.image.load('for game/40.png')
win = pygame.image.load('for game/win.png')

anime_q1_img = pygame.image.load('for game/krd.png')
anime_q2_img = pygame.image.load('for game/mha.png')
anime_q3_img = pygame.image.load('for game/noragami.jpg')
anime_q4_img = pygame.image.load('for game/bsd.jpg')
anime_q5_img = pygame.image.load('for game/blue lock.png')

naruto = pygame.image.load('for game/naruto.png')
naruto_rect = naruto.get_rect()
naruto_rect.x = 680
naruto_rect.y = 440

sxf = pygame.image.load('for game/sxf.png')
sxf_rect = sxf.get_rect()
sxf_rect.x = 90
sxf_rect.y = 440

ds = pygame.image.load('for game/ds.png')
ds_rect = ive.get_rect()
ds_rect.x = 680
ds_rect.y = 580

jjk = pygame.image.load('for game/jjk.png')
jjk_rect = jjk.get_rect()
jjk_rect.x = 90
jjk_rect.y = 580

mha = pygame.image.load('for game/my hero academia.png')
mha_rect = mha.get_rect()
mha_rect.x = 90
mha_rect.y = 580

god = pygame.image.load('for game/naruto.png')
god_rect = god.get_rect()
god_rect.x = 680
god_rect.y = 440

titan = pygame.image.load('for game/attack on titan.png')
titan_rect = titan.get_rect()
titan_rect.x = 90
titan_rect.y = 440

neverland = pygame.image.load('for game/neverland.png')
neverland_rect = neverland.get_rect()
neverland_rect.x = 680
neverland_rect.y = 580

tm = pygame.image.load('for game/tm.png')
tm_rect = tm.get_rect()
tm_rect.x = 90
tm_rect.y = 580

dororo = pygame.image.load('for game/dororo.png')
dororo_rect = dororo.get_rect()
dororo_rect.x = 680
dororo_rect.y = 440

noragami = pygame.image.load('for game/bezdomniy bog.png')
noragami_rect = noragami.get_rect()
noragami_rect.x = 90
noragami_rect.y = 440

td = pygame.image.load('for game/td.png')
td_rect = td.get_rect()
td_rect.x = 680
td_rect.y = 580

op = pygame.image.load('for game/op.png')
op_rect = op.get_rect()
op_rect.x = 90
op_rect.y = 580

bsd = pygame.image.load('for game/bsdd.png')
bsd_rect = bsd.get_rect()
bsd_rect.x = 680
bsd_rect.y = 440

hk = pygame.image.load('for game/haikyuu.png')
hk_rect = hk.get_rect()
hk_rect.x = 90
hk_rect.y = 440

cm = pygame.image.load('for game/cm.png')
cm_rect = cm.get_rect()
cm_rect.x = 680
cm_rect.y = 580

akame = pygame.image.load('for game/akame.png')
akame_rect = akame.get_rect()
akame_rect.x = 90
akame_rect.y = 580

bk = pygame.image.load('for game/black klever.png')
bk_rect = bk.get_rect()
bk_rect.x = 680
bk_rect.y = 440

opm = pygame.image.load('for game/opm.png')
opm_rect = opm.get_rect()
opm_rect.x = 90
opm_rect.y = 440

blue_lock = pygame.image.load('for game/bl.png')
blue_lock_rect = blue_lock.get_rect()
blue_lock_rect.x = 680
blue_lock_rect.y = 580

lose1k = False
lose2k = False
lose3k = False
lose4k = False
lose5k = False
lose1a = False
lose2a = False
lose3a = False
lose4a = False
lose5a = False
winner_k = False
winner_a = False


# font = pygame.font.Font(None, 36)


def Kpop():
    global bg
    bg = pygame.image.load('for game/dudu.jpg')


def Anime():
    global bg
    bg = pygame.image.load('for game/fjg.jpg')


def f_sc_k():
    global bg
    bg = pygame.image.load('for game/dddd.jpg')
    sc.blit(bg, (0, 0))

def f_sc_a():
    global bg
    bg = pygame.image.load('for game/sff.jpg')
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
    sc.blit(kpop_q2_img, (500, 50))
    sc.blit(enhypen, enhypen_rect)
    sc.blit(yena, yena_rect)
    sc.blit(nmixx, nmixx_rect)
    sc.blit(itzy, itzy_rect)

def kpop_q3_f():
    sc.blit(bg, (0, 0))
    sc.blit(kpop_q3_img, (350, 50))
    sc.blit(everglow, everglow_rect)
    sc.blit(leserafim, leserafim_rect)
    sc.blit(aespa, aespa_rect)
    sc.blit(exo, exo_rect)

def kpop_q4_f():
    sc.blit(bg, (0, 0))
    sc.blit(kpop_q4_img, (350, 50))
    sc.blit(svt, svt_rect)
    sc.blit(xg, xg_rect)
    sc.blit(mave, mave_rect)
    sc.blit(triples, triples_rect)

def kpop_q5_f():
    sc.blit(bg, (0, 0))
    sc.blit(kpop_q5_img, (350, 50))
    sc.blit(stayc, stayc_rect)
    sc.blit(ive, ive_rect)
    sc.blit(purple_kiss, purple_kiss_rect)
    sc.blit(kepler, kepler_rect)

def anime_q1_f():
    sc.blit(bg, (0, 0))
    sc.blit(anime_q1_img, (350, 50))
    sc.blit(jjk, jjk_rect)
    sc.blit(naruto, naruto_rect)
    sc.blit(ds, ds_rect)
    sc.blit(sxf, sxf_rect)


def anime_q2_f():
    sc.blit(bg, (0, 0))
    sc.blit(anime_q2_img, (350, 50))
    sc.blit(titan, titan_rect)
    sc.blit(mha, mha_rect)
    sc.blit(god, god_rect)
    sc.blit(neverland, neverland_rect)

def anime_q3_f():
    sc.blit(bg, (0, 0))
    sc.blit(anime_q3_img, (350, 50))
    sc.blit(td, td_rect)
    sc.blit(tm, tm_rect)
    sc.blit(noragami, noragami_rect)
    sc.blit(dororo, dororo_rect)

def anime_q4_f():
    sc.blit(bg, (0, 0))
    sc.blit(anime_q4_img, (375, 150))
    sc.blit(bsd, bsd_rect)
    sc.blit(op, op_rect)
    sc.blit(cm, cm_rect)
    sc.blit(hk, hk_rect)

def anime_q5_f():
    sc.blit(bg, (0, 0))
    sc.blit(anime_q5_img, (375, 150))
    sc.blit(blue_lock, blue_lock_rect)
    sc.blit(opm, opm_rect)
    sc.blit(akame, akame_rect)
    sc.blit(bk, bk_rect)


def finish():

    pygame.quit()
    sys.exit()


def main():
    global main_screen, kpop_screen, anime_screen, kpop_q1, anime_q1, kpop_q2, anime_q2, kpop_q3, anime_q3, kpop_q4, anime_q4, kpop_q5, anime_q5, score, lose1k, lose2k, lose3k, lose4k, lose5k, lose1a, lose2a, lose3a, lose4a, lose5a, winner_k, winner_a
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
                        anime_q1 = True
                        kpop_screen = False
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
                        f_sc_k()
                    elif tap.colliderect(bts_rect):
                        kpop_q1 = False
                        kpop_q2 = False
                        lose1k = True
                        f_sc_k()
                    elif tap.colliderect(txt_rect):
                        kpop_q1 = False
                        kpop_q2 = False
                        lose1k = True
                        f_sc_k()
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
                        lose2k = True
                        f_sc_k()
                    elif tap.colliderect(bts_rect):
                        kpop_q2 = False
                        kpop_q3 = False
                        lose2k = True
                        f_sc_k()
                    elif tap.colliderect(txt_rect):
                        kpop_q2 = False
                        kpop_q3 = False
                        lose2k = True
                        f_sc_k()
            elif event.type == pygame.MOUSEBUTTONDOWN and kpop_q3:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(leserafim_rect):
                        score += 10
                        kpop_q3 = False
                        kpop_q4 = True
                    elif tap.colliderect(aespa_rect):
                        kpop_q3 = False
                        kpop_q4 = False
                        lose3k = True
                        f_sc_k()
                    elif tap.colliderect(exo_rect):
                        kpop_q3 = False
                        kpop_q4 = False
                        lose3k = True
                        f_sc_k()
                    elif tap.colliderect(everglow_rect):
                        kpop_q3 = False
                        kpop_q4 = False
                        lose3k = True
                        f_sc_k()
            elif event.type == pygame.MOUSEBUTTONDOWN and kpop_q4:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(svt_rect):
                        score += 10
                        kpop_q4 = False
                        kpop_q5 = True
                    elif tap.colliderect(xg_rect):
                        kpop_q4 = False
                        kpop_q5 = False
                        lose4k = True
                        f_sc_k()
                    elif tap.colliderect(mave_rect):
                        kpop_q4 = False
                        kpop_q5 = False
                        lose4k = True
                        f_sc_k()
                    elif tap.colliderect(triples_rect):
                        kpop_q4 = False
                        kpop_q5 = False
                        lose4k = True
                        f_sc_k()

            elif event.type == pygame.MOUSEBUTTONDOWN and kpop_q5:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(purple_kiss_rect):
                        score += 10
                        winner_k = True
                        f_sc_k()
                    elif tap.colliderect(stayc_rect):
                        kpop_q5 = False
                        lose5k = True
                        f_sc_k()
                    elif tap.colliderect(ive_rect):
                        kpop_q5 = False
                        lose5k = True
                        f_sc_k()
                    elif tap.colliderect(kepler_rect):
                        kpop_q5 = False
                        lose5k = True
                        f_sc_k()



            elif event.type == pygame.MOUSEBUTTONDOWN and anime_q1:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(ds_rect):
                        anime_q1 = False
                        score += 10
                        anime_q2 = True
                    elif tap.colliderect(jjk_rect):
                        anime_q1 = False
                        anime_q2 = False
                        lose1a = True
                        f_sc_a()
                    elif tap.colliderect(naruto_rect):
                        anime_q1 = False
                        anime_q2 = False
                        lose1a = True
                        f_sc_a()
                    elif tap.colliderect(sxf_rect):
                        anime_q1 = False
                        anime_q2 = False
                        lose1a = True
                        f_sc_a()
            elif event.type == pygame.MOUSEBUTTONDOWN and anime_q2:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(mha_rect):
                        score += 10
                        anime_q2 = False
                        anime_q3 = True
                    elif tap.colliderect(titan_rect):
                        anime_q2 = False
                        anime_q3 = False
                        lose2a = True
                        f_sc_a()
                    elif tap.colliderect(neverland_rect):
                        anime_q2 = False
                        anime_q3 = False
                        lose2a = True
                        f_sc_a()
                    elif tap.colliderect(god_rect):
                        anime_q2 = False
                        anime_q3 = False
                        lose2a = True
                        f_sc_a()
            elif event.type == pygame.MOUSEBUTTONDOWN and anime_q3:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(noragami_rect):
                        score += 10
                        anime_q3 = False
                        anime_q4 = True
                    elif tap.colliderect(dororo_rect):
                        anime_q3 = False
                        anime_q4 = False
                        lose3a = True
                        f_sc_a()
                    elif tap.colliderect(tm_rect):
                        anime_q3 = False
                        anime_q4 = False
                        lose3a = True
                        f_sc_a()
                    elif tap.colliderect(td_rect):
                        anime_q3 = False
                        anime_q4 = False
                        lose3a = True
                        f_sc_a()
            elif event.type == pygame.MOUSEBUTTONDOWN and anime_q4:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(bsd_rect):
                        score += 10
                        anime_q4 = False
                        anime_q5 = True
                    elif tap.colliderect(op_rect):
                        anime_q4 = False
                        anime_q5 = False
                        lose4a = True
                        f_sc_a()
                    elif tap.colliderect(cm_rect):
                        anime_q4 = False
                        anime_q5 = False
                        lose4a = True
                        f_sc_a()
                    elif tap.colliderect(hk_rect):
                        anime_q4 = False
                        anime_q5 = False
                        lose4a = True
                        f_sc_a()
            elif event.type == pygame.MOUSEBUTTONDOWN and anime_q5:
                if event.button == 1:
                    tap = pygame.Rect(x, y, 1, 1)
                    if tap.colliderect(blue_lock_rect):
                        score += 10
                        winner_a = True
                        f_sc_a()
                    elif tap.colliderect(bk_rect):
                        anime_q5 = False
                        lose5a = True
                        f_sc_k()
                    elif tap.colliderect(opm_rect):
                        anime_q5 = False
                        lose5a = True
                        f_sc_a()
                    elif tap.colliderect(akame_rect):
                        anime_q5 = False
                        lose5a = True
                        f_sc_a()

        if main_screen:
            sc.blit(bg, (0, 0))
            sc.blit(text, (350, 70))
            sc.blit(kpop, kpop_rect)
            sc.blit(anime, anime_rect)
        #
        # if kpop_screen:
        #     sc.blit(bg, (0, 0))
        #     kpop_q1 = True

        # if anime_screen:
        #     sc.blit(bg, (0, 0))
        #     anime_q1 = True

        if lose1k:
            f_sc_k()
            sc.blit(sc0, (350, 70))

        if lose2k:
            f_sc_k()
            sc.blit(sc10, (350, 70))

        if lose3k:
            f_sc_k()
            sc.blit(sc20, (350, 70))

        if lose4k:
            f_sc_k()
            sc.blit(sc30, (350, 70))

        if lose5k:
            f_sc_k()
            sc.blit(sc40, (350, 70))

        if lose1a:
            f_sc_a()
            sc.blit(sc0, (350, 70))

        if lose2a:
            f_sc_a()
            sc.blit(sc10, (350, 70))

        if lose3a:
            f_sc_a()
            sc.blit(sc20, (350, 70))

        if lose4a:
            f_sc_a()
            sc.blit(sc30, (350, 70))

        if lose5a:
            f_sc_a()
            sc.blit(sc40, (350, 70))


        if kpop_q1:
            kpop_q1_f()

        if kpop_q2:
            kpop_q2_f()

        if kpop_q3:
            kpop_q3_f()

        if kpop_q4:
            kpop_q4_f()

        if kpop_q5:
            kpop_q5_f()

        if anime_q1:
            anime_q1_f()

        if anime_q2:
            anime_q2_f()

        if anime_q3:
            anime_q3_f()

        if anime_q4:
            anime_q4_f()

        if anime_q5:
            anime_q5_f()

        if winner_k:
            f_sc_k()
            sc.blit(win, (350, 70))

        if winner_a:
            f_sc_a()
            sc.blit(win, (350, 70))

        sc.blit(kursor, (x, y))

        clock.tick(FPS)
        pygame.display.update()


main()