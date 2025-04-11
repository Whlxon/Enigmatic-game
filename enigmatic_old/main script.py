import pygame as pg 
import time
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
            time.sleep(0.16)
            if b_n == 2 or b_n == 4:
                window.blit(self.back1, (player_rect.x, player_rect.y))
            if b_n == 1:
                window.blit(self.back2, (player_rect.x, player_rect.y))
            if b_n == 3:
                window.blit(self.back3, (player_rect.x, player_rect.y))
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
            time.sleep(0.16)
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
            time.sleep(0.16)
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
            time.sleep(0.16)
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
                rock1_rect.x, rock1_rect.y = player_rect.x, (player_rect.y + 20)
        
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
            text_f = font.render("drop the rock > [g]", False, (0, 0, 0))
            window.blit(text_f, (382, 770))
            if pressed[pg.K_g]:
                take.remove('rock2 take')
                take.insert(0, 'rock2 not take')
                rock2_rect.x, rock2_rect.y = player_rect.x, (player_rect.y + 20)
        
        #on verifie si le joueur ce tiens a portée du deuxième caillou et on verifie si il n'a pas deja été pris, si non alors on
        #affiche la possibilité de le prendre avec un text label, si la touche [e] est presser alors on enleve le deuxième cailloux
        #et on mets sa boite de colision en haut a gauche pour pas gêner le joueur
        if player_rect.colliderect(rock2_rect) and 'rock2 not take' in take:
            font = pg.font.SysFont('arial', 20)
            text_f = font.render("take the rock > [r]", False, (0, 0, 0))
            window.blit(text_f, (382, 770))
            if pressed[pg.K_r]:
                take.remove('rock2 not take')
                take.insert(0, 'rock2 take')
        
        if button2_rect.colliderect(rock1_rect) or button2_rect.colliderect(rock2_rect) or button2_rect.colliderect(player_rect):
            if button1_rect.colliderect(rock1_rect) or button1_rect.colliderect(rock2_rect) or button1_rect.colliderect(player_rect):
                font = pg.font.SysFont('arial', 30)
                text_f = font.render("the door is open", False, (0, 255, 0))
                window.blit(text_f, (420, 0))
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
            time.sleep(0.16)
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
            time.sleep(0.16)
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
            time.sleep(0.16)
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
            time.sleep(0.16)
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
        if vie == 6:
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
            font = pg.font.SysFont('arial', 22)
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
            if 'rock not take' in take and 'rock2 not take' in take:
                font = pg.font.SysFont('arial', 25)
                text_f = font.render("talk to Darkadesse [Espace]", False, (0, 0, 0))
                level_3.blit(text_f, (133, 790))
                if pressed[pg.K_SPACE]:
                    papotte = 'papotte'

        if papotte == 'papotte':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("Hi friend, do you ", False, (0, 0, 0))
            level_3.blit(text_f, (133, 770))
            text_f = font.render("want to pay a hint? [y]/[n]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_y]:
                papotte = 'achat indice'

        if player_rect.colliderect(jean_pierre_rect) and jean_pierre_talk == 'aide accept':
            if baque1_remplit_rect.colliderect(drop_zone_rect) and baque2_remplit_rect.colliderect(drop_zone_rect):
                font = pg.font.SysFont('arial', 22)
                text_f = font.render("reclaim the reward", False, (0, 0, 0))
                level_3.blit(text_f, (133, 770))
                text_f = font.render("[space]", False, (0, 0, 0))
                level_3.blit(text_f, (133, 790))
                if pressed[pg.K_SPACE]:
                    jean_pierre_talk = "done"
                    buche = 4

        if player_rect.colliderect(jean_pierre_rect) and jean_pierre_talk == 'aide':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("Can you push the tomatos baque", False, (0, 0, 0))
            level_3.blit(text_f, (133, 770))
            text_f = font.render("into the zone here please? [o]/[n]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                jean_pierre_talk = "parler"
            elif pressed[pg.K_o]:
                jean_pierre_talk = "aide accept"

        if player_rect.colliderect(jean_pierre_rect) and jean_pierre_talk == 'parler':
            font = pg.font.SysFont('arial', 25)
            text_f = font.render("talk to Jean Pierre [Espace]", False, (0, 0, 0))
            level_3.blit(text_f, (133, 775))
            if pressed[pg.K_SPACE]:
                jean_pierre_talk = 'papotte'

        if jean_pierre_talk == 'papotte':
            font = pg.font.SysFont('arial', 22)
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
                font = pg.font.SysFont('arial', 22)
                text_f = font.render("the bridge is broken", False, (0, 0, 0))
                level_3.blit(text_f, (133, 770))
                text_f = font.render(f"{buche}/4 planks", False, (0, 0, 0))
                level_3.blit(text_f, (133, 790))


        # on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            time.sleep(0.16)
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
            time.sleep(0.16)
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
            time.sleep(0.16)
            if f_n == 2 or f_n == 4:
                level_3.blit(front1, (player_rect.x, player_rect.y))
            if f_n == 1:
                level_3.blit(front2, (player_rect.x, player_rect.y))
            if f_n == 3:
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
            time.sleep(0.16)
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

        # on affiche les trois coeurs et leurs états grave a une condition avec la variable vie
        if vie == 6:
            level_3.blit(f_heart, (125, 7))
            level_3.blit(f_heart, (155, 7))
            level_3.blit(f_heart, (185, 7))
        if vie == 5:
            level_3.blit(f_heart, (125, 7))
            level_3.blit(f_heart, (155, 7))
            level_3.blit(m_heart, (185, 7))
        if vie == 4:
            level_3.blit(f_heart, (125, 7))
            level_3.blit(f_heart, (155, 7))
            level_3.blit(e_heart, (185, 7))
        if vie == 3:
            level_3.blit(f_heart, (125, 7))
            level_3.blit(m_heart, (155, 7))
            level_3.blit(e_heart, (185, 7))
        if vie == 2:
            level_3.blit(f_heart, (125, 7))
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
            pg.quit()


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
    achat = 0

    borne_d_rect.x, borne_d_rect.y = 720, 760

    vitesse = 7

    papotte = 'parler'

    jeton_act = True

    player_rect.x, player_rect.y = 765, 785

    jeton_int_rect.x, jeton_int_rect.y = 230, 335

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
        level_4.fill((255, 255, 255))
        level_4.blit(chatbox, (362, 768))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        level_4.blit(jeton, (0, 50))
        font = pg.font.SysFont('arial', 32)
        text_f = font.render(f": {jeton_v}/3", False, (0, 0, 0))
        level_4.blit(text_f, (35, 47))

        # on affiche la borne d'achat
        if achat == 0:
            level_4.blit(borne_d, (borne_d_rect.x, borne_d_rect.y))
        else:
            borne_d_rect.x, borne_d_rect.y = 0, 0

        if papotte == 'achat indice':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("it will cost you 1 jeton", False, (0, 0, 0))
            level_4.blit(text_f, (133, 770))
            text_f = font.render("do you accept? [o]/[n]", False, (0, 0, 0))
            level_4.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_o]:
                papotte = 'indice récup'
                jeton_v -= 1
                achat += 1

        # on voit s'il est a proximiter de la borne si oui on propose de lui parler
        if player_rect.colliderect(borne_d_rect) and papotte == 'parler':
            if 'rock not take' in take and 'rock2 not take' in take:
                font = pg.font.SysFont('arial', 25)
                text_f = font.render("talk to Darkadesse [Espace]", False, (0, 0, 0))
                level_4.blit(text_f, (133, 790))
                if pressed[pg.K_SPACE]:
                    papotte = 'papotte'

        if papotte == 'papotte':
            font = pg.font.SysFont('arial', 22)
            text_f = font.render("Hi friend, do you ", False, (0, 0, 0))
            level_4.blit(text_f, (133, 770))
            text_f = font.render("want to pay a hint? [y]/[n]", False, (0, 0, 0))
            level_4.blit(text_f, (133, 790))
            if pressed[pg.K_n]:
                papotte = 'parler'
            elif pressed[pg.K_y]:
                papotte = 'achat indice'

        # on verifie les touche presser et on effectu les animation et déplacement requis
        if pressed[pg.K_UP]:
            state = "back"
            time.sleep(0.16)
            if b_n == 2 or b_n == 4:
                level_4.blit(back1, (player_rect.x, player_rect.y))
            if b_n == 1:
                level_4.blit(back2, (player_rect.x, player_rect.y))
            if b_n == 3:
                level_4.blit(back3, (player_rect.x, player_rect.y))
                b_n = 0

            player_rect.y -= vitesse
            b_n += 1

        elif pressed[pg.K_LEFT]:
            state = "left"
            time.sleep(0.16)
            if l_n == 2 or l_n == 4:
                level_4.blit(left1, (player_rect.x, player_rect.y))
            if l_n == 1:
                level_4.blit(left2, (player_rect.x, player_rect.y))
            if l_n == 3:
                level_4.blit(left3, (player_rect.x, player_rect.y))
                l_n = 0

            player_rect.x -= vitesse
            l_n += 1

        elif pressed[pg.K_DOWN]:
            state = "front"
            time.sleep(0.16)
            if f_n == 2 or f_n == 4:
                level_4.blit(front1, (player_rect.x, player_rect.y))
            if f_n == 1:
                level_4.blit(front2, (player_rect.x, player_rect.y))
            if f_n == 3:
                level_4.blit(front3, (player_rect.x, player_rect.y))
                f_n = 0

            player_rect.y += vitesse
            f_n += 1

        elif pressed[pg.K_RIGHT]:
            state = "right"
            time.sleep(0.16)
            if r_n == 2 or r_n == 4:
                level_4.blit(right1, (player_rect.x, player_rect.y))
            if r_n == 1:
                level_4.blit(right2, (player_rect.x, player_rect.y))
            if r_n == 3:
                level_4.blit(right3, (player_rect.x, player_rect.y))
                r_n = 0
            player_rect.x += vitesse
            r_n += 1

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

        # on definit et on affiche le text HEALTH a l'écran
        font = pg.font.SysFont('Operator', 55)
        text_f = font.render("health:", False, (0, 0, 0))
        level_4.blit(text_f, (0, 0))

        Clock.tick(10)
        pg.display.flip()

with open('saves/saves.txt', 'r+') as save:
    verif = save.read()
if "level3" in verif:
    level4()
if "level2" in verif:
    level3()
if "level1" in verif:
    level2()
else:
    main_menu()