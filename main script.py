import pygame as pg 
import time
import random
from player_script import *
from background import *
from interact_script import *

global vie
vie = 6
global take
global take_k
global tomato
global buche
global jeton_v
jeton_v = 2

pg.init()

def bomb_game_over():
    window = pg.display.set_mode((1020, 820))
    
    n = 0
    
    running = True
    
    pg.display.set_caption("DON'T CHEAT!!!")
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        
        n += 1
        if n == 2000:
            pg.QUIT()
        
        with open('saves/saves.txt', 'w') as data:
            data.write('level3')
        
        font = pg.font.SysFont('Operator', 100)
        text_f = font.render("Game Over", False, (255, 0, 0))
        window.blit(text_f, (325, 355))
        text_f = font.render("DON'T CHEAT!!", False, (255, 0, 0))
        window.blit(text_f, (250, 425))
        
        pg.display.flip()

def end():
    window = pg.display.set_mode((1020, 820))
    
    Clock = pg.time.Clock()
    
    running = True
    
    caracter = ["Thank To playing IT !!", "Credits Enigmatic Game", "Productor:", "Cyril Houppertz", "Graphic Design:", "take on Internet Open Source Asset", "Game Design & Script:", "Cyril Houppertz", "Enigme Maker:", "Cyril Houppertz", "Game Tester:", "Prudence", "Cyril Houppertz", "My Family", "Game Programmer:", "Cyril Houppertz", "Prgammation Language Used:", "Python", "Special Remerciement:", "Prudence", "Kramozo", "Ever alias Xarever", "CoraTlie", "Parzival", "Colonoc", "A Game from", "Whixon", "Enigmatic Game"]
    coordinate = [820,                             1220,                1620,           1680,              1780,                         1840,                         1940,                  2000,            2100,            2160,              2260,         2320,           2380,          2440,            2540,              2600,                 2700,                   2760,           2860,                2920,      2980,         3040,               3100,       3160,      3220,       4080,       4180,          5040]
    
    pg.display.set_caption('enigmatic game End')
    
    while running:
        window.blit(background4, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        
        for i in range(len(coordinate)):
            if coordinate[i-1] < -30:
                pass
            elif caracter[i-1] == "Enigmatic Game" and coordinate[i-1] < 175:
                with open('saves/saves.txt', 'w') as data:
                    data.write('')
                pg.quit()
            else:
                coordinate[i-1] = coordinate[i-1] - 2
        
        for i in range(len(caracter)):
            if coordinate[i-1] < -30 or coordinate[i-1] > 820:
                pass
            elif caracter[i-1] == "Enigmatic Game":
                font = pg.font.SysFont('Operator', 50)
                text_f = font.render(caracter[i-1], False, (255, 255, 255))
                window.blit(text_f, (375, coordinate[i-1]))
            else:
                font = pg.font.SysFont('Operator', 50)
                text_f = font.render(caracter[i-1], False, (255, 255, 255))
                window.blit(text_f, (2, coordinate[i-1]))
            
        
        Clock.tick(60)
        pg.display.flip()

def game_over():
    window = pg.display.set_mode((1020, 820))
    
    running = True
    
    pg.display.set_caption('enigmatic game game over')
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        
        font = pg.font.SysFont('Operator', 100)
        text_f = font.render("Game Over", False, (255, 0, 0))
        window.blit(text_f, (325, 355))
        
        pg.display.flip()

def main_menu():

    main_window = pg.display.set_mode((1020, 820))
    
    running = True
    
    pg.display.set_caption('enigmatic game main menu')
    
    while running:
        main_window.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        
        pressed = pg.key.get_pressed()
        if pressed[pg.K_SPACE]:
            level1()
            main_window.quit()
        
        font = pg.font.SysFont('Arial', 30)
        text_f = font.render("Press [space] for start the game", True, (0, 0, 0))
        
        main_window.blit(text_f, (355, 450))
        
        main_window.blit(front1, (503, 400))
        
        pg.display.flip()
    
#--------------------------------------------------------------------------------------------------level 1---------------------------------------------------------------------------

def level1():
    global take
    global vie

    window = pg.display.set_mode((1020, 820))

    pg.display.set_caption('enigmatic game')

    #on stock les trois états possibles des coeurs avant de les affichers
    f_heart = pg.image.load('health/full heart.png')
    m_heart = pg.image.load('health/mid heart.png')
    e_heart = pg.image.load('health/empty heart.png')
    jeton = pg.image.load('environement/interact/jetons.png')

    state = "right"
    achat = 0
    
    nuc_x, nuc_y = 500, -82
    
    vitesse = 7
    papotte = 'parler'
    jeton_v = 2

    player_rect.x = 765
    player_rect.y = 775

    #on definit dans des variable l'état de l'animation
    l_n = 1
    r_n = 1
    b_n = 1
    f_n = 1
    
    nuclear_state = False
    
    Clock = pg.time.Clock()

    pg.display.flip()

    running = True

    #on crée la boucle du jeux
    while running:
        pressed = pg.key.get_pressed()
        window.blit(background, (0, 0))
        window.blit(chatbox, (362, 768))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        window.blit(jeton, (0, 50))
        font = pg.font.SysFont('arial', 32)
        text_f = font.render(f": {jeton_v}/3", False, (0, 0, 0))
        window.blit(text_f, (35, 47))

        if player_rect.y < 743 and player_rect.y > 652:
            if player_rect.x > 709 and player_rect.x < 793:
                vitesse = 3
        elif player_rect.y < 673 and player_rect.y > 652:
            if player_rect.x > 366 and player_rect.x < 415:
                vitesse = 3
        elif player_rect.y < 568 and player_rect.y > 456:
            if player_rect.x > 219 and player_rect.x < 282:
                vitesse = 3
        elif player_rect.y < 351 and player_rect.y > 281:
            if player_rect.x > 632 and player_rect.x < 716:
                vitesse = 3
        elif player_rect.y < 239 and player_rect.y > 218:
            if player_rect.x > 681 and player_rect.x < 737:
                vitesse = 3
        elif player_rect.y < 197 and player_rect.y > 148:
            if player_rect.x > 492 and player_rect.x < 555:
                vitesse = 3
        elif player_rect.y < 64 and player_rect.y > 40:
            if player_rect.x > 492 and player_rect.x < 555:
                vitesse = 3
        else:
            vitesse = 7
        
        nuclear_count = 0
        for i in take:
            if i == "rock take" or i == "rock2 take":
                nuclear_count += 1
        
        if nuclear_count > 1:
            nuclear_state = True
        
        if nuclear_state == True:
            window.blit(nuclear_bomb, (nuc_x, nuc_y))
            nuc_y += 10
            if nuc_y > 450:
                pg.QUIT
                bomb_game_over()
        
        #on affiche la borne d'achat
        if achat == 0:
            window.blit(borne_d, (borne_d_rect.x, borne_d_rect.y))
        else:
            borne_d_rect.x, borne_d_rect.y = 0, 0

        #on propose d'acheter un indice en échange d'un demi vie
        if papotte == 'achat indice':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("it will cost you 1 jeton", False, (0, 0, 0))
            window.blit(text_f, (373, 770))
            text_f = font.render("Do you accept? [o]/[n]", False, (0, 0, 0))
            window.blit(text_f, (373, 787))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_o]:
                papotte = 'indice récup'
                jeton_v -= 1
                achat += 1


        #on voit s'il est a proximiter de la borne si oui on propose de lui parler
        if player_rect.colliderect(borne_d_rect) and papotte == 'parler':
            if 'rock not take' in take and 'rock2 not take' in take:
                font = pg.font.SysFont('arial', 25)
                text_f = font.render("talk to darkadess [space]", False, (0, 0, 0))
                window.blit(text_f, (370, 774))
                if pressed[pg.K_SPACE]:
                    papotte = 'papotte'

        if papotte == 'papotte':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("Hi friend,",  False, (0, 0, 0))
            window.blit(text_f, (373, 770))
            text_f = font.render("do you want to pay a hint? [y]/[n]", False, (0, 0, 0))
            window.blit(text_f, (373, 785))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_y]:
                papotte = 'achat indice'

        #on verifie si un des caillou est sur le boutton, si non on affiche le boutton en état lever, si oui on affiche le boutton en état descendu
        if button1_rect.colliderect(rock1_rect) or button1_rect.colliderect(rock2_rect) or button1_rect.colliderect(player_rect):
            window.blit(button1_d, (button1_rect.x, button1_rect.y))
        else:
            window.blit(button1_p, (button1_rect.x, button1_rect.y))
        
        #on verifie si un des caillou est sur le deuxième boutton, si non on affiche le deuxième boutton en état lever, si oui on affiche le deuxième boutton en état descendu
        if button2_rect.colliderect(rock1_rect) or button2_rect.colliderect(rock2_rect) or button2_rect.colliderect(player_rect):
            window.blit(button2_d, (button2_rect.x, button2_rect.y))
        else:
            window.blit(button2_p, (button2_rect.x, button2_rect.y))
        
        #on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            if b_n == 2 or b_n == 4:
                window.blit(back1, (player_rect.x, player_rect.y))
            if b_n == 1:
                window.blit(back2, (player_rect.x, player_rect.y))
            if b_n == 3:
                window.blit(back3, (player_rect.x, player_rect.y))
                b_n = 0
            player_rect.y -= vitesse
            if hitbox1_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y += vitesse
            if player_rect.y < 37:
                if not button2_rect.colliderect(rock1_rect) or button2_rect.colliderect(rock2_rect) or button2_rect.colliderect(player_rect):
                    if not button1_rect.colliderect(rock1_rect) or button1_rect.colliderect(rock2_rect) or button1_rect.colliderect(player_rect):
                        player_rect.y += vitesse
            b_n += 1
            
        elif pressed[pg.K_LEFT]:
            state = "left"
            if l_n == 2 or l_n == 4:
                window.blit(left1, (player_rect.x, player_rect.y))
            if l_n == 1:
                window.blit(left2, (player_rect.x, player_rect.y))
            if l_n == 3:
                window.blit(left3, (player_rect.x, player_rect.y))
                l_n = 0
            player_rect.x -= vitesse
            if hitbox1_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x += vitesse
            l_n += 1

        elif pressed[pg.K_DOWN]:
            state = "front"
            if f_n == 2 or f_n == 4:
                window.blit(front1, (player_rect.x, player_rect.y))
            if f_n == 1:
                window.blit(front2, (player_rect.x, player_rect.y))
            if f_n == 3:
                window.blit(front3, (player_rect.x, player_rect.y))
                f_n = 0
            player_rect.y += vitesse
            if hitbox1_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y -= vitesse
            f_n += 1

        elif pressed[pg.K_RIGHT]:
            state = "right"
            if r_n == 2 or r_n == 4:
                window.blit(right1, (player_rect.x, player_rect.y))
            if r_n == 1:
                window.blit(right2, (player_rect.x, player_rect.y))
            if r_n == 3:
                window.blit(right3, (player_rect.x, player_rect.y))
                r_n = 0
            player_rect.x += vitesse
            if hitbox1_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x -= vitesse
            r_n += 1
        
        else:
            if state == "back":
                window.blit(back1, (player_rect.x, player_rect.y))
            if state == "right":
                window.blit(right1, (player_rect.x, player_rect.y))
            if state == "left":
                window.blit(left1, (player_rect.x, player_rect.y))
            if state == "front":
                window.blit(front1, (player_rect.x, player_rect.y))
        
        #on verifie si le cailloux a été pris, si oui alors on affiche la possibiliter de le lacher
        #et si la touche [e] est presser alors on l'affiche a la position du joueur, si non alors on affiche le cailloux
        #a sont endroit specifique
        if 'rock not take' in take:
            window.blit(rock, (rock1_rect.x, rock1_rect.y))
        else:
            rock1_rect.x, rock1_rect.y = 0, 0
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("drop the rock > [f]", False, (0, 0, 0))
            window.blit(text_f, (382, 790))
            if pressed[pg.K_f]:
                take.remove('rock take')
                take.insert(0, 'rock not take')
                rock1_rect.x, rock1_rect.y = (player_rect.x + 7), (player_rect.y + 27)
        
        #on verifie si le joueur ce tiens a portée du caillou et on verifie si il n'a pas deja été pris, si non alors on
        #affiche la possibilité de le prendre avec un text label, si la touche [e] est presser alors on enleve le cailloux
        #et on mets sa boite de colision en haut a gauche pour pas gêner le joueur
        if player_rect.colliderect(rock1_rect) and 'rock not take' in take:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the rock > [e]", False, (0, 0, 0))
            window.blit(text_f, (382, 790))
            if pressed[pg.K_e]:
                take.remove('rock not take')
                take.insert(0, 'rock take')
                
        #on verifie si le deuxième cailloux a été pris, si oui alors on affiche la possibiliter de le lacher
        #et si la touche [e] est presser alors on l'affiche a la position du joueur, si non alors on affiche le cailloux
        #a sont endroit specifique
        if 'rock2 not take' in take:
            window.blit(rock2, (rock2_rect.x, rock2_rect.y))
        else:
            rock2_rect.x, rock2_rect.y = 0, 0
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("drop the rock > [f]", False, (0, 0, 0))
            window.blit(text_f, (382, 770))
            if pressed[pg.K_g]:
                take.remove('rock2 take')
                take.insert(0, 'rock2 not take')
                rock2_rect.x, rock2_rect.y = (player_rect.x + 7), (player_rect.y + 27)
        
        #on verifie si le joueur ce tiens a portée du deuxième caillou et on verifie si il n'a pas deja été pris, si non alors on
        #affiche la possibilité de le prendre avec un text label, si la touche [e] est presser alors on enleve le deuxième cailloux
        #et on mets sa boite de colision en haut a gauche pour pas gêner le joueur
        if player_rect.colliderect(rock2_rect) and 'rock2 not take' in take:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the rock > [e]", False, (0, 0, 0))
            window.blit(text_f, (382, 770))
            if pressed[pg.K_r]:
                take.remove('rock2 not take')
                take.insert(0, 'rock2 take')
        
        if button2_rect.colliderect(rock1_rect) or button2_rect.colliderect(rock2_rect) or button2_rect.colliderect(player_rect):
            if button1_rect.colliderect(rock1_rect) or button1_rect.colliderect(rock2_rect) or button1_rect.colliderect(player_rect):
                if player_rect.y < 37:
                    with open('saves/saves.txt', 'a') as data:
                        data.write('level1\n')
                    level2()
                    return vie and jeton_v

            else:
                window.blit(porte2, (500, -30))
        else:
            window.blit(porte2, (500, -30))


        # on affiche les trois coeurs et leurs états grave a une condition avec la variable vie
        if vie == 6:
            window.blit(f_heart, (125, 7))
            window.blit(f_heart, (155, 7))
            window.blit(f_heart, (185, 7))
        if vie == 5:
            window.blit(f_heart, (125, 7))
            window.blit(f_heart, (155, 7))
            window.blit(m_heart, (185, 7))
        if vie == 4:
            window.blit(f_heart, (125, 7))
            window.blit(f_heart, (155, 7))
            window.blit(e_heart, (185, 7))
        if vie == 3:
            window.blit(f_heart, (125, 7))
            window.blit(m_heart, (155, 7))
            window.blit(e_heart, (185, 7))
        if vie == 2:
            window.blit(f_heart, (125, 7))
            window.blit(e_heart, (155, 7))
            window.blit(e_heart, (185, 7))
        if vie == 1:
            window.blit(m_heart, (125, 7))
            window.blit(e_heart, (155, 7))
            window.blit(e_heart, (185, 7))
        if vie == 0:
            window.blit(e_heart, (125, 7))
            window.blit(e_heart, (155, 7))
            window.blit(e_heart, (185, 7))

        if papotte == 'indice récup':
            window.blit(chatindice, (0, 145))
            font = pg.font.SysFont('Operator', 40)
            text_f = font.render("hint:", False, (0, 0, 0))
            window.blit(text_f, (4, 150))
            font = pg.font.SysFont('Arial', 25)
            text_f = font.render("you can take", False, (0, 0, 0))
            window.blit(text_f, (4, 180))
            text_f = font.render("the rocks", False, (0, 0, 0))
            window.blit(text_f, (4, 200))
            text_f = font.render("to put them", False, (0, 0, 0))
            window.blit(text_f, (4, 220))
            text_f = font.render("elsewhere", False, (0, 0, 0))
            window.blit(text_f, (4, 240))

        #on definit et on affiche le text HEALTH a l'écran
        font = pg.font.SysFont('Operator', 55)
        text_f = font.render("health:", False, (0, 0, 0))
        window.blit(text_f, (0, 0))
        
        #on rafraichit et on definit les fps avec la variable clock qui stock l'instant pg.clock 
        Clock.tick(10)
        pg.display.flip()

