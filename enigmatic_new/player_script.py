import pygame as pg

#animation front
front1 = pg.image.load('player/front1.png')
front2 = pg.image.load('player/front2.png')
front3 = pg.image.load('player/front3.png')

#animation left
left1 = pg.image.load('player/left1.png')
left2 = pg.image.load('player/left2.png')
left3 = pg.image.load('player/left3.png')

#animation right
right1 = pg.image.load('player/right1.png')
right2 = pg.image.load('player/right2.png')
right3 = pg.image.load('player/right3.png')

#animation back
back1 = pg.image.load('player/back1.png')
back2 = pg.image.load('player/back2.png')
back3 = pg.image.load('player/back3.png')

mask_front1 = pg.image.load('player/mask_front1.png')

front_rect = front1.get_rect()

mask_front1_rect = mask_front1.get_rect()

player_rect = mask_front1.get_rect()
player_mask = pg.mask.from_surface(mask_front1)
mask_player = player_mask.to_surface()