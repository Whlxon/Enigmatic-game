import pygame as pg

hitbox1 = pg.image.load('environement/background/hitbox1.png')
background = pg.image.load('environement/background/background1.png')

cache = pg.image.load('environement/background/hidde.png')

background2 = pg.image.load('environement/background/background2.png')
hitbox2 = pg.image.load('environement/background/hitbox2.png')

background3 = pg.image.load('environement/background/background3.png')
hitbox3 = pg.image.load('environement/background/hitbox3.png')

chatbox = pg.image.load('environement/interact/chatbox.png')
chatindice = pg.image.load('environement/interact/chatindice.png')

hitbox1_rect = hitbox1.get_rect()
hitbox1_mask = pg.mask.from_surface(hitbox1)

hitbox2_rect = hitbox2.get_rect()
hitbox2_mask = pg.mask.from_surface(hitbox2)

hitbox3_rect = hitbox3.get_rect()
hitbox3_mask = pg.mask.from_surface(hitbox3)