#--------------------------------------------------------------------------------------------------level 2---------------------------------------------------------------------------

def level2():
    global take_k
    global vie
    global jeton_v

    level_2 = pg.display.set_mode((1025, 825))

    pg.display.set_caption('enigmatic game level2')

    # on stock les trois états possibles des coeurs avant de les affichers
    f_heart = pg.image.load('health/full heart.png')
    m_heart = pg.image.load('health/mid heart.png')
    e_heart = pg.image.load('health/empty heart.png')
    jeton = pg.image.load('environement/interact/jetons.png')

    state = "right"
    achat = 0

    borne_d_rect.x, borne_d_rect.y = 720, 760

    vitesse = 7

    papotte = 'parler'

    jeton_act = True

    player_rect.x, player_rect.y = 765, 785

    jeton_int_rect.x, jeton_int_rect.y = 230, 335

    clign = 0

    # on definit dans des variable l'état de l'animation
    l_n = 1
    r_n = 1
    b_n = 1
    f_n = 1

    Clock = pg.time.Clock()

    pg.display.flip()

    running = True

    # on crée la boucle du jeux
    while running:
        pressed = pg.key.get_pressed()
        level_2.blit(background2, (0, 0))
        level_2.blit(chatbox, (362, 768))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        level_2.blit(jeton, (0, 50))
        font = pg.font.SysFont('arial', 32)
        text_f = font.render(f": {jeton_v}/3", False, (0, 0, 0))
        level_2.blit(text_f, (35, 47))

        if player_rect.colliderect(jeton_int_rect):
            jeton_v += 1
            jeton_act = False

        if jeton_act:
            level_2.blit(jeton_int, (jeton_int_rect.x, jeton_int_rect.y))
        else:
            jeton_int_rect.x, jeton_int_rect.y = 0, 0

        # on affiche la borne d'achat
        if achat == 0:
            level_2.blit(borne_d, (borne_d_rect.x, borne_d_rect.y))
        else:
            borne_d_rect.x, borne_d_rect.y = 0, 0

        if 'key give' in take_k and 'key2 give' in take_k:
            porte_rect.x, porte_rect.y = 0, 0
            porteh_rect.x, porteh_rect.y = 0, 0
        else:
            level_2.blit(porte, (porte_rect.x, porte_rect.y))

        # on propose d'acheter un indice en échange d'un demi vie
        if papotte == 'achat indice':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("it will cost you 1 jeton", False, (0, 0, 0))
            level_2.blit(text_f, (373, 770))
            text_f = font.render("do you accept? [o]/[n]", False, (0, 0, 0))
            level_2.blit(text_f, (373, 787))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_o]:
                papotte = 'indice récup'
                jeton_v -= 1
                achat += 1

        # on voit s'il est a proximiter de la borne si oui on propose de lui parler
        if player_rect.colliderect(borne_d_rect) and papotte == 'parler':
            if 'key take' in take_k or 'key2 take' in take_k:
                pass
            else:
                font = pg.font.SysFont('arial', 25)
                text_f = font.render("talk to Darkadesse [space]", False, (0, 0, 0))
                level_2.blit(text_f, (370, 774))
                if pressed[pg.K_SPACE]:
                    papotte = 'papotte'

        if papotte == 'papotte':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("hi friend,", False, (0, 0, 0))
            level_2.blit(text_f, (373, 770))
            text_f = font.render("do you want to pay a hint? [y]/[n]", False, (0, 0, 0))
            level_2.blit(text_f, (373, 785))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_y]:
                papotte = 'achat indice'

        # on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            if b_n == 2 or b_n == 4:
                level_2.blit(back1, (player_rect.x, player_rect.y))
            if b_n == 1:
                level_2.blit(back2, (player_rect.x, player_rect.y))
            if b_n == 3:
                level_2.blit(back3, (player_rect.x, player_rect.y))
                b_n = 0
            player_rect.y -= vitesse
            if hitbox2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y += vitesse

            if porteh_rect.colliderect(player_rect):
                player_rect.y += vitesse
            b_n += 1

        elif pressed[pg.K_LEFT]:
            state = "left"
            if l_n == 2 or l_n == 4:
                level_2.blit(left1, (player_rect.x, player_rect.y))
            if l_n == 1:
                level_2.blit(left2, (player_rect.x, player_rect.y))
            if l_n == 3:
                level_2.blit(left3, (player_rect.x, player_rect.y))
                l_n = 0
            player_rect.x -= vitesse
            if hitbox2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x += vitesse
            l_n += 1

        elif pressed[pg.K_DOWN]:
            state = "front"
            if f_n == 2 or f_n == 4:
                level_2.blit(front1, (player_rect.x, player_rect.y))
            if f_n == 1:
                level_2.blit(front2, (player_rect.x, player_rect.y))
            if f_n == 3:
                level_2.blit(front3, (player_rect.x, player_rect.y))
                f_n = 0
            player_rect.y += vitesse
            if hitbox2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y -= vitesse
            f_n += 1

        elif pressed[pg.K_RIGHT]:
            state = "right"
            if r_n == 2 or r_n == 4:
                level_2.blit(right1, (player_rect.x, player_rect.y))
            if r_n == 1:
                level_2.blit(right2, (player_rect.x, player_rect.y))
            if r_n == 3:
                level_2.blit(right3, (player_rect.x, player_rect.y))
                r_n = 0
            player_rect.x += vitesse
            if hitbox2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x -= vitesse
            r_n += 1

        else:
            if state == "back":
                level_2.blit(back1, (player_rect.x, player_rect.y))
            if state == "right":
                level_2.blit(right1, (player_rect.x, player_rect.y))
            if state == "left":
                level_2.blit(left1, (player_rect.x, player_rect.y))
            if state == "front":
                level_2.blit(front1, (player_rect.x, player_rect.y))

        # on verifie si la clé a été pris, si oui alors on affiche la possibiliter de le lacher
        # et si la touche [e] est presser alors on l'affiche a la position du joueur, si non alors on affiche le cailloux
        # a sont endroit specifique
        if 'key not take' in take_k:
            level_2.blit(key, (key_rect.x, key_rect.y))
        else:
            key_rect.x, key_rect.y = 0, 0

        if player_rect.colliderect(porte_rect) and 'key take' in take_k:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("insert the key > [f]", False, (0, 0, 0))
            level_2.blit(text_f, (382, 790))
            if pressed[pg.K_f]:
                take_k.remove('key take')
                take_k.insert(0, 'key give')

        # on verifie si le joueur ce tiens a portée de la clé et on verifie si il n'a pas deja été pris, si non alors on
        # affiche la possibilité de le prendre avec un text label, si la touche [e] est presser alors on enleve le cailloux
        # et on mets sa boite de colision en haut a gauche pour pas gêner le joueur
        if player_rect.colliderect(key_rect) and 'key not take' in take_k:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the key > [e]", False, (0, 0, 0))
            level_2.blit(text_f, (382, 790))
            if pressed[pg.K_e]:
                take_k.remove('key not take')
                take_k.insert(0, 'key take')

        # on verifie si la deuxième clé a été pris, si oui alors on affiche la possibiliter de le lacher
        # et si la touche [e] est presser alors on l'affiche a la position du joueur, si non alors on affiche le cailloux
        # a sont endroit specifique

        if 'key give' in take_k and 'key2 not take' in take_k:
            key2_rect.x, key2_rect.y = 140, 465
            level_2.blit(key2, (key2_rect.x, key2_rect.y))

        if player_rect.colliderect(porte_rect) and 'key2 take' in take_k:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("insert the key > [g]", False, (0, 0, 0))
            level_2.blit(text_f, (382, 790))
            if pressed[pg.K_g]:
                take_k.remove('key2 take')
                take_k.insert(0, 'key2 give')

        # on verifie si le joueur ce tiens a portée de la deuxième clé et on verifie si il n'a pas deja été pris, si non alors on
        # affiche la possibilité de le prendre avec un text label, si la touche [e] est presser alors on enleve le cailloux
        # et on mets sa boite de colision en haut a gauche pour pas gêner le joueur
        if player_rect.colliderect(key2_rect) and 'key2 not take' in take_k:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the key > [r]", False, (0, 0, 0))
            level_2.blit(text_f, (382, 790))
            if pressed[pg.K_r]:
                take_k.remove('key2 not take')
                take_k.insert(0, 'key2 take')

        # on affiche les trois coeurs et leurs états grave a une condition avec la variable vie
        level_2.blit(f_heart, (125, 7))
        level_2.blit(f_heart, (155, 7))
        level_2.blit(f_heart, (185, 7))
        if vie == 5:
            level_2.blit(f_heart, (125, 7))
            level_2.blit(f_heart, (155, 7))
            level_2.blit(m_heart, (185, 7))
        if vie == 4:
            level_2.blit(f_heart, (125, 7))
            level_2.blit(f_heart, (155, 7))
            level_2.blit(e_heart, (185, 7))
        if vie == 3:
            level_2.blit(f_heart, (125, 7))
            level_2.blit(m_heart, (155, 7))
            level_2.blit(e_heart, (185, 7))
        if vie == 2:
            level_2.blit(f_heart, (125, 7))
            level_2.blit(e_heart, (155, 7))
            level_2.blit(e_heart, (185, 7))
        if vie == 1:
            level_2.blit(m_heart, (125, 7))
            level_2.blit(e_heart, (155, 7))
            level_2.blit(e_heart, (185, 7))
        if vie == 0:
            level_2.blit(e_heart, (125, 7))
            level_2.blit(e_heart, (155, 7))
            level_2.blit(e_heart, (185, 7))

        if papotte == 'indice récup':
            level_2.blit(chatindice, (0, 670))
            font = pg.font.SysFont('Operator', 40)
            text_f = font.render("hint:", False, (0, 0, 0))
            level_2.blit(text_f, (4, 680))
            font = pg.font.SysFont('Arial', 25)
            text_f = font.render("I think", False, (0, 0, 0))
            level_2.blit(text_f, (4, 700))
            text_f = font.render("in the", False, (0, 0, 0))
            level_2.blit(text_f, (4, 720))
            text_f = font.render("bug zone there", False, (0, 0, 0))
            level_2.blit(text_f, (4, 740))
            text_f = font.render("is a key", False, (0, 0, 0))
            level_2.blit(text_f, (4, 760))

        if player_rect.y < 0:
            with open('saves/saves.txt', 'a') as data:
                data.write('level2')
            level3()
            return vie and jeton_v

        if clign == 15:
            clign = 0

        elif clign > -1:
            level_2.blit(cache, (17, 202))
            clign +=1

        # on definit et on affiche le text HEALTH a l'écran
        font = pg.font.SysFont('Operator', 55)
        text_f = font.render("health:", False, (0, 0, 0))
        level_2.blit(text_f, (0, 0))

        Clock.tick(10)
        pg.display.flip()

