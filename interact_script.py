import pygame as pg

buche = 0

take = ['rock not take', 'rock2 not take']
take_k = ['key not take', 'key2 not take']

rock = pg.image.load('environement/interact/rock.png')
rock2 = pg.image.load('environement/interact/rock.png')

button1_p = pg.image.load('environement/interact/button_up.png')
button1_d = pg.image.load('environement/interact/button_down.png')

button2_p = pg.image.load('environement/interact/button_up.png')
button2_d = pg.image.load('environement/interact/button_down.png')

borne_d = pg.image.load("environement/interact/borne d'indice.png")

key = pg.image.load('environement/interact/key.png')

key2 = pg.image.load('environement/interact/key.png')

porte = pg.image.load('environement/interact/porte fermer.png')

porte_hitbox = pg.image.load('environement/interact/porte hitbox.png')

porte2 = pg.image.load('environement/interact/porte2.png')

jean_pierre = pg.image.load('environement/interact/pnj.png')

baque1_remplit = pg.image.load('environement/interact/baque tomate.png')
baque2_remplit = pg.image.load('environement/interact/baque tomate.png')

drop_zone = pg.image.load('environement/interact/drop_zone.png')

broken_bridge = pg.image.load('environement/interact/bridge broken.png')

bridge = pg.image.load('environement/interact/bridge.png')

jeton_int = pg.image.load('environement/interact/jeton_interact.png')

jeton_int_rect = jeton_int.get_rect()

bridge_rect = bridge.get_rect()
bridge_rect.x, bridge_rect.y = 490, 197

broken_bridge_rect = broken_bridge.get_rect()
broken_bridge_rect.x, broken_bridge_rect.y = 490, 197
broken_bridge_mask = pg.mask.from_surface(broken_bridge)
mask_broken_bridge = broken_bridge_mask.to_surface()

drop_zone_rect = drop_zone.get_rect()
drop_zone_rect.x, drop_zone_rect.y = 184, 513

baque2_remplit_rect = baque2_remplit.get_rect()
baque2_remplit_rect.x, baque2_remplit_rect.y = 750, 550
baque2_mask = pg.mask.from_surface(baque2_remplit)
mask_baque2 = baque2_mask.to_surface()

baque1_remplit_rect = baque1_remplit.get_rect()
baque1_remplit_rect.x, baque1_remplit_rect.y = 750, 630
baque1_mask = pg.mask.from_surface(baque1_remplit)
mask_baque1 = baque1_mask.to_surface()

jean_pierre_rect = jean_pierre.get_rect()
jean_pierre_rect.x, jean_pierre_rect.y = 85, 425

porteh_rect = porte_hitbox.get_rect()
porteh_rect.x, porteh_rect.y = 414, 200

porte_rect = porte.get_rect()
porte_rect.x, porte_rect.y = 414, 200
porte_mask = pg.mask.from_surface(porte)

key2_rect = key2.get_rect()
key2_rect.x, key2_rect.y = 0, 0

key_rect = key.get_rect()
key_rect.x, key_rect.y = 230, 285

borne_d_rect = borne_d.get_rect()
borne_d_rect.x, borne_d_rect.y = 700, 770
borne_d_mask = pg.mask.from_surface(borne_d)

button1_rect = button1_d.get_rect()
button1_rect.x, button1_rect.y = 230, 120

button2_rect = button2_d.get_rect()
button2_rect.x, button2_rect.y = 615, 485

rock1_rect = rock.get_rect()
rock1_rect.x, rock1_rect.y = 432, 365

rock2_rect = rock2.get_rect()
rock2_rect.x, rock2_rect.y = 550, 735