#--------------------------------------------------------------------------------------------------level 3---------------------------------------------------------------------------

def level3():
    global vie
    global jeton_v

    level_3 = pg.display.set_mode((1025, 825))

    pg.display.set_caption('enigmatic game level3')

    # on stock les trois états possibles des coeurs avant de les affichers
    f_heart = pg.image.load('health/full heart.png')
    m_heart = pg.image.load('health/mid heart.png')
    e_heart = pg.image.load('health/empty heart.png')
    jeton = pg.image.load('environement/interact/jetons.png')

    state = "right"
    achat = 0

    borne_d_rect.x, borne_d_rect.y = 455, 760

    vitesse = 7

    tomato = 0

    buche = 0
    papotte = 'parler'

    jean_pierre_talk = 'parler'

    player_rect.x, player_rect.y = 500, 785

    state_bridge = False

    # on definit dans des variable l'état de l'animation
    l_n = 1
    r_n = 1
    b_n = 1
    f_n = 1

    Clock = pg.time.Clock()

    pg.display.flip()

    running = True

    # on crée la boucle du jeux
    while running:
        mask_front1_rect.x, mask_front1_rect.y = player_rect.x, player_rect.y
        pressed = pg.key.get_pressed()
        level_3.blit(background3, (0, 0))
        level_3.blit(drop_zone, (drop_zone_rect.x, drop_zone_rect.y))
        level_3.blit(jean_pierre, (jean_pierre_rect.x, jean_pierre_rect.y))
        level_3.blit(baque2_remplit, (baque2_remplit_rect.x, baque2_remplit_rect.y))
        level_3.blit(baque1_remplit, (baque1_remplit_rect.x, baque1_remplit_rect.y))
        level_3.blit(chatbox, (125, 768))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        level_3.blit(jeton, (0, 50))
        font = pg.font.SysFont('arial', 32)
        text_f = font.render(f": {jeton_v}/3", False, (255, 255, 255))
        level_3.blit(text_f, (35, 47))

        # on affiche la borne d'achat
        if achat == 0:
            level_3.blit(borne_d, (borne_d_rect.x, borne_d_rect.y))
        else:
            borne_d_rect.x, borne_d_rect.y = 0, 0

        if papotte == 'achat indice':
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("it will cost you 1 jeton", False, (0, 0, 0))
            level_3.blit(text_f, (133, 770))
            text_f = font.render("do you accept? [o]/[n]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_o]:
                papotte = 'indice récup'
                jeton_v -= 1
                achat += 1

        # on voit s'il est a proximiter de la borne si oui on propose de lui parler
        if player_rect.colliderect(borne_d_rect) and papotte == 'parler':
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("talk to Darkadesse [Espace]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_SPACE]:
                papotte = 'papotte'

        if papotte == 'papotte':
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("Hi friend, do you ", False, (0, 0, 0))
            level_3.blit(text_f, (133, 770))
            text_f = font.render("want to pay a hint? [y]/[n]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_y]:
                papotte = 'achat indice'
        
        if papotte == "indice récup":
            level_3.blit(chatindice, (300, 10))
            font = pg.font.SysFont('arial', 25)
            text_f = font.render("Hint:", False, (0, 0, 0))
            level_3.blit(text_f, (305, 12))
            
            font = pg.font.SysFont('arial', 21)
            text_f = font.render("I think this man", False, (0, 0, 0))
            level_3.blit(text_f, (305, 62))
            
            text_f = font.render("need some help", False, (0, 0, 0))
            level_3.blit(text_f, (305, 87))
            

        if player_rect.colliderect(jean_pierre_rect) and jean_pierre_talk == 'aide accept':
            if baque1_remplit_rect.colliderect(drop_zone_rect) and baque2_remplit_rect.colliderect(drop_zone_rect):
                font = pg.font.SysFont('arial', 20)
                text_f = font.render("reclaim the reward", False, (0, 0, 0))
                level_3.blit(text_f, (133, 770))
                text_f = font.render("[space]", False, (0, 0, 0))
                level_3.blit(text_f, (133, 790))
                if pressed[pg.K_SPACE]:
                    jean_pierre_talk = "done"
                    buche = 4

        if player_rect.colliderect(jean_pierre_rect) and jean_pierre_talk == 'aide':
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("Can you push the tomatos baque", False, (0, 0, 0))
            level_3.blit(text_f, (133, 770))
            text_f = font.render("into the zone here please? [o]/[n]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                jean_pierre_talk = "parler"
            elif pressed[pg.K_o]:
                jean_pierre_talk = "aide accept"

        if player_rect.colliderect(jean_pierre_rect) and jean_pierre_talk == 'parler':
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("talk to Jean Pierre [Espace]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 775))
            if pressed[pg.K_SPACE]:
                jean_pierre_talk = 'papotte'

        if jean_pierre_talk == 'papotte':
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("Hy friend, Can you ", False, (0, 0, 0))
            level_3.blit(text_f, (133, 770))
            text_f = font.render("help me for something? [y]/[n]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                jean_pierre_talk = 'parler'
            elif pressed[pg.K_y]:
                jean_pierre_talk= 'aide'

        if state_bridge == False:
            level_3.blit(broken_bridge, (broken_bridge_rect.x, broken_bridge_rect.y))
        elif state_bridge == True:
            level_3.blit(bridge, (bridge_rect.x, bridge_rect.y))

        if player_rect.colliderect(broken_bridge_rect):
            if buche == 4:
                state_bridge = True
            else:
                font = pg.font.SysFont('arial', 20)
                text_f = font.render("the bridge is broken", False, (0, 0, 0))
                level_3.blit(text_f, (133, 770))
                text_f = font.render(f"{buche}/4 planks", False, (0, 0, 0))
                level_3.blit(text_f, (133, 790))


        # on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            if b_n == 2 or b_n == 4:
                level_3.blit(back1, (player_rect.x, player_rect.y))
            if b_n == 1:
                level_3.blit(back2, (player_rect.x, player_rect.y))
            if b_n == 3:
                level_3.blit(back3, (player_rect.x, player_rect.y))
                b_n = 0

            player_rect.y -= vitesse
            if mask_front1_rect.y == 330 and state_bridge == False:
                player_rect.y += vitesse
            if player_rect.colliderect(baque1_remplit_rect) and tomato == 0:
                baque1_remplit_rect.y -= vitesse

                if hitbox3_mask.overlap(baque1_mask, (baque1_remplit_rect.x, baque1_remplit_rect.y)):
                    baque1_remplit_rect.y += vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.y += vitesse

                if baque1_remplit_rect.colliderect(baque2_remplit_rect):
                    baque1_remplit_rect.y += vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.y += vitesse

            elif player_rect.colliderect(baque2_remplit_rect) and tomato == 0:
                baque2_remplit_rect.y -= vitesse

                if hitbox3_mask.overlap(baque2_mask, (baque2_remplit_rect.x, baque2_remplit_rect.y)):
                    baque2_remplit_rect.y += vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.y += vitesse

                if baque2_remplit_rect.colliderect(baque1_remplit_rect):
                    baque2_remplit_rect.y += vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.y += vitesse

            else:
                if hitbox3_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                    player_rect.y += vitesse
            b_n += 1

        elif pressed[pg.K_LEFT]:
            state = "left"
            if l_n == 2 or l_n == 4:
                level_3.blit(left1, (player_rect.x, player_rect.y))
            if l_n == 1:
                level_3.blit(left2, (player_rect.x, player_rect.y))
            if l_n == 3:
                level_3.blit(left3, (player_rect.x, player_rect.y))
                l_n = 0

            player_rect.x -= vitesse
            if player_rect.colliderect(baque1_remplit_rect) and tomato == 0:
                baque1_remplit_rect.x -= vitesse

                if hitbox3_mask.overlap(baque1_mask, (baque1_remplit_rect.x, baque1_remplit_rect.y)):
                    baque1_remplit_rect.x += vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.x += vitesse

                if baque1_remplit_rect.colliderect(baque2_remplit_rect):
                    baque1_remplit_rect.x += vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.x += vitesse

            elif player_rect.colliderect(baque2_remplit_rect) and tomato == 0:
                baque2_remplit_rect.x -= vitesse

                if hitbox3_mask.overlap(baque2_mask, (baque2_remplit_rect.x, baque2_remplit_rect.y)):
                    baque2_remplit_rect.x += vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.x += vitesse

                if baque2_remplit_rect.colliderect(baque1_remplit_rect):
                    baque2_remplit_rect.x += vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.x += vitesse

            else:
                if hitbox3_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                    player_rect.x += vitesse
            l_n += 1

        elif pressed[pg.K_DOWN]:
            state = "front"
            if f_n == 2 or f_n == 4:
                level_3.blit(front1, (player_rect.x, player_rect.y))
            elif f_n == 1:
                level_3.blit(front2, (player_rect.x, player_rect.y))
            elif f_n == 3:
                level_3.blit(front3, (player_rect.x, player_rect.y))
                f_n = 0

            player_rect.y += vitesse
            if player_rect.colliderect(baque1_remplit_rect) and tomato == 0:
                baque1_remplit_rect.y += vitesse

                if hitbox3_mask.overlap(baque1_mask, (baque1_remplit_rect.x, baque1_remplit_rect.y)):
                    baque1_remplit_rect.y -= vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.y -= vitesse

                if baque1_remplit_rect.colliderect(baque2_remplit_rect):
                    baque1_remplit_rect.y -= vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.y -= vitesse

            elif player_rect.colliderect(baque2_remplit_rect) and tomato == 0:
                baque2_remplit_rect.y += vitesse

                if hitbox3_mask.overlap(baque2_mask, (baque2_remplit_rect.x, baque2_remplit_rect.y)):
                    baque2_remplit_rect.y -= vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.y -= vitesse

                if baque2_remplit_rect.colliderect(baque1_remplit_rect):
                    baque2_remplit_rect.y -= vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.y -= vitesse

            else:
                if hitbox3_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                    player_rect.y -= vitesse
            f_n += 1

        elif pressed[pg.K_RIGHT]:
            state = "right"
            if r_n == 2 or r_n == 4:
                level_3.blit(right1, (player_rect.x, player_rect.y))
            if r_n == 1:
                level_3.blit(right2, (player_rect.x, player_rect.y))
            if r_n == 3:
                level_3.blit(right3, (player_rect.x, player_rect.y))
                r_n = 0
            player_rect.x += vitesse
            if player_rect.colliderect(baque1_remplit_rect) and tomato == 0:
                baque1_remplit_rect.x += vitesse

                if hitbox3_mask.overlap(baque1_mask, (baque1_remplit_rect.x, baque1_remplit_rect.y)):
                    baque1_remplit_rect.x -= vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.x -= vitesse

                if baque1_remplit_rect.colliderect(baque2_remplit_rect):
                    baque1_remplit_rect.x -= vitesse
                    if player_rect.colliderect(baque1_remplit_rect):
                        player_rect.x -= vitesse

            elif player_rect.colliderect(baque2_remplit_rect) and tomato == 0:
                baque2_remplit_rect.x += vitesse

                if hitbox3_mask.overlap(baque2_mask, (baque2_remplit_rect.x, baque2_remplit_rect.y)):
                    baque2_remplit_rect.x -= vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.x -= vitesse

                if baque2_remplit_rect.colliderect(baque1_remplit_rect):
                    baque2_remplit_rect.x -= vitesse
                    if player_rect.colliderect(baque2_remplit_rect):
                        player_rect.x -= vitesse

            else:
                if hitbox3_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                    player_rect.x -= vitesse

            r_n += 1

        else:
            if state == "back":
                level_3.blit(back1, (player_rect.x, player_rect.y))
            if state == "right":
                level_3.blit(right1, (player_rect.x, player_rect.y))
            if state == "left":
                level_3.blit(left1, (player_rect.x, player_rect.y))
            if state == "front":
                level_3.blit(front1, (player_rect.x, player_rect.y))

        level_3.blit(f_heart, (125, 7))
        level_3.blit(f_heart, (155, 7))
        level_3.blit(f_heart, (185, 7))
        
        # on affiche les trois coeurs et leurs états grave a une condition avec la variable vie
        if vie == 5:
            level_3.blit(m_heart, (185, 7))
        if vie == 4:
            level_3.blit(e_heart, (185, 7))
        if vie == 3:
            level_3.blit(m_heart, (155, 7))
            level_3.blit(e_heart, (185, 7))
        if vie == 2:
            level_3.blit(e_heart, (155, 7))
            level_3.blit(e_heart, (185, 7))
        if vie == 1:
            level_3.blit(m_heart, (125, 7))
            level_3.blit(e_heart, (155, 7))
            level_3.blit(e_heart, (185, 7))
        if vie == 0:
            level_3.blit(e_heart, (125, 7))
            level_3.blit(e_heart, (155, 7))
            level_3.blit(e_heart, (185, 7))

        if player_rect.y < 0:
            with open('saves/saves.txt', 'a') as data:
                data.write('level3')
            level4()
            return vie and jeton_v


        # on definit et on affiche le text HEALTH a l'écran
        font = pg.font.SysFont('Operator', 55)
        text_f = font.render("health:", False, (0, 0, 0))
        level_3.blit(text_f, (0, 0))

        Clock.tick(10)
        pg.display.flip()

#--------------------------------------------------------------------------------------------------level 4---------------------------------------------------------------------------
    
def level4():
    global vie
    global jeton_v

    level_4 = pg.display.set_mode((1025, 825))

    pg.display.set_caption('enigmatic game level2')

    # on stock les trois états possibles des coeurs avant de les affichers
    f_heart = pg.image.load('health/full heart.png')
    m_heart = pg.image.load('health/mid heart.png')
    e_heart = pg.image.load('health/empty heart.png')
    jeton = pg.image.load('environement/interact/jetons.png')

    state = "right"

    borne_d_rect.x, borne_d_rect.y = 460, 760

    vitesse = 7

    player_rect.x, player_rect.y = 500, 785

    jeton_int_rect.x, jeton_int_rect.y = 230, 335

    # on definit dans des variable l'état de l'animation
    l_n = 1
    r_n = 1
    b_n = 1
    f_n = 1
    
    piece1_t = "False"
    piece2_t = "False"
    piece3_t = "False"
    piece4_t = "False"
    piece5_t = "False"
    piece6_t = "False"
    piece7_t = "False"
    piece8_t = "False"
    piece9_t = "False"
    piece10_t = "False"
    piece11_t = "False"
    piece12_t = "False"
    piece13_t = "False"
    piece14_t = "False"
    piece15_t = "False"
    piece16_t = "False"
    piece17_t = "False"
    piece18_t = "False"
    piece19_t = "False"
    piece20_t = "False"
    piece21_t = "False"
    piece22_t = "False"
    piece23_t = "False"
    piece24_t = "False"
    piece25_t = "False"
    piece26_t = "False"
    piece27_t = "False"
    piece28_t = "False"
    piece29_t = "False"
    piece30_t = "False"
    piece31_t = "False"
    piece32_t = "False"
    piece33_t = "False"
    piece34_t = "False"
    piece35_t = "False"
    piece36_t = "False"
    piece37_t = "False"
    piece38_t = "False"
    piece39_t = "False"
    piece40_t = "False"
    piece41_t = "False"
    piece42_t = "False"
    piece43_t = "False"
    piece44_t = "False"
    piece45_t = "False"
    piece46_t = "False"
    piece47_t = "False"
    piece48_t = "False"
    piece49_t = "False"
    piece50_t = "False"
    piece51_t = "False"
    piece52_t = "False"
    piece53_t = "False"
    piece54_t = "False"
    piece55_t = "False"
    piece56_t = "False"
    piece57_t = "False"
    piece58_t = "False"
    piece59_t = "False"
    piece60_t = "False"
    piece61_t = "False"
    piece62_t = "False"
    piece63_t = "False"
    piece64_t = "False"
    piece65_t = "False"
    piece66_t = "False"
    piece67_t = "False"
    piece68_t = "False"
    piece69_t = "False"
    piece70_t = "False"
    
    porte_rect.x, porte_rect.y = 480, -80
    
    piece_t_L =    [piece1_t, piece2_t, piece3_t, piece4_t, piece5_t, piece6_t, piece7_t, piece8_t, piece9_t, piece10_t, piece11_t, piece12_t, piece13_t, piece14_t, piece15_t, piece16_t, piece17_t, piece18_t, piece19_t, piece20_t, piece21_t, piece22_t, piece23_t, piece24_t, piece25_t, piece26_t, piece27_t, piece28_t, piece29_t, piece30_t, piece31_t, piece32_t, piece33_t, piece34_t, piece35_t, piece36_t, piece37_t, piece38_t, piece39_t, piece40_t, piece41_t, piece42_t, piece43_t, piece44_t, piece45_t, piece46_t, piece47_t, piece48_t, piece49_t, piece50_t, piece51_t, piece52_t, piece53_t, piece54_t, piece55_t, piece56_t, piece57_t, piece58_t, piece59_t, piece60_t, piece61_t, piece62_t, piece63_t, piece64_t, piece65_t, piece66_t, piece67_t, piece68_t, piece69_t, piece70_t]
    piece_L =      [piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9, piece10, piece11, piece12, piece13, piece14, piece15, piece16, piece17, piece18, piece19, piece20, piece21, piece22, piece23, piece24, piece25, piece26, piece27, piece28, piece29, piece30, piece31, piece32, piece33, piece34, piece35, piece36, piece37, piece38, piece39, piece40, piece41, piece42, piece43, piece44, piece45, piece46, piece47, piece48, piece49, piece50, piece51, piece52, piece53, piece54, piece55, piece56, piece57, piece58, piece59, piece60, piece61, piece62, piece63, piece64, piece65, piece66, piece67, piece68, piece69, piece70]
    piece_rect_L = [piece1_rect, piece2_rect, piece3_rect, piece4_rect, piece5_rect, piece6_rect, piece7_rect, piece8_rect, piece9_rect, piece10_rect, piece11_rect, piece12_rect, piece13_rect, piece14_rect, piece15_rect, piece16_rect, piece17_rect, piece18_rect, piece19_rect, piece20_rect, piece21_rect, piece22_rect, piece23_rect, piece24_rect, piece25_rect, piece26_rect, piece27_rect, piece28_rect, piece29_rect, piece30_rect, piece31_rect, piece32_rect, piece33_rect, piece34_rect, piece35_rect, piece36_rect, piece37_rect, piece38_rect, piece39_rect, piece40_rect, piece41_rect, piece42_rect, piece43_rect, piece44_rect, piece45_rect, piece46_rect, piece47_rect, piece48_rect, piece49_rect, piece50_rect, piece51_rect, piece52_rect, piece53_rect, piece54_rect, piece55_rect, piece56_rect, piece57_rect, piece58_rect, piece59_rect, piece60_rect, piece61_rect, piece62_rect, piece63_rect, piece64_rect, piece65_rect, piece66_rect, piece67_rect, piece68_rect, piece69_rect, piece70_rect]
    cases_L_rect = [cases1_rect, cases2_rect, cases3_rect, cases4_rect, cases5_rect, cases6_rect, cases7_rect, cases8_rect, cases9_rect, cases10_rect, cases11_rect, cases12_rect, cases13_rect, cases14_rect, cases15_rect, cases16_rect, cases17_rect, cases18_rect, cases19_rect, cases20_rect, cases21_rect, cases22_rect, cases23_rect, cases24_rect, cases25_rect, cases26_rect, cases27_rect, cases28_rect, cases29_rect, cases30_rect, cases31_rect, cases32_rect, cases33_rect, cases34_rect, cases35_rect, cases36_rect, cases37_rect, cases38_rect, cases39_rect, cases40_rect, cases41_rect, cases42_rect, cases43_rect, cases44_rect, cases45_rect, cases46_rect, cases47_rect, cases48_rect, cases49_rect, cases50_rect, cases51_rect, cases52_rect, cases53_rect, cases54_rect, cases55_rect, cases56_rect, cases57_rect, cases58_rect, cases59_rect, cases60_rect, cases61_rect, cases62_rect, cases63_rect, cases64_rect, cases65_rect, cases66_rect, cases67_rect, cases68_rect, cases69_rect, cases70_rect]
    cases_L =      [cases1, cases2, cases3, cases4, cases5, cases6, cases7, cases8, cases9, cases10, cases11, cases12, cases13, cases14, cases15, cases16, cases17, cases18, cases19, cases20, cases21, cases23, cases24, cases25, cases26, cases27, cases28, cases29, cases30, cases31, cases32, cases33, cases34, cases35, cases36, cases37, cases38, cases39, cases40, cases41, cases42, cases43, cases44, cases45, cases46, cases47, cases48, cases49, cases50, cases51, cases52, cases53, cases54, cases55, cases56, cases57, cases58, cases59, cases60, cases61, cases62, cases63, cases64, cases65, cases66, cases67, cases68, cases69, cases70]
    
    hitbox_sel = 1
    
    étincelle_state = 0
    étincelle_state1 = 0
    étincelle_state2 = 0
    étincelle_state3 = 0
    
    pressed = pg.key.get_pressed()
    
    stick_t = "not taked"
    
    nuc_x, nuc_y = 500, -82
    
    finish = 0
    
    nuclear_state = False
    
    state_train = "stay"
    
    Clock = pg.time.Clock()
    
    #ici on reprend les coordonée (si la personne veut) du fichier de sauvegarde et on mets les valeeurs dans leur variable respective pour chaque ppiece du puzzle
    T = True
    ind = 0
    with open('saves/saves.txt', 'r') as data:
        for i in range(489):
            temp = 0
            a = data.readline()
                
            if a == "\n":
                pass
            elif a == "xd\n":
                T = False
            elif a == "fx\n":
                T = True
                
            elif not T:
                temp += int(a)
                    
                piece_rect_L[ind].x = temp
                    
                ind += 1
        
    T = True
    ind = 0
    with open('saves/saves.txt', 'r') as data:
        for i in range(489):
            temp = 0
            a = data.readline()
                
            if a == "\n":
                pass
            elif a == "yd\n":
                T = False
            elif a == "fy\n":
                T = True
                
            elif not T:
                temp += int(a)
                    
                piece_rect_L[ind].y = temp
                    
                ind += 1
        
    T = True
    ind = 0
    with open('saves/saves.txt', 'r') as data:
        for i in range(6):
            temp = ""
            a = data.readline()
                
            if a == "\n":
                pass
            elif a == "sd\n":
                T = False
            elif a == "fs\n":
                T = True
                
            elif not T:
                temp += a
                    
                stick_t = temp
                    
            if stick_t == "taked\n":
                stick_rect.x,stick_rect.y = 0, 0
                stick_t = "taked"
                    
                ind += 1
        
    for i in range(len(piece_rect_L)):
        if piece_rect_L[i-1].colliderect(cases_L_rect[i-1]):
            piece_rect_L[i-1].x, piece_rect_L[i-1].y = cases_L[i-1].x, cases_L[i-1].y
            piece_t_L[i-1] = "locked"
    
    Nvt = 15

    pg.display.flip()

    running = True

    # on crée la boucle du jeux
    while running:
        pressed = pg.key.get_pressed()
        level_4.blit(background4, (0,0))
        level_4.blit(chatbox, (162, 768))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        
        if player_rect.x < -25:
            level4_2()
            pg.quit()

        #------------------------------début de la gestion des pieces de puzzle----------------------------
        #on fait la gestion des pieces du puzzle ici pour que le script soit plus lisible
        #on detecte si on tiens deja une piece en main, si oui on rajoute 1 a p_detect ce qui desactivera les detections des autre pieces
        for i in range(len(cases_L)):
            level_4.blit(cases_L[i-1], (cases_L_rect[i-1].x, cases_L_rect[i-1].y))
            
        p_detect = 0
        for i in piece_t_L:
            if i == "True":
                p_detect += 1
            else:
                pass

        if not p_detect > 0:
            for i in range(72):
                if i == 16:
                    pass
                else:
                    if player_rect.colliderect(piece_rect_L[i-2]) and piece_t_L[i-2] == "False":
                        font = pg.font.SysFont('arial', 20)
                        text_f = font.render("take the puzzle piece [e]", False, (0, 0, 0))
                        level_4.blit(text_f, (173, 790))
                        if pressed[pg.K_e]:
                            piece_t_L[i-2] = "True"
        
        #on propose de lacher la piece tenu en main
        
        for i in range(len(cases_L_rect)):
            if piece_t_L[i-1] == "True":
                font = pg.font.SysFont('arial', 20)
                text_f = font.render("drop the puzzle piece [r]", False, (0, 0, 0))
                level_4.blit(text_f, (173, 790))
                if pressed[pg.K_r]:
                    piece_t_L[i-1] = "False"
                    if piece_rect_L[i-1].colliderect(cases_L_rect[i-1]):
                        piece_rect_L[i-1].x, piece_rect_L[i-1].y = cases_L_rect[i-1].x, cases_L_rect[i-1].y
                        piece_t_L[i-1] = "locked"
        
        #ici on verifie pour chaque piece du puzzle si on la tiens en main, si oui on ne l'affiche pas
        
        for i in range(71):
            if i == 16:
                pass
            else:
                if piece_t_L[i-1] == "False" or piece_t_L[i-1] == "locked":
                    level_4.blit(piece_L[i-1], (piece_rect_L[i-1].x, piece_rect_L[i-1].y))
                elif piece_t_L[i-1] == "True":
                    piece_rect_L[i-1].x, piece_rect_L[i-1].y = player_rect.x, player_rect.y
        finish = 0
        for i in piece_t_L:
            if i == "locked":
                finish += 1
        
        if finish == 70:
            porte_rect.x, porte_rect.y = -1000, -1000
        else:
            level_4.blit(porte, (porte_rect.x, porte_rect.y))
        
        #-------------------------------fin de la gestion des pieces de puzzle-------------------------------
        
        level_4.blit(jeton, (0, 50))
        font = pg.font.SysFont('arial', 32)
        text_f = font.render(f": {jeton_v}/3", False, (0, 0, 0))
        level_4.blit(text_f, (35, 47))
        
        if stick_rect.colliderect(player_rect) and stick_t == "not taked" and p_detect == 0:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the stick [e]", False, (0, 0, 0))
            level_4.blit(text_f, (173, 790))
            
            if pressed[pg.K_e]:
                stick_rect.x,stick_rect.y = 0, 0
                stick_t = "taked"
        
        if stick_t == "taked" and p_detect == 0:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("drop the stick [f]", False, (0, 0, 0))
            level_4.blit(text_f, (173, 790))
            
            if pressed[pg.K_f]:
                stick_rect.x,stick_rect.y = player_rect.x, player_rect.y
                stick_t = "not taked"
        
        if stick_t == "taked":
            pass
        else:
            level_4.blit(stick,(stick_rect.x, stick_rect.y))
        
        nt = random.randint(0, 100)
        
        if nt == 5 and state_train == 'stay':
            state_train = "Move"
        
        if state_train == 'Move':
            train_rect.x -= 15
            train_rect.y = 545
        
        if train_rect.x < -702 and state_train == "Move":
            state_train = "stay"
            train_rect.x, train_rect.y= 1026, -10000
                
        if train_rect.colliderect(player_rect):
            vie -= 1
        
        if train_rect.colliderect(stick_rect) and not state_train == "destroyed_move":
            state_train = "destroyed_move"
            destroyed_train_rect.x, destroyed_train_rect.y = train_rect.x, train_rect.y
            train_rect.x, train_rect.y = -1000, -1000
        
        if state_train == "destroyed_move":
            if Nvt == 0:
                state_train = "stay_destroyed"
            else:
                destroyed_train_rect.x -= Nvt
                Nvt -= 1
        
        if state_train == "destroyed_move" or state_train == "stay_destroyed":
            level_4.blit(destroyed_train, (destroyed_train_rect.x, 555))
        
        elif not state_train == "destroyed_move" or not state_train == "stay_destroyed":
            level_4.blit(train, (train_rect.x, train_rect.y))
        
        nuclear_count = 0
        for i in piece_t_L:
            if i == "True":
                nuclear_count += 1
        
        if nuclear_count > 1:
            nuclear_state = True
        
        if nuclear_state == True:
            level_4.blit(nuclear_bomb, (nuc_x, nuc_y))
            nuc_y += 10
            if nuc_y > 450:
                pg.QUIT
                bomb_game_over()
        
        if state_train == "destroyed_move":
            if étincelle_state == 0:
                level_4.blit(étincelle1, (destroyed_train_rect.x - 12, 557))
            elif étincelle_state == 1:
                level_4.blit(étincelle2, (destroyed_train_rect.x - 12, 557))
            elif étincelle_state == 2:
                level_4.blit(étincelle3, (destroyed_train_rect.x - 12, 557))
            elif étincelle_state == 3:
                level_4.blit(étincelle3, (destroyed_train_rect.x - 12, 557))
            elif étincelle_state == 4:
                level_4.blit(étincelle4, (destroyed_train_rect.x - 12, 557))
            elif étincelle_state == 5:
                level_4.blit(étincelle5, (destroyed_train_rect.x - 12, 557))
            elif étincelle_state == 6:
                level_4.blit(étincelle6, (destroyed_train_rect.x - 12, 557))
                
            if étincelle_state1 == 0:
                level_4.blit(étincelle1, (destroyed_train_rect.x + 163, 557))
            elif étincelle_state1 == 1:
                level_4.blit(étincelle2, (destroyed_train_rect.x + 163, 557))
            elif étincelle_state1 == 2:
                level_4.blit(étincelle3, (destroyed_train_rect.x + 163, 557))
            elif étincelle_state1 == 3:
                level_4.blit(étincelle3, (destroyed_train_rect.x + 163, 557))
            elif étincelle_state1 == 4:
                level_4.blit(étincelle4, (destroyed_train_rect.x + 163, 557))
            elif étincelle_state1 == 5:
                level_4.blit(étincelle5, (destroyed_train_rect.x + 163, 557))
            elif étincelle_state1 == 6:
                level_4.blit(étincelle6, (destroyed_train_rect.x + 163, 557))
            
            if étincelle_state2 == 0:
                level_4.blit(étincelle1, (destroyed_train_rect.x + 340, 557))
            elif étincelle_state2 == 1:
                level_4.blit(étincelle2, (destroyed_train_rect.x + 340, 557))
            elif étincelle_state2 == 2:
                level_4.blit(étincelle3, (destroyed_train_rect.x + 340, 557))
            elif étincelle_state2 == 3:
                level_4.blit(étincelle3, (destroyed_train_rect.x + 340, 557))
            elif étincelle_state2 == 4:
                level_4.blit(étincelle4, (destroyed_train_rect.x + 340, 557))
            elif étincelle_state2 == 5:
                level_4.blit(étincelle5, (destroyed_train_rect.x + 340, 557))
            elif étincelle_state2 == 6:
                level_4.blit(étincelle6, (destroyed_train_rect.x + 340, 557))
            
            if étincelle_state3 == 0:
                level_4.blit(étincelle1, (destroyed_train_rect.x + 517, 557))
            elif étincelle_state3 == 1:
                level_4.blit(étincelle2, (destroyed_train_rect.x + 517, 557))
            elif étincelle_state3 == 2:
                level_4.blit(étincelle3, (destroyed_train_rect.x + 517, 557))
            elif étincelle_state3 == 3:
                level_4.blit(étincelle3, (destroyed_train_rect.x + 517, 557))
            elif étincelle_state3 == 4:
                level_4.blit(étincelle4, (destroyed_train_rect.x + 517, 557))
            elif étincelle_state3 == 5:
                level_4.blit(étincelle5, (destroyed_train_rect.x + 517, 557))
            elif étincelle_state3 == 6:
                level_4.blit(étincelle6, (destroyed_train_rect.x + 517, 557))
            
            étincelle_state += 1
            
            if étincelle_state == 6:
                étincelle_state = 0
                
            étincelle_state1 += 1
            
            if étincelle_state1 == 6:
                étincelle_state1 = 0
            
            étincelle_state2 += 1
            
            if étincelle_state2 == 6:
                étincelle_state2 = 0
            
            étincelle_state3 += 1
            
            if étincelle_state3 == 6:
                étincelle_state3 = 0
        
        # on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            if b_n == 1:
                level_4.blit(back2, (player_rect.x, player_rect.y))
                
            if b_n == 2:
                level_4.blit(back1, (player_rect.x, player_rect.y))
                
            if b_n == 3:
                level_4.blit(back3, (player_rect.x, player_rect.y))
            
            if b_n == 4:
                level_4.blit(back2, (player_rect.x, player_rect.y))
                b_n = 0

            player_rect.y -= vitesse
            b_n += 1

            if hitbox4_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y += vitesse
            
            if destroyed_train_rect.colliderect(player_rect):
                player_rect.y += vitesse
            
            if porte_rect.colliderect(player_rect):
                player_rect.y += vitesse

        elif pressed[pg.K_LEFT]:
            state = "left"
            if l_n == 2 or l_n == 4:
                level_4.blit(left1, (player_rect.x, player_rect.y))
            if l_n == 1:
                level_4.blit(left2, (player_rect.x, player_rect.y))
            if l_n == 3:
                level_4.blit(left3, (player_rect.x, player_rect.y))
                l_n = 0

            player_rect.x -= vitesse
            l_n += 1

            if hitbox4_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x += vitesse
            
            if destroyed_train_rect.colliderect(player_rect):
                player_rect.x += vitesse
            
            if porte_rect.colliderect(player_rect):
                player_rect.x += vitesse

        elif pressed[pg.K_DOWN]:
            state = "front"
            if f_n == 2 or f_n == 4:
                level_4.blit(front1, (player_rect.x, player_rect.y))
            if f_n == 1:
                level_4.blit(front2, (player_rect.x, player_rect.y))
            if f_n == 3:
                level_4.blit(front3, (player_rect.x, player_rect.y))
                f_n = 0

            player_rect.y += vitesse
            f_n += 1

            if hitbox4_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y -= vitesse
            
            if destroyed_train_rect.colliderect(player_rect):
                player_rect.y -= vitesse
            
            if porte_rect.colliderect(player_rect):
                player_rect.y -= vitesse

        elif pressed[pg.K_RIGHT]:
            state = "right"
            if r_n == 2 or r_n == 4:
                level_4.blit(right1, (player_rect.x, player_rect.y))
            if r_n == 1:
                level_4.blit(right2, (player_rect.x, player_rect.y))
            if r_n == 3:
                level_4.blit(right3, (player_rect.x, player_rect.y))
                r_n = 0
            player_rect.x += vitesse
            r_n += 1

            if hitbox4_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x -= vitesse
            
            if destroyed_train_rect.colliderect(player_rect):
                player_rect.x -= vitesse
            
            if porte_rect.colliderect(player_rect):
                player_rect.x += vitesse

        else:
            if state == "back":
                level_4.blit(back1, (player_rect.x, player_rect.y))
            if state == "right":
                level_4.blit(right1, (player_rect.x, player_rect.y))
            if state == "left":
                level_4.blit(left1, (player_rect.x, player_rect.y))
            if state == "front":
                level_4.blit(front1, (player_rect.x, player_rect.y))

        # on affiche les trois coeurs et leurs états grave a une condition avec la variable vie
        if vie == 6:
            level_4.blit(f_heart, (125, 7))
            level_4.blit(f_heart, (155, 7))
            level_4.blit(f_heart, (185, 7))
        if vie == 5:
            level_4.blit(f_heart, (125, 7))
            level_4.blit(f_heart, (155, 7))
            level_4.blit(m_heart, (185, 7))
        if vie == 4:
            level_4.blit(f_heart, (125, 7))
            level_4.blit(f_heart, (155, 7))
            level_4.blit(e_heart, (185, 7))
        if vie == 3:
            level_4.blit(f_heart, (125, 7))
            level_4.blit(m_heart, (155, 7))
            level_4.blit(e_heart, (185, 7))
        if vie == 2:
            level_4.blit(f_heart, (125, 7))
            level_4.blit(e_heart, (155, 7))
            level_4.blit(e_heart, (185, 7))
        if vie == 1:
            level_4.blit(m_heart, (125, 7))
            level_4.blit(e_heart, (155, 7))
            level_4.blit(e_heart, (185, 7))
        if vie == 0:
            level_4.blit(e_heart, (125, 7))
            level_4.blit(e_heart, (155, 7))
            level_4.blit(e_heart, (185, 7))
            game_over()
        
        if player_rect.y < -37:
            with open('saves/saves.txt', 'a') as data:
                data.write('level4')
            end()
            
        if pressed[pg.K_s]:
            c = 1
            font = pg.font.SysFont('arial', 90)
            text_f = font.render("Game Saved", False, (0, 255, 0))
            level_4.blit(text_f, (300, 350))
            
            with open('saves/saves.txt', 'w') as data:
                data.write('level3 \n'
                           '\n'
                            'sd\n'
                            f'{stick_t}\n'
                            'fs\n')
            
            
            for i in range(len(piece_rect_L)):
                with open('saves/saves.txt', 'a') as data:
                    data.write('\n'
                                'xd\n'
                                f'{piece_rect_L[i].x} \n'
                                'fx\n'
                                'yd\n'
                                f'{piece_rect_L[i].y} \n'
                                'fy\n')
        
        # on definit et on affiche le text HEALTH a l'écran
        font = pg.font.SysFont('Operator', 55)
        text_f = font.render("health:", False, (0, 0, 0))
        level_4.blit(text_f, (0, 0))

        Clock.tick(10)
        pg.display.flip()

#niveau annexe du niveau4

def level4_2():
    global vie
    global jeton_v

    level_4_2 = pg.display.set_mode((1025, 825))

    pg.display.set_caption('enigmatic game level2')
    
    # on stock les trois états possibles des coeurs avant de les affichers
    f_heart = pg.image.load('health/full heart.png')
    m_heart = pg.image.load('health/mid heart.png')
    e_heart = pg.image.load('health/empty heart.png')
    jeton = pg.image.load('environement/interact/jetons.png')

    state = "right"
    achat = 0

    borne_d_rect.x, borne_d_rect.y = 455, 760
    
    hitbox_way_rect.x, hitbox_way_rect.y = 120, 120
    
    vitesse = 7
    
    button1_rect.x, button1_rect.y = 475, 520
    
    piece16_t = "False"

    player_rect.x, player_rect.y = 1000, 565

    # on definit dans des variable l'état de l'animation
    l_n = 1
    r_n = 1
    b_n = 1
    f_n = 1

    Clock = pg.time.Clock()

    pg.display.flip()

    running = True

    # on crée la boucle du jeux
    while running:
        pressed = pg.key.get_pressed()
        level_4_2.blit(background4_2, (0,0))
        level_4_2.blit(chatbox, (162, 768))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
        
        if piece16_t == "False":
            level_4_2.blit(piece16, (piece16_rect.x, piece16_rect.y))
        elif piece16_t == "True":
            piece16_rect.x, piece16_rect.y = player_rect.x, player_rect.y
        
        if player_rect.colliderect(piece16_rect) and piece16_t == "False":
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the puzzle piece [e]", False, (0, 0, 0))
            level_4_2.blit(text_f, (173, 790))
            if pressed[pg.K_e]:
                piece16_t = "True"
        
        if piece16_t == "True":
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("drop the puzzle piece [r]", False, (0, 0, 0))
            level_4_2.blit(text_f, (173, 790))
            if pressed[pg.K_r]:
                piece16_t = "False"
        
        if button1_rect.colliderect(player_rect):
            level_4_2.blit(button1_d, (button1_rect.x, button1_rect.y))
            level_4_2.blit(good_way, (120, 120))
        else:
            level_4_2.blit(button1_p, (button1_rect.x, button1_rect.y))
            level_4_2.blit(hide_way, (120, 120))
        
        # on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            if b_n == 1:
                level_4_2.blit(back2, (player_rect.x, player_rect.y))
                
            if b_n == 2:
                level_4_2.blit(back1, (player_rect.x, player_rect.y))
                
            if b_n == 3:
                level_4_2.blit(back3, (player_rect.x, player_rect.y))
            
            if b_n == 4:
                level_4_2.blit(back2, (player_rect.x, player_rect.y))
                b_n = 0

            player_rect.y -= vitesse
            b_n += 1

            if hitbox4_2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y += vitesse
            
            if hitbox_way_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                print('colision')
                game_over()
                pg.quit()

        elif pressed[pg.K_LEFT]:
            state = "left"
            if l_n == 2 or l_n == 4:
                level_4_2.blit(left1, (player_rect.x, player_rect.y))
            if l_n == 1:
                level_4_2.blit(left2, (player_rect.x, player_rect.y))
            if l_n == 3:
                level_4_2.blit(left3, (player_rect.x, player_rect.y))
                l_n = 0

            player_rect.x -= vitesse
            l_n += 1

            if hitbox4_2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x += vitesse
            
            if hitbox_way_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                game_over()
                pg.quit()

        elif pressed[pg.K_DOWN]:
            state = "front"
            if f_n == 2 or f_n == 4:
                level_4_2.blit(front1, (player_rect.x, player_rect.y))
            if f_n == 1:
                level_4_2.blit(front2, (player_rect.x, player_rect.y))
            if f_n == 3:
                level_4_2.blit(front3, (player_rect.x, player_rect.y))
                f_n = 0

            player_rect.y += vitesse
            f_n += 1

            if hitbox4_2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.y -= vitesse
                
            if hitbox_way_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                game_over()
                pg.quit()

        elif pressed[pg.K_RIGHT]:
            state = "right"
            if r_n == 2 or r_n == 4:
                level_4_2.blit(right1, (player_rect.x, player_rect.y))
            if r_n == 1:
                level_4_2.blit(right2, (player_rect.x, player_rect.y))
            if r_n == 3:
                level_4_2.blit(right3, (player_rect.x, player_rect.y))
                r_n = 0
            player_rect.x += vitesse
            r_n += 1

            if hitbox4_2_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                player_rect.x -= vitesse
            
            if hitbox_way_mask.overlap(player_mask, (player_rect.x, player_rect.y)):
                game_over()
                pg.quit()

        else:
            if state == "back":
                level_4_2.blit(back1, (player_rect.x, player_rect.y))
            if state == "right":
                level_4_2.blit(right1, (player_rect.x, player_rect.y))
            if state == "left":
                level_4_2.blit(left1, (player_rect.x, player_rect.y))
            if state == "front":
                level_4_2.blit(front1, (player_rect.x, player_rect.y))
        
        pg.display.flip()
        Clock.tick(10)

level4_2()

with open('saves/saves.txt', 'r+') as save:
    verif = save.read()
if "level4" in verif:
    end()
if "level3" in verif:
    level4()
if "level2" in verif:
    level3()
if "level1" in verif:
    level2()
else:
    main_menu()